class SystemManager:
    def __init__(self, connector, managerID, managerFullName, bankAccount, email, phoneNumber, loginDetails):
        self.connector = connector 
        self.managerID = managerID
        self.managerFullName = managerFullName
        self.bankAccount = bankAccount
        self.email = email
        self.phoneNumber = phoneNumber
        self.email= email
        self.phoneNumber = phoneNumber
        self.loginDetails = loginDetails

        sql = "INSERT INTO SystemManager (managerID, managerFullName, bankAccount, email, phoneNumber, loginDetails ) VALUES (?, ?, ?, ?, ?, ?)"
        values = (self.managerID, self.managerFullName, self.bankAccount, self.email, self.phoneNumber, self.loginDetails)
        self.connector.execute_query(sql, values)

    def set_managerID(self, managerID):
        sql = "UPDATE SystemManager SET managerID=? WHERE managerID=?;"
        values = (managerID, self.managerID)
        self.connector.execute_query(sql, values)
        self.managerID = managerID

    def delete(self):
        sql = "DELETE FROM SystemManager WHERE managerID=?;"
        self.connector.execute_query(sql, self.managerID)

    def getProducts(self, BrandedMerchandise):
        pass

    def setProducts(self, BrandedMerchandise):
        pass

    def addTrainer(self, Trainer):
        pass

    def removeTrainer(self, Trainer):
        pass

    def smPosting(self, loginDetails):
        pass



