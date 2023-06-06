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
from sqlalchemy import asc

@application.route("/")
def login():
    return render_template("login.html")

@application.route("/can")
def can():
    return render_template("membershipCan.html")


@application.route("/home")
def home():
    return render_template("home.html")

@application.route("/create_records")
def create_records():
    ad_db.create_Trainings()
    ad_db.create_SystemManager()
    ad_db.create_MembershipPlan()
    ad_db.create_Trainer()
    ad_db.create_BrandedMerchandise()
    ad_db.create_Trainee()
    ad_db.create_Payment()
    ad_db.create_SpecificTimeTraining()
    # ad_db.create_MembershipCancellationRequestForm()
    # ad_db.create_TrainingRegistrationForm()
    # ad_db.create_TrainingCancellationRequestForm()
    return render_template("test.html")

@application.route("/schedule")
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
            map[i.specificTimeTrainingDate]=[]
        else:
            map[i.specificTimeTrainingDate].append(i)
    for key in map.keys():
        print(key)
    for i in map.keys():
        map[i] =  sorted(map[i], key=lambda obj: obj.startTime)
    
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

    return render_template("schedule.html",schedule_map=map, trainers=trainers_map, trainings=trainings_map)


if __name__ == '__main__':
    with application.app_context():
        # Create the database tables 
        db.create_all()
    application.run()


