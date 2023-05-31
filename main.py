from users.Trainer import Trainer
from users.Trainee import Trainee
from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date
import time

connector = DBConnector(server=socket.gethostname(), database='BLING_System')
connector.connect()
#Trainee = Trainee(connector, 123211, 'Dana Cohen' , '10-356-659384' , date(1990, 5, 22), 'shaked201098@gmail.com' ,'052-6265698', 4, 'DanaCohen1000', 'StudioMember: 1003')
#print("create")
#time.sleep(30)
#Trainee.set_traineeID(1010101)
#print("set")
#time.sleep(30)
#Trainee.delete()
#print("deleted")
#connector.disconnect()
Trainer = Trainer (connector, 12345, 'Shay Levi', 'Barre', '10-154-850274', 'shaked201098@gmail.com' , '052- 5843564', 'ShayLevi55', '70.00', 1111)
print("create")
time.sleep(30)
Trainer.set_trainerID(1010101)
print("set")
time.sleep(30)
Trainee.delete()
print("deleted")
connector.disconnect()

