from datetime import date, time
from app import db

class SpecificTimeTraining(db.Model):
    specificTimeTrainingDate = db.Column(db.Date, primary_key=True)
    trainingID = db.Column(db.Integer,db.ForeignKey('training.trainingID'), primary_key=True ) 
    training = db.relationship('Training', backref=db.backref('training', uselist=False))
    startTime = db.Column(db.Time)
    endTime = db.Column(db.Time)
    standByTrainer= db.Column(db.Integer,db.ForeignKey('trainer.trainerID') ) 
    trainer = db.relationship('Trainer', backref=db.backref('trainer', uselist=False))
    trainerID= db.Column(db.Integer,db.ForeignKey('trainer.trainerID') ) 
    trainer = db.relationship('Trainer', backref=db.backref('trainer', uselist=False))


class SpecificTimeTraining:
    def __init__(self, specificTimeTrainingDate, trainingID, startTime, endTime, standByTrainer, registeredTrainees):
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.trainingID = trainingID
        self.startTime = startTime
        self.endTime = endTime
        self.standByTrainer = standByTrainer

    def getStartTime(self, startTime):
        pass
    def setStartTime(self, startTime):
        pass
    def getEndTime(self, endTime):
        pass
    def setEndTime(self, endTime):
        pass
    def updateStandByTrainer(self, standByTrainer):
        pass
    def getRegisteredTrainees(self, registeredTrainees):
        pass



