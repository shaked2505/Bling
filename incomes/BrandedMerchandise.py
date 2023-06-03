from app import db

class BrandedMerchandise(db.Model):
    productID = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    unitInStock = db.Column(db.Integer)
    productName = db.Column(db.String)
    productDescription = db.Column(db.String)
    managerID = db.Column(db.Integer)
    paymentID = db.Column(db.Integer)

    # Create initializer/constructor
    def __init__(self, productID, price, unitInStock, productName, productDescription, managerID, paymentID):
        self.productID = productID
        self.price = price
        self.unitInStock = unitInStock
        self.productName = productName
        self.productDescription = productDescription
        self.managerID = managerID
        self.paymentID = paymentID
     
    def getPrice(self):
        return self.price
    
    def setPrice(self,new_price):
        self.price = new_price
        db.session.commit()  

    def getDescription(self):
        return self.productDescription
    
    def getUnitInStock(self):
        return self.unitInStock
