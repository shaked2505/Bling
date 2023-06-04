from app import db
import datetime

class MembershipCancellationRequestForm(db.Model):
    requestID = db.Column(db.Integer, primary_key=True)
    traineeID = db.Column(db.Integer, db.ForeignKey('trainee.traineeID'))
    trainee = db.relationship('Trainee', backref=db.backref('Trainee', uselist=False))
    membershipID = db.Column(db.Integer, db.ForeignKey('membership_plan.membershipID'))
    Membership_plan = db.relationship('MembershipPlan', backref=db.backref('Membership_plan', uselist=False))
    reason = db.Column(db.String)
    requestDate = db.Column(db.DateTime, default=datetime.now)
    approvalStatus = db.Column(db.String)

    # Create initializer/constructor
    def __init__(self, requestID, traineeID, membershipID, reason, approvalStatus):
        self.requestID = requestID
        self.traineeID = traineeID
        self.membershipID = membershipID
        self.reason = reason
        self.requestDate = datetime.date.today()
        self.approvalStatus = approvalStatus



    def getRequestDetails(self):
        return self.requestID
        

    def isPending(self):
        return self.approvalStatus


    def notificationEmailToSystemManager(self, systemManager):
        pass


