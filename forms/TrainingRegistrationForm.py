import datetime
from sqlalchemy import ForeignKeyConstraint
from main_services.SpecificTimeTraining import SpecificTimeTraining
from app import db

class TrainingRegistrationForm(db.Model):
    registrationID = db.Column(db.Integer, primary_key=True)
    traineeID = db.Column(db.Integer, db.ForeignKey('trainee.traineeID'))
    trainee = db.relationship('Trainee', foreign_keys=[traineeID])
    trainingID = db.Column(db.Integer)
    specificTimeTrainingDate = db.Column(db.Date)
    __table_args__ = (ForeignKeyConstraint([specificTimeTrainingDate, trainingID],
                                    [SpecificTimeTraining.specificTimeTrainingDate, SpecificTimeTraining.trainingID]),
                    {})
    reason = db.Column(db.String)
    requestDate = db.Column(db.Date, default=datetime.date.today())
    approvalStatus = db.Column(db.String)

    # Create initializer/constructor
    def __init__(self, registrationID, traineeID,trainingID ,specificTimeTrainingDate, reason, requestDate, approvalStatus):
        self.registrationID = registrationID
        self.traineeID = traineeID
        self.trainingID = trainingID
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.reason = reason
        self.requestDate = requestDate
        self.approvalStatus = approvalStatus



# class TrainingRegistrationForm:
#     def __init__(self, connector,registrationID, memberID, trainingID, specificTimeTrainingDate ,approvalStatus):
#         self.registrationID = registrationID
#         self.memberID = memberID
#         self.trainingID = trainingID
#         self.specificTimeTrainingDate = specificTimeTrainingDate
#         self.requestDate = datetime.date.today()
#         self.approvalStatus = approvalStatus
#         self.connector=connector


#         sql= "INSERT INTO TrainingRegistrationForm (registrationID, memberID, trainingID, specificTimeTrainingDate,  approvalStatus,  requestDate) VALUES (?, ?, ?, ?, ?, ?)"
#         values = (self.registrationID, self.memberID, self.trainingID,str(self.specificTimeTrainingDate) , self.approvalStatus, str(self.requestDate))
#         self.connector.execute_query(sql, values)

#     def set_registrationID(self, registrationID):
#         sql = "UPDATE TrainingRegistrationForm SET registrationID=? WHERE registrationID=?;"
#         values = (registrationID, self.registrationID)
#         self.connector.execute_query(sql, values)
#         self.registrationID = registrationID

#     def delete(self):
#         sql = "DELETE FROM TrainingRegistrationForm WHERE registrationID=?;"
#         self.connector.execute_query(sql, self.registrationID)




    def getRegistrationDetails(self, registrationID):
        return self.registrationID

    def checkAvailability(self, specificTimeTraining):
        pass
    def isConfirmed(self):
        self.approvalStatus

    def register(self):
      pass


