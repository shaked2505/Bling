from datetime import date
from flask import render_template
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

@application.route("/")
def home():
    return render_template("login.html")

@application.route("/home")
def login():
    return render_template("home.html")

@application.route("/membershipCan")
def member():
    return render_template("membershipCan.html")

@application.route("/create_records")
def create_records():
    ad_db.create_Trainings()
    ad_db.create_SystemManager()
    ad_db.create_MembershipPlan()
    ad_db.create_Trainer()
    ad_db.create_BrandedMerchandise()
    ad_db.create_Trainee()
    ad_db.create_MembershipCancellationRequestForm()
    ad_db.create_Payment()
    ad_db.create_SpecificTimeTraining()
    ad_db.create_TrainingRegistrationForm()
    ad_db.create_TrainingCancellationRequestForm()
    return render_template("test.html")

@application.route("/schedule")
def schedule():
    current_date = datetime.now().date()

    # Calculate the start and end dates of the current week
    start_of_week = current_date - timedelta(days=current_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    time_schedules = Trainer.query.all()
    # time_schedules = SpecificTimeTraining.query.filter(SpecificTimeTraining.specificTimeTrainingDate.between(start_of_week, end_of_week)).all()
    print(f"test {time_schedules}")
    return render_template("schedule.html")


if __name__ == '__main__':
    with application.app_context():
        # Create the database tables 
        db.create_all()
    application.run()


