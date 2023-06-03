from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date, time
from main_services.SpecificTimeTraining import SpecificTimeTraining

connector = DBConnector(server=socket.gethostname(), database='BLING_System')
connector.connect()
SpecificTimeTraining = SpecificTimeTraining(connector, str(date(2023, 5, 25)), 1, str(time(9, 30)), str(time(10, 30)), 55, 66 ) 
print("create")
time.sleep(10)
#def set_specificTimeTrainingID()
#print("set")
#time.sleep(10)
#MembershipPlan.delete()
#print("deleted")
connector.disconnect()