from datetime import date, time
import socket
from DBFunctions import DBConnector




# Assuming you have already established a connection and created a cursor
# ...


connector = DBConnector(server=socket.gethostname(), database='bling')
connector.connect()



#-------training-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO training (trainingID, trainingType, capacity, duration, trainingDescription ) VALUES (?, ?, ?, ?, ?)"

# Define the values to be inserted
values = (1, 'Power',8, 60, "Functional training with weights and other instruments incorporates resistance exercises that mimic real-life movements to enhance overall strength, stability, and mobility.")
connector.execute_query(sql, values)
values = (2, 'Barre',10, 60, "Barre training is a low-impact workout that combines elements of ballet, Pilates, and yoga to improve flexibility, strength, and posture.")
connector.execute_query(sql, values)
values= (3, 'MatPilates' , 12 , 60 , " Mat Pilates training is a floor-based exercise method that focuses on core strength, flexibility, and body awareness through controlled movements and proper breathing techniques.")
connector.execute_query(sql, values)
values= (4,'ReformerPilates' , 6 , 60, " Reformer Pilates training is a form of exercise that utilizes a specialized machine called a reformer to enhance strength, flexibility, and body alignment through controlled movements and resistance.")
connector.execute_query(sql, values)
values= (5,'Hit' , 12 , 60, "HIIT workouts involve short bursts of intense exercises followed by periods of rest or low-intensity activity. These sessions are designed to improve cardiovascular fitness, burn calories, and boost metabolism.")
connector.execute_query(sql, values)


#-------system_manager-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO system_manager (managerID , managerFullName, bankAccount, email, phoneNumber,  loginDetails) VALUES (?, ?, ?, ?, ?, ?)"
 
# Define the values to be inserted
values = (1111, 'Bar Diamant',  '10-350-789543', 'bar154@gmail.com', '054-7895279', 'Bar Diamant1111')
connector.execute_query(sql, values)


#-------trainer-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO trainer (trainerID, trainerFullName, specialty, hireDate, bankAccount , email, phoneNumber, loginDetails, hourlyWage, managerID ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Define the values to be inserted
values = ( 55, 'Shay Levi', 'Barre', str(date(2021, 5, 22)), '10-154-850274', 'shaked201098@gmail.com' , '052- 5843564', 'ShayLevi55', '70.00', 1111)
connector.execute_query(sql, values)
values = ( 66, 'Miri Bar Lev', 'Power and MatPilates' , str(date(2022, 7, 18)), '12-294-972547', 'miri@gmail.com'  ,'052-8653908' , 'MiriBarLev66' , '65.00',1111 )
connector.execute_query(sql, values)
values= ( 77, 'Hadar Oz', 'MatPilates', str(date(2021, 10, 7)), '9-398-846298', 'shirelyakim2@gmail.com' , '050-8364980', 'HadarOz77', '60.00', 1111 )
connector.execute_query(sql, values)
values= ( 88, 'Bar Gur', 'ReformerPilates', str(date(2023, 2, 12)), '5-625-835298', 'bar@gmail.com', '052-6452989' , 'BarGur88', '80.00', 1111 )
connector.execute_query(sql, values)
values= ( 99, 'Noa Maor', 'Hit', str(date(2023, 2, 18)), '4-768-758940', 'noa@gmail.com', '052-7564839' , 'NoaMaor99', '70.00', 1111 )
connector.execute_query(sql, values)
 

 #-------membership_plan-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO membership_plan (membershipID, membershipPlanType, membershipPlanDescription, price) VALUES (?, ?, ?, ?)"
 
# Define the values to be inserted
values = ( 4," 4 monthly entries", " does not include reformer Pilates ", 260.0) 
connector.execute_query(sql, values)
values = (8 ," 8 monthly entries", " does not include reformer Pilates ", 480.0)
connector.execute_query(sql, values)
values= (12 ,"12 monthly entries", " does not include reformer Pilates ", 580.0)
connector.execute_query(sql, values)
values= (40," 4 monthly entries", " includes reformer Pilates ", 280.0)
connector.execute_query(sql, values)
values= (80," 8 monthly entries", " includes reformer Pilates ", 520.0)
connector.execute_query(sql, values)
values=(120," 12 monthly entries", " includes reformer Pilates ", 650.0)
connector.execute_query(sql, values)
values=(100," unlimited", " includes reformer Pilates ", 700.0)
connector.execute_query(sql, values)
values=(10," unlimited", " does not include reformer Pilates ", 650.0)
connector.execute_query(sql, values)
 
#-------trainee-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO trainee (traineeID, traineeFullName, bankAccount, birthday, email, phoneNumber, joiningDate, membershipID , loginDetails, recruitedBy ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
 
# Define the values to be inserted
values = (1000, 'Dana Cohen' , '10-356-659384' , str(date(1990, 5, 22)), 'shaked201098@gmail.com' ,'052-6265698', str(date(2020, 7, 20)), 4, 'DanaCohen1000', 'StudioMember: 1003') 
connector.execute_query(sql, values)
values = (1001, 'Yuval Zak', '9-564-254979',str(date(1996, 10, 20)), 'YuvalZa@colman.ac.il' , '052-7852490', str(date(2020, 8, 10)), 8, 'YuvalZak1001', 'Instagram' )
connector.execute_query(sql, values)
values= (1002, 'Orit Mizrahi' , '5-153-692478', str(date(2000, 12, 27)), 'nmizra7@gmail.com' , '050-7496820' , str(date(2021, 1, 6)), 12, 'OritMizrahi1002', 'Facebook')
connector.execute_query(sql, values)
values= (1003, 'Idit Solomon' , '8-239-967352' , str(date(2002, 8, 10)), 'Orsolomon24@gmail.com ' , '050-2459875' , str(date(2019, 6, 25)), 100, 'IditSolomon1003' , 'SystemManager')
connector.execute_query(sql, values)
values= (1004, 'Stav Shalom' , '10-367-768306',  str(date(1999, 1, 15)), 'shirelyakim2@gmail.com ' , '052-8753095' ,  str(date(2023, 12, 18)), 80, 'StavShalom1004', 'StudioMember: 1003' ) 
connector.execute_query(sql, values)
values= (1005, 'Sapir Levi' , '5-246-654328',  str(date(1998, 2, 30)), 'tzvika.tubis@gmail.com ' , '052-6543234' ,  str(date(2021, 6, 6)), 80, 'SapirLevi1005', 'StudioMember: 1002' ) 
connector.execute_query(sql, values)
values= (1006, 'Mor Hadad' , '6-764-190876',  str(date(1997, 10, 16)), 'mor@gmail.com ' , '054-8765320' ,  str(date(2020, 3, 30)), 4, 'MorHadad1006', 'Instagram' ) 
connector.execute_query(sql, values)
values= (1007, 'Amit Marchiano' , '8-898-358964',  str(date(1998, 3, 12)), 'amit@gmail.com ' , '054-6547890' ,  str(date(2021, 4, 5)), 100, 'AmitMarchiano1007', 'Facebook' ) 
connector.execute_query(sql, values)
values= (1008, 'Rona Segal' , '6-544-674832',  str(date(2000, 8, 17)), 'rona@gmail.com ' , '053-6578498' ,  str(date(2023, 5, 8)), 12, 'RonaSegal1008', 'StudioMember: 1001' ) 
connector.execute_query(sql, values)

  

#-------specific_time_training-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO specific_time_training (specificTimeTrainingDate , trainingID , startTime, endTime, standbyTrainer, trainerID ) VALUES (?, ?, ?, ?, ?, ?)"
 
# Define the values to be inserted
values = ( str(date(2023, 6, 4)), 1, str(time(16, 00)), str(time(17, 00)), 55, 66 ) 
connector.execute_query(sql, values)
values = ( str(date(2023, 6, 4)), 2, str(time(17, 00)), str(time(18, 00)), 66, 77 )
connector.execute_query(sql, values)
values= ( str(date(2023, 6, 4)), 3, str(time(18, 00)), str(time(19, 00)), 77, 55 )
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 4)), 4, str(time(19, 00)), str(time(20, 00)), 88, 66 ) 
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 4)), 5, str(time(20, 00)), str(time(21, 00)), 99, 88 ) 
connector.execute_query(sql, values)

values = ( str(date(2023, 6, 5)), 1, str(time(16, 00)), str(time(17, 00)), 99, 66 ) 
connector.execute_query(sql, values)
values = ( str(date(2023, 6, 5)), 4, str(time(17, 00)), str(time(18, 00)), 77, 88 )
connector.execute_query(sql, values)
values= ( str(date(2023, 6, 5)), 3, str(time(18, 00)), str(time(19, 00)), 55, 99 )
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 5)), 2, str(time(19, 00)), str(time(20, 00)), 88, 66 ) 
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 5)), 5, str(time(20, 00)), str(time(21, 00)), 66, 77 ) 
connector.execute_query(sql, values)

values = ( str(date(2023, 6, 6)), 3, str(time(16, 00)), str(time(17, 00)), 55, 99 ) 
connector.execute_query(sql, values)
values = ( str(date(2023, 6, 6)), 5, str(time(17, 00)), str(time(18, 00)), 88, 66 )
connector.execute_query(sql, values)
values= ( str(date(2023, 6, 6)), 2, str(time(18, 00)), str(time(19, 00)), 99, 88 )
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 6)), 1, str(time(19, 00)), str(time(20, 00)), 77, 66 ) 
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 6)), 4, str(time(20, 00)), str(time(21, 00)), 66, 55 ) 
connector.execute_query(sql, values)

values = ( str(date(2023, 6, 7)), 5, str(time(16, 00)), str(time(17, 00)), 66, 77 ) 
connector.execute_query(sql, values)
values = ( str(date(2023, 6, 7)), 2, str(time(17, 00)), str(time(18, 00)), 88, 99 )
connector.execute_query(sql, values)
values= ( str(date(2023, 6, 7)), 3, str(time(18, 00)), str(time(19, 00)), 99, 55 )
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 7)), 4, str(time(19, 00)), str(time(20, 00)), 77, 66 ) 
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 7)), 1, str(time(20, 00)), str(time(21, 00)), 55, 88 ) 
connector.execute_query(sql, values)

values = ( str(date(2023, 6, 8)), 3, str(time(16, 00)), str(time(17, 00)), 77, 99 ) 
connector.execute_query(sql, values)
values = ( str(date(2023, 6, 8)), 5, str(time(17, 00)), str(time(18, 00)), 88, 66 )
connector.execute_query(sql, values)
values= ( str(date(2023, 6, 8)), 2, str(time(18, 00)), str(time(19, 00)), 55, 88 )
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 8)), 1, str(time(19, 00)), str(time(20, 00)), 66, 55 ) 
connector.execute_query(sql, values)
values=  (str(date(2023, 6, 8)), 4, str(time(20, 00)), str(time(21, 00)), 99, 77 ) 
connector.execute_query(sql, values)

values = ( str(date(2023, 6, 9)), 2, str(time(8, 00)), str(time(9, 00)), 88, 99 ) 
connector.execute_query(sql, values)
values = ( str(date(2023, 6, 9)), 1, str(time(9, 00)), str(time(10, 00)), 77, 66 )
connector.execute_query(sql, values)
values= ( str(date(2023, 6, 9)), 5, str(time(10, 00)), str(time(11, 00)), 55, 88 )



#-------membership_cancellation_request_form-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO membership_cancellation_request_form (requestID, traineeID , membershipID , reason, requestDate, approvalStatus) VALUES (?, ?, ?, ?, ?, ?)"
 
# Define the values to be inserted
values = ( 11, 1001, 4, 'Too expensive' ,  str(date(2023, 4,12)), 'Declined' ) 
connector.execute_query(sql, values)
values = ( 12, 1002, 12, 'Arriving difficulties', str(date(2023, 4,28)), ' Declined' )
connector.execute_query(sql, values)
values= ( 13, 1004, 80, 'Schedule difficulties', str(date(2023, 4,15)), 'In Process' )
connector.execute_query(sql, values)




#-------training_registration_form-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO training_registration_form (registrationID, traineeID , trainingID , approvalStatus, SpecificTimeTrainingDate, requestDate) VALUES (?, ?, ?, ?, ?, ?)"
#Define the values to be inserted
values = ( 111, 1000, 1, 'Approved', str(date(2023, 5 ,20)), str(date(2023, 5 ,18)) ) 
connector.execute_query(sql, values)
values =( 112, 1001, 3, 'Approved', str(date(2023, 3, 3)), str(date(2023, 3, 1) ))
connector.execute_query(sql, values)
values= ( 113, 1003, 2, 'Approved', str(date(2023, 5, 10)), str(date(2023, 5, 8)))
connector.execute_query(sql, values)
values=( 114, 1004, 4, 'Approved', str(date(2023, 4, 12)), str(date(2023, 4, 10)) )
connector.execute_query(sql, values)
values= (115, 1002, 1, 'Approved', str(date(2023, 5, 20)) ,str(date(2023, 5, 18)) )
connector.execute_query(sql, values)

#-------training_cancellation_request_form-------
# Prepare the SQL INSERT statement

sql= "INSERT INTO training_cancellation_request_form (requestID, traineeID , reason, approvalStatus, specificTimeTrainingDate , trainingID, requestDate) VALUES (?, ?, ?, ?, ?, ?, ?)"
# Define the values to be inserted
values = ( 220, 1000, 'Timetable constraints ' , 'Approved', str(date(2023, 5,10)),2 ,str(date(2023, 5,9)) )  
connector.execute_query(sql, values)
values = ( 221, 1001, 'Health conditions' , 'Approved',  str(date(2023,5, 20)), 1 , str(date(2023,5, 19))) 
connector.execute_query(sql, values)
values= ( 222, 1000, 'Timetable constraints ' , 'Approved',  str(date(2023,5, 20)), 1 , str(date(2023,5, 19)))
connector.execute_query(sql, values)
values=( 223, 1004, 'Timetable constraints ' , 'Approved',  str(date(2023,5,20)), 1 ,str(date(2023,5,19)) )
connector.execute_query(sql, values)
values= (224, 1002, 'Health conditions' , 'Approved',  str(date(2023, 5, 10)), 2, str(date(2023, 5, 9)) )
connector.execute_query(sql, values)

#-------branded_merchandise-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO branded_merchandise (productID, price, unitInStock, productName, productDescription,managerID) VALUES (?, ?, ?, ?, ?, ?, ?)"

# Define the values to be inserted
values = ( 300, 50.00 , 20 ,'Water Bottle', 'Stainless steel bottle, contains 500 ml' ,1111, None,)
connector.execute_query(sql, values)
values = (301, 80.00, 15, 'Towel' , 'Personal training towel, embroidered logo on the front', 1111, None,)
connector.execute_query(sql, values)
values = (302, 70.00, 30, 'Bling Hat' , 'Designed hat made of 70% cotton fabric, embroidered logo on the front', 1111, None,)
connector.execute_query(sql, values)


# #-------payment-------
# Prepare the SQL INSERT statement
sql= "INSERT INTO payment (paymentID, amount, dateOfPayment, paymentStatus, traineeID, membershipID  , productID ) VALUES (?, ?, ?, ?, ?, ?, ? )"

# Define the values to be inserted
values = (2000, 480.0, str(date(2023, 5, 1)), 'Approved' , 1001, 8, None) 
connector.execute_query(sql, values)
values = (2001, 520.0, str(date(2022, 10, 1)) ,'Approved', 1004, 80, None) 
connector.execute_query(sql, values)
values = (2002, 50.0, str(date(2023, 4, 20)) , 'Approved', 1002, 12, 300)
connector.execute_query(sql, values)
values= (2003, 80.0, str(date(2023, 2, 20)) , 'Approved', 1001, 8, 301)
connector.execute_query(sql, values)
values=(2004, 700.0, str(date(2023, 3, 1)) , 'Approved', 1003, 100, None)
connector.execute_query(sql, values)
values=(2005, 700.0, str(date(2023, 3, 12)) , 'Approved', 1000, 4, None )
connector.execute_query(sql, values)

connector.disconnect

