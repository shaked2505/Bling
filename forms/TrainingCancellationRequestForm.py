import datetime
from app import db

class TrainingCancellationRequestForm(db.Model):
    requestID = db.Column(db.Integer, primary_key=True)
    traineeID = db.Column(db.Integer, db.ForeignKey('trainee.traineeID'))
    trainee = db.relationship('Trainee', backref=db.backref('trainee', uselist=False))
    reason = db.Column(db.String)
    approvalStatus = db.Column(db.String)
    specificTimeTrainingDate = db.Column(db.Date, db.ForeignKey('specific_time_training.specificTimeTrainingDate'))
    specific_time_training_date = db.relationship('SpecificTimeTraining', backref=db.backref('specific_time_training', uselist=False))
    trainingID = db.Column(db.Integer, db.ForeignKey('specific_time_training.trainingID'))
    specific_time_training_id = db.relationship('SpecificTimeTraining', backref=db.backref('specific_time_training', uselist=False))
    requestDate = db.Column(db.DateTime, default=datetime.date.today())

    def __init__(self, requestID, traineeID, reason, approvalStatus, specificTimeTrainingDate, trainingID):
        self.requestID = requestID
        self.traineeID = traineeID
        self.reason = reason
        self.requestDate = requestDate
        self.approvalStatus = approvalStatus
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.trainingID = trainingID
        self.requestDate = datetime.date.today()

    def isConfirmed(self, requestID):
        return self.approvalStatus


    def cancel_registration(self):
        pass




