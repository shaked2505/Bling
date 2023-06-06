import datetime
from app import db


class Payment(db.Model):
    paymentID = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    dateOfPayment = db.Column(db.Date)
    paymentStatus = db.Column(db.String)
    traineeID = db.Column(db.String(9), db.ForeignKey('trainee.traineeID'))
    trainee = db.relationship('Trainee', foreign_keys=[traineeID])
    membershipID =db.Column (db.Integer, db.ForeignKey('membership_plan.membershipID'))
    membership_plan = db.relationship('MembershipPlan', foreign_keys=[membershipID])
    productID = db.Column(db.Integer, db.ForeignKey('branded_merchandise.productID'))
    branded_merchendise = db.relationship('BrandedMerchandise', foreign_keys=[productID])


    def __init__(self,paymentID, amount, paymentStatus, traineeID, membershipID, productID, dateOfPayment=datetime.date.today()):
        self.paymentID = paymentID
        self.amount = amount
        self.dateOfPayment = dateOfPayment
        self.paymentStatus = paymentStatus
        self.traineeID = traineeID
        self.membershipID = membershipID
        self.productID = productID
           
    def getAmount(self, amount):
        pass
    def getPaymentID(self, paymentID):
        pass
    def getCustomer(self, customerID):
        pass







