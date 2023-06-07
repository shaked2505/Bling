from app import db
from flask_login import UserMixin

class SystemManager(UserMixin, db.Model):
    __tablename__ = 'system_manager'
    managerID = db.Column(db.String(9), primary_key=True)
    managerFullName = db.Column(db.String)
    bankAccount = db.Column(db.String)
    email = db.Column(db.String)
    phoneNumber = db.Column(db.String)
    loginDetails = db.Column(db.String)

    # Create initializer/constructor
    def __init__(self, managerID, managerFullName, bankAccount, email, phoneNumber, loginDetails):
        self.managerID = managerID
        self.managerFullName = managerFullName
        self.bankAccount = bankAccount
        self.email = email
        self.phoneNumber = phoneNumber
        self.loginDetails = loginDetails

    def get_id(self):
        return self.managerID
# class SystemManager:
#     def __init__(self):
#         self.managerID = 0
#         self.managerFullName = "" 
#         self.bankAccount = ""
#         self.email = ""
#         self.phoneNumber = ""
#         self.loginDetails = ""

#     def getProducts(self, BrandedMerchandise):
#         pass

#     def setProducts(self, BrandedMerchandise):
#         pass

#     def addTrainer(self, Trainer):
#         pass

#     def removeTrainer(self, Trainer):
#         pass

#     def smPosting(self, loginDetails):
#         pass

