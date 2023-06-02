from users.Trainer import Trainer
from incomes.BrandedMerchandise import BrandedMerchandise
from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date
import time
from forms.MembershipCancellationRequestForm import MembershipCancellationRequestForm

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
MembershipCancellationRequestForm = MembershipCancellationRequestForm(connector, 14, 1004 , 80, "Cancel" ,'Approved')
print("create")
time.sleep(10)
MembershipCancellationRequestForm.set_requestID(15)
print("set")
time.sleep(10)
MembershipCancellationRequestForm.delete()
print("deleted")
connector.disconnect()


# (requestID, memberID, planID, reason, requestDate,approvalStatus )


