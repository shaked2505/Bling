class Trainee:
    def __init__(self, traineeID, traineeFullName, bankAccount):
        self.traineeID = 0
        self.traineeFullName = ""
        self.bankAccount = ""
        self.joiningDate = None
        self.birthday = None
        self.email = ""
        self.phoneNumber = ""
        self.membershipID = None
        self.loginDetails = ""
        self.recruitedBy = ""
    def registerationReq(self, TrainingRegistrationForm):
        pass
    def getPersonalProfileData(self, loginDetails):
        pass
    def setPersonalProfileData(self, loginDetails):
        pass
    def getMembershipPlan(self, membershipID):
        pass
    def setMembershipPlan(self, membershipID):
        pass
    def membershipCancellationRequestForm(self, MembershipCancellationRequestForm):
        pass
    def trainingCancellationRequestForm(self, TrainingCancellationRequestForm):
        pass

