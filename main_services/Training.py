import datetime
from app import db

class Training(db.Model):
    trainingID = db.Column(db.Integer, primary_key=True)
    trainingType = db.Column(db.String)
    capacity = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    trainingDescription= db.Column(db.String)
   
    # Create initializer/constructor
    def __init__(self, trainingID, trainingType, capacity, duration,trainingDescription):
        self.trainingID = trainingID
        self.trainingType = trainingType
        self.capacity = capacity
        self.duration = duration
        self.trainingDescription= trainingDescription
    def getTrainer(self, Trainer):
        pass
    def setTrainer(self, Trainer):
        pass
    def getCapacity(self, capacity):
        pass
    def setCapacity(self, capacity):
        pass










