import datetime
from sqlalchemy import ForeignKeyConstraint
from main_services.SpecificTimeTraining import SpecificTimeTraining
from app import db

class TrainingCancellationRequestForm(db.Model):
    requestID = db.Column(db.Integer, primary_key=True)
    traineeID = db.Column(db.String(9), db.ForeignKey('trainee.traineeID'))
    trainee = db.relationship('Trainee', foreign_keys=[traineeID])
    trainingID = db.Column(db.Integer)
    specificTimeTrainingDate = db.Column(db.Date)
    __table_args__ = (ForeignKeyConstraint([specificTimeTrainingDate, trainingID],
                                        [SpecificTimeTraining.specificTimeTrainingDate, SpecificTimeTraining.trainingID]),
                    {})
    Specific_Time_Training = db.relationship('SpecificTimeTraining', foreign_keys=[specificTimeTrainingDate, trainingID])
    reason = db.Column(db.String)
    requestDate = db.Column(db.Date)
    approvalStatus = db.Column(db.String)

    # Create initializer/constructor
    def __init__(self, requestID, traineeID, reason, approvalStatus, specificTimeTrainingDate, trainingID, requestDate=datetime.date.today()):
        self.requestID = requestID
        self.traineeID = traineeID
        self.trainingID = trainingID
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.reason = reason
        self.requestDate = requestDate
        self.approvalStatus = approvalStatus



# class TrainingCancellationRequestForm:
#     def __init__(self, connector,requestID, memberID, trainingID, specificTimeTrainingDate, reason, approvalStatus):
#         self.requestID = requestID
#         self.memberID = memberID
#         self.trainingID = trainingID
#         self.specificTimeTrainingDate = specificTimeTrainingDate
#         self.reason = reason
#         self.approvalStatus = approvalStatus
#         self.requestDate = datetime.date.today()
#         self.connector = connector


#         sql= "INSERT INTO TrainingCancellationRequestForm (requestID, memberID, trainingID, specificTimeTrainingDate, reason, approvalStatus,  requestDate) VALUES (?, ?, ?, ?, ?, ?, ?)"
#         values = (self.requestID, self.memberID, self.trainingID,str(self.specificTimeTrainingDate) ,self.reason, self.approvalStatus, str(self.requestDate))
#         self.connector.execute_query(sql, values)

#     def set_requestID(self, requestID):
#         sql = "UPDATE TrainingCancellationRequestForm SET requestID=? WHERE requestID=?;"
#         values = (requestID, self.requestID)
#         self.connector.execute_query(sql, values)
#         self.requestID = requestID

#     def delete(self):
#         sql = "DELETE FROM TrainingCancellationRequestForm WHERE requestID=?;"
#         self.connector.execute_query(sql, self.requestID)


    def getRequestDetails(self):
        return self.requestID


    def isConfirmed(self, requestID):
        return self.approvalStatus


    def cancel_registration(self):
        pass




