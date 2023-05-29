class TrainingCancellationRequestForm:
    def __init__(self, requestID, memberID, trainingID, specificTimeTrainingDate, reason, approvalStatus):
        self.requestID = requestID
        self.memberID = memberID
        self.trainingID = trainingID
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.reason = reason
        self.approvalStatus = approvalStatus

    def getRequestDetails(self, requestID):
        pass
    def isConfirmed(self, requestID):
        pass
    def cancel_registration(self):
        pass
