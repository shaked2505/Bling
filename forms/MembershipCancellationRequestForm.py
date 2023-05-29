class MembershipCancellationRequestForm:
    def __init__(self):
        self.requestID = 0  # int
        self.memberID = Trainee()  # Trainee (assuming Trainee is a class)
        self.planID = MembershipPlan()  # MembershipPlan (assuming MembershipPlan is a class)
        self.reason = ""  # str
        self.requestDate = None  # date (assuming date is a valid date type)
        self.approvalStatus = ""  # str
    
    def getRequestDetails(self, requestID):
        pass
    def isPending(self, requestID):
        pass
    def notificationEmailToSystemManager(self, systemManager):
        pass




