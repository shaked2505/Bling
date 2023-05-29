import datetime

class Trainee:
    def __init__(self, connector, traineeID, traineeFullName, bankAccount, birthday, email, phoneNumber, membershipID, loginDetails, recruitedBy):
        self.traineeID = traineeID
        self.traineeFullName = traineeFullName
        self.bankAccount = bankAccount
        self.joiningDate = datetime.date.today()
        self.birthday = birthday
        self.email = email
        self.phoneNumber = phoneNumber
        self.membershipID = membershipID
        self.loginDetails = loginDetails
        self.recruitedBy = recruitedBy
        self.connector = connector
        sql= "INSERT INTO Trainee (traineeID, traineeFullName, bankAccount, birthday, email, phoneNumber, joiningDate, membershipID , loginDetails, recruitedBy ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (self.traineeID, self.traineeFullName, self.bankAccount, str(self.birthday), self.email, self.phoneNumber, str(self.joiningDate), self.membershipID , self.loginDetails, self.recruitedBy)
        self.connector.execute_query(sql, values)

    def set_traineeID(self, traineeID):
        sql = "UPDATE Trainee SET traineeID=? WHERE traineeID=?;"
        values = (traineeID, self.traineeID)
        self.connector.execute_query(sql, values)
        self.traineeID = traineeID

    def delete(self):
        sql = "DELETE FROM Trainee WHERE traineeID=?;"
        self.connector.execute_query(sql, self.traineeID)

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

