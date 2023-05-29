class TrainingRegistrationForm:
    def __init__(self, registrationID, memberID, trainingID, registrationDate, approvalStatus):
        self.registrationID = registrationID
        self.memberID = memberID
        self.trainingID = trainingID
        self.registrationDate = registrationDate
        self.approvalStatus = approvalStatus

    def getRegistrationDetails(self, registrationID):
        pass
    def checkAvailability(self, specificTimeTraining):
        pass
    def isConfirmed(self, registrationID):
        pass
    def register(self):
      pass


