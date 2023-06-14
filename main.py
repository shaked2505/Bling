from datetime import date
from flask import render_template, request, redirect, url_for, jsonify, Response 
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app import db, application
from users.Trainer import Trainer
from users.Trainee import Trainee
from users.SystemManager import SystemManager
from incomes.BrandedMerchandise import BrandedMerchandise
from incomes.MembershipPlan import MembershipPlan
from incomes.Payment import Payment
from main_services.Training import Training
from main_services.SpecificTimeTraining import SpecificTimeTraining
from datetime import datetime,timedelta
from forms.MembershipCancellationRequestForm import MembershipCancellationRequestForm
from forms.TrainingCancellationRequestForm import TrainingCancellationRequestForm
from forms.TrainingRegistrationForm import TrainingRegistrationForm
import add_to_db as ad_db
from sqlalchemy import asc,func
import smtplib
from email.mime.text import MIMEText
import csv
from io import StringIO

login_manager = LoginManager()
login_manager.init_app(application)

def is_admin():
    user = current_user._get_current_object()
    if type(user) == SystemManager:
        return True
    else:
        return False


@application.route('/', methods=['GET', 'POST'])
def login():
    error=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = Trainee.query.filter_by(traineeID=username).first()
        if not user:
            user = SystemManager.query.filter_by(managerID=username).first()
        if user is not None and user.loginDetails == password:
            login_user(user)  # Create a session for the user
            return redirect(url_for('home'))
        else:
            error = "Invalied Username/Password"
    return render_template('login.html',error=error)

@application.route("/home")
@login_required
def home():
    user = current_user._get_current_object()
    admin = is_admin()
    showCancelProcess = True
    cancle = None
    if not admin:
        trainee = current_user._get_current_object()
        cancle = MembershipCancellationRequestForm.query.filter(
            MembershipCancellationRequestForm.traineeID==trainee.traineeID,
            MembershipCancellationRequestForm.approvalStatus=="In Process"
        ).first()
        print(cancle)
        if cancle:
            showCancelProcess = False   
    return render_template("home.html", is_admin=admin, trainee=user, showCancelProcess=showCancelProcess, cancle=cancle )

@application.route("/membership-cancellation" , methods=['POST'])
@login_required
def membership_cancellation():
    traineeID = request.form['traineeID']
    membershipID = request.form['membershipID']
    reason = request.form['reason']
    approvalStatus = request.form['approvalStatus']
    obj = MembershipCancellationRequestForm(traineeID, membershipID, reason, approvalStatus)
    db.session.add(obj)
    db.session.commit()
    return redirect(url_for('home'))

@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@application.route("/trainingReg")
def trainingReg():
    return render_template("trainingReg.html")

@application.route("/create_records")
def create_records():
    # ad_db.create_Trainings()
    # ad_db.create_SystemManager()
    # ad_db.create_MembershipPlan()
    # ad_db.create_Trainer()
    # ad_db.create_BrandedMerchandise()
    # ad_db.create_Trainee()
    ad_db.create_Payment()
    # # ad_db.create_SpecificTimeTraining()
    # ad_db.create_MembershipCancellationRequestForm()
    # ad_db.create_TrainingRegistrationForm()
    # ad_db.create_TrainingCancellationRequestForm()
    return render_template("test.html")

@application.route("/schedule")
@login_required
def schedule():
    current_date = datetime.now().date()
    current_time = datetime.now().time()
    # Filter objects based on the current date and time
    filtered_schedules = SpecificTimeTraining.query.filter(
        SpecificTimeTraining.specificTimeTrainingDate >= current_date).order_by(
        asc(SpecificTimeTraining.specificTimeTrainingDate)).all()

    map={}
    for i in filtered_schedules:
        if i.specificTimeTrainingDate not in map.keys():
            map[i.specificTimeTrainingDate]=[i]
        else:
            map[i.specificTimeTrainingDate].append(i)
    for i in map.keys():
        map[i] =  sorted(map[i], key=lambda obj: obj.startTime)
    
    if current_date in map.keys():
        for i in range(len(map[current_date])-1, -1, -1):
            print(i)
            if map[current_date][i].startTime <= current_time:
                map[current_date].pop(i)

    for i in map:
        print("-------------------")
        print(f"date = {i}")
        print("-------------------")
        for j in map[i]:
            print(j.startTime)

    trainers_map={}
    trainers = Trainer.query.all()
    for trainer in trainers:
        trainers_map[trainer.trainerID] = trainer

    trainings_map={}
    trainings = Training.query.all()
    for training in trainings:
        trainings_map[training.trainingID] = training
    
    admin = is_admin()
    registers_map={}
    if not admin:
        traineeID = current_user._get_current_object().traineeID
        registers = TrainingRegistrationForm.query.filter(
            TrainingRegistrationForm.traineeID == traineeID).all()
        for register in registers:
            registers_map[f"{register.trainingID}/{register.specificTimeTrainingDate}"] = register



    schedule_capacity_map = {}
    for schedule in filtered_schedules:
        schedule_capacity_map[f"{schedule.trainingID}/{schedule.specificTimeTrainingDate}"]={
            "capacity":trainings_map[schedule.trainingID].capacity, "utilization": 0}

    schedules_utilizations = db.session.query(
        TrainingRegistrationForm.specificTimeTrainingDate,
        TrainingRegistrationForm.trainingID,
        func.count(TrainingRegistrationForm.registrationID)
    ).filter(
        TrainingRegistrationForm.specificTimeTrainingDate >= current_date
    ).group_by(
        TrainingRegistrationForm.specificTimeTrainingDate,
        TrainingRegistrationForm.trainingID
    ).all()

    for schedule in schedules_utilizations:
         schedule_capacity_map[f"{schedule.trainingID}/{schedule.specificTimeTrainingDate}"]["utilization"]=schedule[2]

    return render_template("schedule.html",schedule_map=map, trainers=trainers_map, trainings=trainings_map, is_admin=admin, registers = registers_map, schedule_capacity_map=schedule_capacity_map)


@application.route("/training-registration" , methods=['POST'])
@login_required
def training_registration():
    trainingID = request.form['trainingID']
    specificTimeTrainingDate = request.form['specificTimeTrainingDate']
    trainee = current_user._get_current_object()
    obj=TrainingRegistrationForm(trainee.traineeID, trainingID, 'Approved',specificTimeTrainingDate)
    db.session.add(obj)
    db.session.commit()
    return redirect(url_for('schedule'))

@application.route("/training-cancelation" , methods=['POST'])
@login_required
def training_cancelation():
    trainingID = request.form['trainingID']
    specificTimeTrainingDate = request.form['specificTimeTrainingDate']
    reason = request.form['reason']
    trainee = current_user._get_current_object()
    obj=TrainingCancellationRequestForm(trainee.traineeID, reason, 'Approved', specificTimeTrainingDate, trainingID)
    db.session.add(obj)
    db.session.commit()
    obj=TrainingRegistrationForm.query.filter(
            TrainingRegistrationForm.traineeID == trainee.traineeID,
            TrainingRegistrationForm.specificTimeTrainingDate == specificTimeTrainingDate, 
            TrainingRegistrationForm.trainingID == trainingID).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect(url_for('schedule'))

@application.route("/membership-resume" , methods=['POST'])
@login_required
def membership_resume():
    traineeID = request.form['traineeID']
    membershipID = request.form['membershipID']
    obj=MembershipCancellationRequestForm.query.filter(
            MembershipCancellationRequestForm.traineeID == traineeID,
            MembershipCancellationRequestForm.membershipID == membershipID,
            MembershipCancellationRequestForm.approvalStatus == "In Process").first()
    obj.approvalStatus = "Cancel"    
    db.session.commit()
    return redirect(url_for('home'))


def get_report_map(startDate, endDate, incomeType):
    trainee_map={}
    trainees = Trainee.query.all()
    for trainee in trainees:
        trainee_map[trainee.traineeID] = trainee

    merch_map={}
    merches = BrandedMerchandise.query.all()
    for merch in merches:
        merch_map[merch.productID] = merch

    memb_map={}
    membs = MembershipPlan.query.all()
    for memb in membs:
        memb_map[memb.membershipID] = memb

    ret_data = []
    if incomeType == "mem_plans":
        payments = Payment.query.filter(
            Payment.dateOfPayment <= endDate,
            Payment.dateOfPayment >= startDate,
            Payment.productID == None
        ).all()
        for payment in payments:
            payment_data = {
                'id': payment.paymentID,
                'traineeID': trainee_map[payment.traineeID].traineeFullName,
                'date_of_payment': payment.dateOfPayment.strftime('%d/%m/%Y'),
                'amount': payment.amount,
                'membershipID': memb_map[payment.membershipID].membershipPlanType
            }
            ret_data.append(payment_data)
    elif incomeType == "branded":
        payments = Payment.query.filter(
            Payment.dateOfPayment <= endDate,
            Payment.dateOfPayment >= startDate,
            Payment.productID != None
        ).all()
        for payment in payments:
            payment_data = {
                'id': payment.paymentID,
                'traineeID': trainee_map[payment.traineeID].traineeFullName,
                'date_of_payment': payment.dateOfPayment.strftime('%d/%m/%Y'),
                'amount': payment.amount,
                'productID': merch_map[payment.productID].productName,
            }
            ret_data.append(payment_data)
    else:
        payments = Payment.query.filter(
            Payment.dateOfPayment <= endDate,
            Payment.dateOfPayment >= startDate
        ).all()
        for payment in payments:
            if payment.productID:
                product =  merch_map[payment.productID].productName
                memb = None
            else:
                product =  None
                memb = memb_map[payment.membershipID].membershipPlanType      
            payment_data = {
                'id': payment.paymentID,
                'traineeID': trainee_map[payment.traineeID].traineeFullName,
                'date_of_payment': payment.dateOfPayment.strftime('%d/%m/%Y'),
                'amount': payment.amount,
                'productID': product,
                'membershipID': memb
            }
            ret_data.append(payment_data)
    return ret_data


@application.route("/get_data_to_report" , methods=['POST'])
@login_required
def get_data_to_report():
    data = request.get_json()
    startDate = data['startDate']
    endDate = data['endDate']
    incomeType = data['incomeType']

    data = get_report_map(startDate, endDate, incomeType)

    return jsonify(data)

@application.route("/get_report", methods=['POST'])
@login_required
def get_report():
    data = request.get_json()
    startDate = data['startDate']
    endDate = data['endDate']
    incomeType = data['incomeType']

    ret_data = get_report_map(startDate, endDate, incomeType)

    return jsonify(ret_data)


def get_report_map(startDate, endDate, incomeType):
    trainee_map = {}
    trainees = Trainee.query.all()
    for trainee in trainees:
        trainee_map[trainee.traineeID] = trainee

    merch_map = {}
    merches = BrandedMerchandise.query.all()
    for merch in merches:
        merch_map[merch.productID] = merch

    memb_map = {}
    membs = MembershipPlan.query.all()
    for memb in membs:
        memb_map[memb.membershipID] = memb

    ret_data = []
    total_income = 0  # Initialize total income variable

    if incomeType == "mem_plans":
        payments = Payment.query.filter(
            Payment.dateOfPayment <= endDate,
            Payment.dateOfPayment >= startDate,
            Payment.productID == None
        ).all()
        for payment in payments:
            payment_data = {
                'id': payment.paymentID,
                'traineeID': trainee_map[payment.traineeID].traineeFullName,
                'date_of_payment': payment.dateOfPayment.strftime('%d/%m/%Y'),
                'amount': payment.amount,
                'membershipID': memb_map[payment.membershipID].membershipPlanType
            }
            ret_data.append(payment_data)
            total_income += payment.amount  # Add payment amount to total income
        summary_line = {
            'id': 'Summary',
            'traineeID': 'Total Income:',
            'date_of_payment': '',
            'amount': total_income,
            'membershipID': ''
        }
        ret_data.append(summary_line)
    elif incomeType == "branded":
        payments = Payment.query.filter(
            Payment.dateOfPayment <= endDate,
            Payment.dateOfPayment >= startDate,
            Payment.productID != None
        ).all()
        for payment in payments:
            payment_data = {
                'id': payment.paymentID,
                'traineeID': trainee_map[payment.traineeID].traineeFullName,
                'date_of_payment': payment.dateOfPayment.strftime('%d/%m/%Y'),
                'amount': payment.amount,
                'productID': merch_map[payment.productID].productName,
            }
            ret_data.append(payment_data)
            total_income += payment.amount  # Add payment amount to total income
        summary_line = {
            'id': 'Summary',
            'traineeID': 'Total Income:',
            'date_of_payment': '',
            'amount': total_income,
            'productID': '',
        }
        ret_data.append(summary_line)
    else:
        payments = Payment.query.filter(
            Payment.dateOfPayment <= endDate,
            Payment.dateOfPayment >= startDate
        ).all()
        for payment in payments:
            if payment.productID:
                product = merch_map[payment.productID].productName
                memb = None
            else:
                product = None
                memb = memb_map[payment.membershipID].membershipPlanType
            payment_data = {
                'id': payment.paymentID,
                'traineeID': trainee_map[payment.traineeID].traineeFullName,
                'date_of_payment': payment.dateOfPayment.strftime('%d/%m/%Y'),
                'amount': payment.amount,
                'productID': product,
                'membershipID': memb
            }
            ret_data.append(payment_data)
            total_income += payment.amount  # Add payment amount to total income
        summary_line = {
            'id': 'Summary',
            'traineeID': 'Total Income:',
            'date_of_payment': '',
            'amount': total_income,
            'productID': '',
            'membershipID': ''
        }
        ret_data.append(summary_line)

    # Add summary line to ret_data

    return ret_data


@application.route("/get_report_csv" , methods=['POST'])
def get_report_csv():
    data = request.get_json()
    startDate = data['startDate']
    endDate = data['endDate']
    incomeType = data['incomeType']

    data = get_report_map(startDate, endDate, incomeType)

    keys = data[0].keys()

    # Create a CSV file in memory
    csv_output = StringIO()
    csv_writer = csv.DictWriter(csv_output, fieldnames=keys)
    csv_writer.writeheader()
    csv_writer.writerows(data)

    headers = {
        'Content-Disposition': 'attachment; filename=data.csv',
        'Content-Type': 'text/csv'
    }
    print("-------------------")
    return Response(
        csv_output.getvalue(),
        mimetype='text/csv',
        headers=headers
    )


@application.route("/data_report" , methods=['GET'])
@login_required
def data_report():
    return render_template('DataReport.html')




@application.route("/send_mail" , methods=['POST'])
def send_email():
    managers=SystemManager.query.all()
    recipients = []
    for manager in managers:
        recipients.append(manager.email)
    trainee = current_user._get_current_object()
    subject = "Trainee sum on 'Cancle Membership'"
    body = f"The trainee {trainee.traineeID, trainee.traineeFullName} pushed on 'Cancle Membership'"
    sender = "blingboutiquestudio@gmail.com"
    password = "jiyhhmzailtggayu"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    return "sent mail to system manager"


@login_manager.user_loader
def load_user(user_id):
    user = Trainee.query.get(user_id)
    if not user:
        user = SystemManager.query.get(user_id)
    return user

if __name__ == '__main__':
    with application.app_context():
        # Create the database tables 
        db.create_all()
    application.run(debug=True)


