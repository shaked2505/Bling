from app import db

class MembershipPlan(db.Model):
    membershipID = db.Column(db.Integer, primary_key=True)
    membershipPlanDescription = db.Column(db.String)
    price = db.Column(db.Float)
    membershipPlanType = db.Column(db.String)

    # Create initializer/constructor
    def __init__(self, membershipID, membershipPlanType, membershipPlanDescription, price):
        self.membershipID = membershipID
        self.membershipPlanDescription = membershipPlanDescription
        self.price = price
        self.membershipPlanType = membershipPlanType
      

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
        db.session.commit()

    def updateDescription(self, membershipPlanDescription):
        self.membershipPlanDescription = membershipPlanDescription
        db.session.commit()

    def updateType(self, membershipPlanType):
        self.membershipPlanType = membershipPlanType
        db.session.commit()

    def getType(self):
        return self.membershipPlanType