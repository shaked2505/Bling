class MembershipPlan:
    def __init__(self, connector, membershipID, membershipPlanDescription,price,membershipPlanType):
        self.membershipID = membershipID
        self.membershipPlanDescription = membershipPlanDescription
        self.price = price
        self.membershipPlanType = membershipPlanType
        self.connector=connector 


        sql= "INSERT INTO MembershipPlan (membershipID, membershipPlanDescription,price,membershipPlanType ) VALUES (?, ?, ?, ?)"
        values = (self.membershipID, self.membershipPlanDescription, self.price, self.membershipPlanType)
        self.connector.execute_query(sql, values)

    def set_membershipID(self, membershipID):
        sql = "UPDATE MembershipPlan SET membershipID=? WHERE membershipID=?;"
        values = (membershipID, self.membershipID)
        self.connector.execute_query(sql, values)
        self.membershipID = membershipID

    def delete(self):
        sql = "DELETE FROM MembershipPlan WHERE membershipID=?;"
        self.connector.execute_query(sql, self.membershipID)



    def getPrice(self):
        pass
    def setPrice(self, price):
        pass
    def updateDescription(self, membershipPlanDescription):
        pass
    def updateType(self, membershipPlanType):
        pass
    def getType(self):
        pass        
