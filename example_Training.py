from users.Trainer import Trainer
from main_services.Training import Training
from incomes.BrandedMerchandise import BrandedMerchandise
from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date
import time
from incomes.Payment import Payment


connector = DBConnector(server=socket.gethostname(), database='BLING_System')
connector.connect()
Training = Training(connector, 12, 'hit' , 20 , 50, 'hit training')
print("create")
time.sleep(30)
Training.set_trainingID(14)
print("set")
time.sleep(30)
Training.delete()
print("deleted")
connector.disconnect()



# (trainingID, trainingType, capacity, duration, trainingDescription )
