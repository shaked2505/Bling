import datetime

class Payment:
    def __init__(self, connector,paymentID, amount, paymentStatus, customerID, membershipID, productID):
        self.paymentID = paymentID
        self.amount = amount
        self.dateOfPayment = datetime.date.today()
        self.paymentStatus = paymentStatus
        self.customerID = customerID
        self.membershipID = membershipID
        self.productID = productID
        self.connector = connector

        sql= "INSERT INTO Payment (PaymentID, amount,  dateOfPayment, paymentStatus, customerID, membershipID, productID ) VALUES (?, ?, ?, ?, ?, ?, ? )"
        values = (self.paymentID, self.amount, str(self.dateOfPayment), self.paymentStatus, self.customerID, self.membershipID, self.productID )
        self.connector.execute_query(sql, values)

    def set_paymentID(self, paymentID):
        sql = "UPDATE Payment SET paymentID=? WHERE paymentID=?;"
        values = (paymentID, self.paymentID)
        self.connector.execute_query(sql, values)
        self.paymentID = paymentID


    def delete(self):
        sql = "DELETE FROM Payment WHERE paymentID=?;"
        self.connector.execute_query(sql, self.paymentID)    

    def getAmount(self, amount):
        pass
    def getPaymentID(self, paymentID):
        pass
    def getCustomer(self, customerID):
        pass







