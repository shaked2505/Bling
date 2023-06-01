from users.Trainee import Trainee
from incomes.BrandedMerchandise import BrandedMerchandise
from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date
import time
from incomes.Payment import Payment

# connector = DBConnector(server=socket.gethostname(), database='BLING_System')
# connector.connect()
# Trainee = Trainee(connector, 123211, 'Dana Cohen' , '10-356-659384' , date(1990, 5, 22), 'shaked201098@gmail.com' ,'052-6265698', 4, 'DanaCohen1000', 'StudioMember: 1003')
# print("create")
# time.sleep(30)
# Trainee.set_traineeID(1010101)
# print("set")
# time.sleep(30)
# Trainee.delete()
# print("deleted")
# connector.disconnect()


# connector = DBConnector(server=socket.gethostname(), database='BLING_System')
# connector.connect()
# BrandedMerchandise = BrandedMerchandise(connector, 12134, 23.0 , 5544 , 'Shirt', 'beautiful' ,1111, 2000)
# print("create")
# time.sleep(30)
# BrandedMerchandise.set_productID(12134)
# print("set")
# time.sleep(30)
# BrandedMerchandise.delete()
# print("deleted")
# connector.disconnect()

connector = DBConnector(server=socket.gethostname(), database='BLING_System')
connector.connect()
Payment = Payment(connector, 2006, 23.0 , 'Approved', 1004 ,80, 300)
print("create")
time.sleep(10)
Payment.set_paymentID(2008)
print("set")
time.sleep(10)
Payment.delete()
print("deleted")
connector.disconnect()


