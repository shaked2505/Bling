class Trainer:
    def __init__(self, trainerID, trainerFullName, specialty, hireDate, bankAccount, email, phoneNumber, loginDetails, hourlyWage, managerID):
        self.trainerID = trainerID
        self.trainerFullName = trainerFullName
        self.specialty = specialty
        self.hireDate = hireDate
        self.bankAccount = bankAccount
        self.email = email
        self.phoneNumber = phoneNumber
        self.loginDetails = loginDetails
        self.hourlyWage = hourlyWage
        self.managerID = managerID

    def shiftAssignment(self, Training):
        pass
    def changeShift(self, Training):
        pass
    def getHourlyWageViewing(self, hourlyWage):
        pass
    def standByAssignment(self, Training):
        pass
    def workAvailability(self, loginDetails):
        pass

