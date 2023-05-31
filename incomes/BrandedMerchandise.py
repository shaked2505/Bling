class BrandedMerchandise:
    def __init__(self, connector,productID, price, unitInStock, productName, productDescription, managerID, paymentID ):
        self.productID = productID  
        self.price = price  
        self.unitInStock = unitInStock  
        self.productName = productName  
        self.productDescription = productDescription 
        self.managerID = managerID  
        self.paymentID = paymentID  
        self.connector = connector



        sql= "INSERT INTO BrandedMerchandise ( productID, price, unitInStock, productName, productDescription,managerID,paymentID ) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (self.productID, self.price, self.unitInStock, self.productName, self.productDescription, self.managerID, self.paymentID )
        self.connector.execute_query(sql, values)

    def set_productID(self, productID):
        sql = "UPDATE BrandedMerchandise SET productID=? WHERE productID=?;"
        values = (productID, self.productID)
        self.connector.execute_query(sql, values)
        self.productID = productID
        self.connector.execute_query(sql, values)

    def delete(self):
        sql = "DELETE FROM BrandedMerchandise WHERE productID=?;"
        self.connector.execute_query(sql, self.productID)
        self.connector.execute_query(sql, self.productID)



    def getPrice(self):
        pass
    def setPrice(self, price):
        pass
    def getDescription(self):
        pass  
    def getUnitInStock(self):
        pass
