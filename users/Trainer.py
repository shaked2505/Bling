from app import db

class Trainer(db.Model):
    trainerID = db.Column(db.Integer, primary_key=True)
    trainerFullName = db.Column(db.String)
    specialty = db.Column(db.String)
    hireDate = db.Column(db.Date)
    bankAccount = db.Column(db.String)
    email = db.Column(db.String)
    phoneNumber = db.Column(db.String)
    loginDetails = db.Column(db.String)
    hourlyWage = db.Column(db.Float)
    managerID = db.Column(db.Integer, db.ForeignKey('system_manager.managerID'))
    system_manager = db.relationship('SystemManager', backref=db.backref('system_manager', uselist=False))

    # Create initializer/constructor
    def __init__(self, trainerID, trainerFullName, specialty, hireDate, bankAccount, email, phoneNumber, loginDetails, hourlyWage, managerID):
        self.trainerID = trainerID
        self.trainerFullName = trainerFullName
        self.specialty = specialty
        self.hireDate = hireDate
        self.bankAccount = bankAccount
        self.email = email
        self.phoneNumber = phoneNumber
        self.loginDetails = loginDetails
        self.hourlyWage = hourlyWage
        self.managerID = managerID
