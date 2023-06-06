from app import db

class BrandedMerchandise(db.Model):
    productID = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    unitInStock = db.Column(db.Integer)
    productName = db.Column(db.String)
    productDescription = db.Column(db.String)
    managerID = db.Column(db.String(9), db.ForeignKey('system_manager.managerID'))
    system_manager = db.relationship('SystemManager', foreign_keys=[managerID])

    # Create initializer/constructor
    def __init__(self, productID, price, unitInStock, productName, productDescription, managerID):
        self.productID = productID
        self.price = price
        self.unitInStock = unitInStock
        self.productName = productName
        self.productDescription = productDescription
        self.managerID = managerID
     
    def getPrice(self):
        return self.price
    
    def setPrice(self,new_price):
        self.price = new_price
        db.session.commit()  

    def getDescription(self):
        return self.productDescription
    
    def getUnitInStock(self):
        return self.unitInStock
