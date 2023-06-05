from datetime import date, time
from app import db

class SpecificTimeTraining(db.Model):
    specificTimeTrainingDate = db.Column(db.Date, primary_key=True)
    trainingID = db.Column(db.Integer,db.ForeignKey('training.trainingID'), primary_key=True)
    training = db.relationship('Training', foreign_keys=[trainingID])
    startTime = db.Column(db.Time)
    endTime = db.Column(db.Time)
    standByTrainer= db.Column(db.Integer,db.ForeignKey('trainer.trainerID') ) 
    stand_by_trainer = db.relationship('Trainer', foreign_keys=[standByTrainer], uselist=False)
    trainerID= db.Column(db.Integer,db.ForeignKey('trainer.trainerID') ) 
    trainer = db.relationship('Trainer', foreign_keys=[trainerID], uselist=False)

    def __init__(self, specificTimeTrainingDate, trainingID, startTime, endTime, standByTrainer, trainerID):
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.trainingID = trainingID
        self.startTime = startTime
        self.endTime = endTime
        self.standByTrainer = standByTrainer
        self.trainerID = trainerID
