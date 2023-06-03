from users.Trainer import Trainer
from incomes.BrandedMerchandise import BrandedMerchandise
from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date
import time
from forms.TrainingCancellationRequestForm import TrainingCancellationRequestForm

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
TrainingCancellationRequestForm = TrainingCancellationRequestForm(connector, 225, 1004 , 1, date(2023,5,20) ,'Health conditions', 'Approved')
print("create")
time.sleep(10)
TrainingCancellationRequestForm.set_requestID(226)
print("set")
time.sleep(10)
TrainingCancellationRequestForm.delete()
print("deleted")
connector.disconnect()


# (requestID, memberID, trainingID, specificTimeTrainingDate, reason, approvalStatus,  requestDate)


