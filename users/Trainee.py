from app import db

class Trainee:
    traineeID = db.Column(db.Integer, primary_key=True)
    traineeFullName = db.Column(db.String)
    bankAccount = db.Column(db.String)
    joiningDate = db.Column(db.Date)
    birthday = db.Column(db.Date)
    email = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.Integer, primary_key=True)
    membershipID = db.Column(db.Integer, primary_key=True)
    loginDetails = db.Column(db.Integer, primary_key=True)
    recruitedBy = db.Column(db.Integer, primary_key=True)

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
