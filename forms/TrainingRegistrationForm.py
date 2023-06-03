import datetime
class TrainingRegistrationForm:
    def __init__(self, connector,registrationID, memberID, trainingID, specificTimeTrainingDate ,approvalStatus):
        self.registrationID = registrationID
        self.memberID = memberID
        self.trainingID = trainingID
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.requestDate = datetime.date.today()
        self.approvalStatus = approvalStatus
        self.connector=connector


        sql= "INSERT INTO TrainingRegistrationForm (registrationID, memberID, trainingID, specificTimeTrainingDate,  approvalStatus,  requestDate) VALUES (?, ?, ?, ?, ?, ?)"
        values = (self.registrationID, self.memberID, self.trainingID,str(self.specificTimeTrainingDate) , self.approvalStatus, str(self.requestDate))
        self.connector.execute_query(sql, values)

    def set_registrationID(self, registrationID):
        sql = "UPDATE TrainingRegistrationForm SET registrationID=? WHERE registrationID=?;"
        values = (registrationID, self.registrationID)
        self.connector.execute_query(sql, values)
        self.registrationID = registrationID

    def delete(self):
        sql = "DELETE FROM TrainingRegistrationForm WHERE registrationID=?;"
        self.connector.execute_query(sql, self.registrationID)












    def getRegistrationDetails(self, registrationID):
        pass
    def checkAvailability(self, specificTimeTraining):
        pass
    def isConfirmed(self, registrationID):
        pass
    def register(self):
      pass


