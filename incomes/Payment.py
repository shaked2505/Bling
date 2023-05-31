class Payment:
  def __init__(self, paymentID, amount, dateOfPayment, paymentStatus, customerID, membershipID, productID):
        self.paymentID = paymentID
        self.amount = amount
        self.dateOfPayment = dateOfPayment
        self.paymentStatus = paymentStatus
        self.customerID = customerID
        self.membershipID = membershipID
        self.productID = productID

  def getAmount(self, amount):
        pass
  def getPaymentID(self, paymentID):
        pass
  def getCustomer(self, customerID):
        pass

