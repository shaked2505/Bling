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

@application.route("/")
def landing():
    # db.session.add(Trainer(66, 'Miri Bar Lev', 'Power and MatPilates', str(date(2022, 7, 18)), '12-294-972547', 'miri@gmail.com', '052-8653908', 'MiriBarLev66', '65.00', 1111))
    # db.session.add(BrandedMerchandise(300, 50.00, 20, 'Water Bottle', 'Stainless steel bottle, contains 500 ml', 1111, None))
    # db.session.add(SystemManager(1111, 'Bar Diamant',  '10-350-789543', 'bar154@gmail.com', '054-7895279', 'Bar Diamant1111'))
    # db.session.commit()
    return render_template("test.html")

@application.route("/schedule")
def schedule():
    return render_template("schedule.html")

if __name__ == '__main__':
    with application.app_context():
        # Create the database tables 
        db.create_all()
    application.run()
