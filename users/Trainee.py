from app import db
import datetime

class Trainee(db.Model):
    traineeID = db.Column(db.Integer, primary_key=True)
    traineeFullName = db.Column(db.String)
    bankAccount = db.Column(db.String)
    joiningDate = db.Column(db.Date)
    birthday = db.Column(db.Date)
    email = db.Column(db.String)
    phoneNumber = db.Column(db.String)
    membershipID =db.Column (db.Integer, db.ForeignKey('membership_plan.membershipID'))
    membership_plan = db.relationship('MembershipPlan', foreign_keys=[membershipID])
    loginDetails = db.Column(db.String)
    recruitedBy = db.Column(db.String)

    def __init__(self, traineeID, traineeFullName, bankAccount, birthday, email, phoneNumber, membershipID, loginDetails, recruitedBy):
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
