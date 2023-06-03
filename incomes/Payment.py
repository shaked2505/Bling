import datetime
from app import db


class Payment(db.Model):
    paymentID = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    dateOfPayment = db.Column(db.Date)
    paymentStatus = db.Column(db.String)
    traineeID = db.Column(db.Integer, db.ForeignKey('trainee.traineeID'))
    trainee = db.relationship('Trainee', backref=db.backref('trainee', uselist=False))
    membershipID =db.Column (db.Integer, db.ForeignKey('membership_plan.membershipID'))
    membership_plan = db.relationship('MembershipPlan', backref=db.backref('membership_plan', uselist=False))
    productID = db.Column(db.Integer, db.ForeignKey('branded_merchandise.productID'))
    branded_merchendise = db.relationship('BrandedMerchandise', backref=db.backref('branded_merchandise', uselist=False))


    def __init__(self,paymentID, amount, paymentStatus, customerID, membershipID, productID):
        self.paymentID = paymentID
        self.amount = amount
        self.dateOfPayment = datetime.date.today()
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







