import datetime
class TrainingCancellationRequestForm:
    def __init__(self, connector,requestID, memberID, trainingID, specificTimeTrainingDate, reason, approvalStatus):
        self.requestID = requestID
        self.memberID = memberID
        self.trainingID = trainingID
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.reason = reason
        self.approvalStatus = approvalStatus
        self.requestDate = datetime.date.today()
        self.connector = connector


        sql= "INSERT INTO TrainingCancellationRequestForm (requestID, memberID, trainingID, specificTimeTrainingDate, reason, approvalStatus,  requestDate) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (self.requestID, self.memberID, self.trainingID,str(self.specificTimeTrainingDate) ,self.reason, self.approvalStatus, str(self.requestDate))
        self.connector.execute_query(sql, values)

    def set_requestID(self, requestID):
        sql = "UPDATE TrainingCancellationRequestForm SET requestID=? WHERE requestID=?;"
        values = (requestID, self.requestID)
        self.connector.execute_query(sql, values)
        self.requestID = requestID

    def delete(self):
        sql = "DELETE FROM TrainingCancellationRequestForm WHERE requestID=?;"
        self.connector.execute_query(sql, self.requestID)


    def getRequestDetails(self, requestID):
        pass
    def isConfirmed(self, requestID):
        pass
    def cancel_registration(self):
        pass




