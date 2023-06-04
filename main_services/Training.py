import datetime
from app import db

class Training(db.Model):
    trainingID = db.Column(db.Integer, primary_key=True)
    trainingType = db.Column(db.String)
    capacity = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    trainingDescription= db.Column(db.String)
   
    # Create initializer/constructor
    def __init__(self, membershipID, membershipPlanDescription, price, membershipPlanType):
        self.membershipID = membershipID
        self.membershipPlanDescription = membershipPlanDescription
        self.price = price
        self.membershipPlanType = membershipPlanType
      
    def getTrainer(self, Trainer):
        pass
    def setTrainer(self, Trainer):
        pass
    def getCapacity(self, capacity):
        pass
    def setCapacity(self, capacity):
        pass










