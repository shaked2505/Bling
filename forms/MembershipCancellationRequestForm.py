from app import db
import datetime

class MembershipCancellationRequestForm(db.Model):
    requestID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    traineeID = db.Column(db.String(9), db.ForeignKey('trainee.traineeID'))
    trainee = db.relationship('Trainee', foreign_keys=[traineeID])
    membershipID = db.Column(db.Integer, db.ForeignKey('membership_plan.membershipID'))
    Membership_plan = db.relationship('MembershipPlan', foreign_keys=[membershipID])
    reason = db.Column(db.String)
    requestDate = db.Column(db.Date)
    approvalStatus = db.Column(db.String)

    # Create initializer/constructor
    def __init__(self, traineeID, membershipID, reason, approvalStatus, requestDate=datetime.date.today()):
        self.traineeID = traineeID
        self.membershipID = membershipID
        self.reason = reason
        self.requestDate = requestDate
        self.approvalStatus = approvalStatus



    def getRequestDetails(self):
        return self.requestID
        

    def isPending(self):
        return self.approvalStatus


    def notificationEmailToSystemManager(self, systemManager):
        pass


