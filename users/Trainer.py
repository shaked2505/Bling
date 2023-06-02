import datetime

class Trainer:
    def __init__(self, connector, trainerID, trainerFullName, specialty, bankAccount, email, phoneNumber, loginDetails, hourlyWage, managerID):
        self.trainerID = trainerID
        self.trainerFullName = trainerFullName
        self.specialty = specialty
        self.hireDate = datetime.date.today()
        self.bankAccount = bankAccount
        self.email = email
        self.phoneNumber = phoneNumber
        self.loginDetails = loginDetails
        self.hourlyWage = hourlyWage
        self.managerID = managerID
        self.connector= connector
        sql= "INSERT INTO Trainer  (trainerID, trainerFullName, specialty, hireDate, bankAccount, email, phoneNumber, loginDetails, hourlyWage, managerID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (self.trainerID, self.trainerFullName, self.specialty, str(self.hireDate), self.bankAccount, self.email, self.phoneNumber , self.loginDetails, self.hourlyWage, self.managerID )
        self.connector.execute_query(sql, values)

    def set_trainerID(self, trainerID):
        sql = "UPDATE Trainer SET trainerID=? WHERE trainerID=?;"
        values = (trainerID, self.trainerID)
        self.connector.execute_query(sql, values)
        self.trainerID = trainerID

    def delete(self):
        sql = "DELETE FROM Trainer WHERE trainerID=?;"
        self.connector.execute_query(sql, self.trainerID)


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

