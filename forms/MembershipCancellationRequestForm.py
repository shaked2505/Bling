import datetime

class MembershipCancellationRequestForm:
    def __init__(self, connector, requestID, memberID,planID,reason,approvalStatus):
        self.requestID = requestID
        self.memberID = memberID
        self.planID = planID
        self.reason = reason
        self.requestDate = datetime.date.today()
        self.approvalStatus = approvalStatus
        self.connector = connector


        sql= "INSERT INTO MembershipCancellationRequestForm (requestID, memberID, planID, reason, requestDate,approvalStatus ) VALUES (?, ?, ?, ?, ?, ?)"
        values = (self.requestID, self.memberID, self.planID,self.reason ,str(self.requestDate), self.approvalStatus)
        self.connector.execute_query(sql, values)

    def set_requestID(self, requestID):
        sql = "UPDATE MembershipCancellationRequestForm SET requestID=? WHERE requestID=?;"
        values = (requestID, self.requestID)
        self.connector.execute_query(sql, values)
        self.requestID = requestID

    def delete(self):
        sql = "DELETE FROM MembershipCancellationRequestForm WHERE requestID=?;"
        self.connector.execute_query(sql, self.requestID)


    def getRequestDetails(self, requestID):
        pass
    def isPending(self, requestID):
        pass
    def notificationEmailToSystemManager(self, systemManager):
        pass
