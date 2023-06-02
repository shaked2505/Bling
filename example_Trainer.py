from users.Trainer import Trainer
from users.Trainee import Trainee
from incomes.BrandedMerchandise import BrandedMerchandise
from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date
import time
from incomes.Payment import Payment


connector = DBConnector(server=socket.gethostname(), database='BLING_System')
connector.connect()
Trainer = Trainer(connector, 99,'Noa Noy' , 'power hit',  '123457', 'noa@gmail.com', '052-3333332','NoaNoy1234', 34.0 ,1111)
print("create")
time.sleep(10)
Trainer.set_trainerID(999)
print("set")
time.sleep(10)
Trainer.delete()
print("deleted")
connector.disconnect()


# (trainerID, trainerFullName, specialty, hireDate, bankAccount, email, phoneNumber, loginDetails, hourlyWage, managerID)
