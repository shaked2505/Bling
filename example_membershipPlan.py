from users.Trainee import Trainee
from incomes.BrandedMerchandise import BrandedMerchandise
from DBConnector.DBFunctions import DBConnector
import socket
from datetime import date
import time
from incomes.MembershipPlan import MembershipPlan


connector = DBConnector(server=socket.gethostname(), database='BLING_System')
connector.connect()
MembershipPlan = MembershipPlan(connector, 140, "Sbaba" , 300.00, "Year")
print("create")
time.sleep(10)
MembershipPlan.set_membershipID(150)
print("set")
time.sleep(10)
MembershipPlan.delete()
print("deleted")
connector.disconnect()


