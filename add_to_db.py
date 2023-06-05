from app import db, application
from users.Trainer import Trainer
from users.Trainee import Trainee
from users.SystemManager import SystemManager
from incomes.BrandedMerchandise import BrandedMerchandise
from incomes.MembershipPlan import MembershipPlan
from incomes.Payment import Payment
from main_services.Training import Training
from main_services.SpecificTimeTraining import SpecificTimeTraining
from datetime import datetime,timedelta, date, time
from forms.MembershipCancellationRequestForm import MembershipCancellationRequestForm
from forms.TrainingCancellationRequestForm import TrainingCancellationRequestForm
from forms.TrainingRegistrationForm import TrainingRegistrationForm

def write_to_db(object):
    try:
        db.session.add(object)
        db.session.commit()
    except Exception as e:
        if "Cannot insert duplicate key in object" in str(e):
            print("Duplicate key probably ID already inserted")
        else:
            raise e

def create_Trainer():
    write_to_db(Trainer(55, 'Shay Levi', 'Barre', str(date(2021, 5, 22)), '10-154-850274', 'shaked201098@gmail.com' , '052- 5843564', 'ShayLevi55', '70.00', 1111))
    write_to_db(Trainer(66, 'Miri Bar Lev', 'Power and MatPilates' , str(date(2022, 7, 18)), '12-294-972547', 'miri@gmail.com'  ,'052-8653908' , 'MiriBarLev66' , '65.00',1111 ))
    write_to_db(Trainer(77, 'Hadar Oz', 'MatPilates', str(date(2021, 10, 7)), '9-398-846298', 'shirelyakim2@gmail.com' , '050-8364980', 'HadarOz77', '60.00', 1111 ))
    write_to_db(Trainer(88, 'Bar Gur', 'ReformerPilates', str(date(2023, 2, 12)), '5-625-835298', 'bar@gmail.com', '052-6452989' , 'BarGur88', '80.00', 1111 ))

def create_Trainings():
    write_to_db(Training(1, 'Power',8, 60, "Functional training with weights and other instruments incorporates resistance exercises that mimic real-life movements to enhance overall strength, stability, and mobility."))
    write_to_db(Training(2, 'Barre',10, 60, "Barre training is a low-impact workout that combines elements of ballet, Pilates, and yoga to improve flexibility, strength, and posture."))
    write_to_db(Training(3, 'MatPilates' , 12 , 60 , " Mat Pilates training is a floor-based exercise method that focuses on core strength, flexibility, and body awareness through controlled movements and proper breathing techniques."))
    write_to_db(Training(4,'ReformerPilates' , 6 , 60, " Reformer Pilates training is a form of exercise that utilizes a specialized machine called a reformer to enhance strength, flexibility, and body alignment through controlled movements and resistance."))
    
def create_SystemManager():
    write_to_db(SystemManager(1111, 'Bar Diamant',  '10-350-789543', 'bar154@gmail.com', '054-7895279', 'Bar Diamant1111'))

def create_MembershipPlan():
    write_to_db(MembershipPlan(4," 4 monthly entries", " does not include reformer Pilates ", 260.0))
    write_to_db(MembershipPlan(8 ," 8 monthly entries", " does not include reformer Pilates ", 480.0))
    write_to_db(MembershipPlan(12 ,"12 monthly entries", " does not include reformer Pilates ", 580.0))
    write_to_db(MembershipPlan(40," 4 monthly entries", " includes reformer Pilates ", 280.0))
    write_to_db(MembershipPlan(80," 8 monthly entries", " includes reformer Pilates ", 520.0))
    write_to_db(MembershipPlan(120,"12 monthly entries", " includes reformer Pilates ", 650.0))
    write_to_db(MembershipPlan(100,"unlimited", " includes reformer Pilates ", 700.0))
    write_to_db(MembershipPlan(10,"unlimited", " does not include reformer Pilates ", 650.0))
    
def create_Trainee():
    write_to_db(Trainee(1000, 'Dana Cohen' , '10-356-659384' , str(date(1990, 5, 22)), 'shaked201098@gmail.com' ,'052-6265698', 4, 'DanaCohen1000', 'StudioMember: 1003', str(date(2020, 7, 20))))
    write_to_db(Trainee(1001, 'Yuval Zak', '9-564-254979',str(date(1996, 10, 20)), 'YuvalZa@colman.ac.il' , '052-7852490', 8, 'YuvalZak1001', 'Instagram', str(date(2020, 8, 10))))
    write_to_db(Trainee(1002, 'Orit Mizrahi' , '5-153-692478', str(date(2000, 12, 27)), 'nmizra7@gmail.com' , '050-7496820', 12, 'OritMizrahi1002', 'Facebook',str(date(2021, 1, 6))))
    write_to_db(Trainee(1003, 'Idit Solomon' , '8-239-967352' , str(date(2002, 8, 10)), 'Orsolomon24@gmail.com ' , '050-2459875' , 100, 'IditSolomon1003' , 'SystemManager', str(date(2019, 6, 25))))
    write_to_db(Trainee(1004, 'Stav Shalom' , '10-367-768306',  str(date(1999, 1, 15)), 'shirelyakim2@gmail.com ' , '052-8753095', 80, 'StavShalom1004', 'StudioMember: 1003', str(date(2023, 12, 18))))
    write_to_db(Trainee(1005, 'Sapir Levi' , '5-246-654328',  str(date(1998, 4, 30)), 'tzvika.tubis@gmail.com ' , '052-6543234' , 80, 'SapirLevi1005', 'StudioMember: 1002', str(date(2021, 6, 6))))
    write_to_db(Trainee(1006, 'Mor Hadad' , '6-764-190876',  str(date(1997, 10, 16)), 'mor@gmail.com ' , '054-8765320', 4, 'MorHadad1006', 'Instagram', str(date(2020, 3, 30)) ))
    write_to_db(Trainee(1007, 'Amit Marchiano' , '8-898-358964',  str(date(1998, 3, 12)), 'amit@gmail.com ' , '054-6547890' , 100, 'AmitMarchiano1007', 'Facebook', str(date(2021, 4, 5)),))
    write_to_db(Trainee(1008, 'Rona Segal' , '6-544-674832',  str(date(2000, 8, 17)), 'rona@gmail.com ' , '053-6578498' , 12, 'RonaSegal1008', 'StudioMember: 1001', str(date(2023, 5, 8)) ))
    
def create_SpecificTimeTraining():
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 1, str(time(16, 00)), str(time(17, 00)), 55, 66))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 2, str(time(17, 00)), str(time(18, 00)), 66, 77))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 3, str(time(18, 00)), str(time(19, 00)), 77, 55))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 4, str(time(19, 00)), str(time(20, 00)), 88, 66)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 1, str(time(16, 00)), str(time(17, 00)), 88, 66))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 2, str(time(19, 00)), str(time(20, 00)), 88, 66))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 3, str(time(18, 00)), str(time(19, 00)), 55, 88)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 4, str(time(17, 00)), str(time(18, 00)), 77, 88))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 1, str(time(19, 00)), str(time(20, 00)), 77, 66))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 2, str(time(18, 00)), str(time(19, 00)), 77, 88))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 3, str(time(16, 00)), str(time(17, 00)), 55, 66)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 4, str(time(20, 00)), str(time(21, 00)), 66, 55)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 1, str(time(16, 00)), str(time(17, 00)), 66, 77)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 2, str(time(17, 00)), str(time(18, 00)), 88, 77))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 3, str(time(18, 00)), str(time(19, 00)), 66, 55))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 4, str(time(19, 00)), str(time(20, 00)), 77, 66))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 1, str(time(19, 00)), str(time(20, 00)), 66, 55)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 2, str(time(16, 00)), str(time(17, 00)), 77, 88)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 3, str(time(17, 00)), str(time(18, 00)), 88, 66))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 4, str(time(20, 00)), str(time(21, 00)), 88, 77))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 9)), 1, str(time(9, 00)), str(time(10, 00)), 77, 66)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 9)), 2, str(time(8, 00)), str(time(9, 00)), 88, 55)) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 9)), 3, str(time(10, 00)), str(time(11, 00)), 55, 88))

def create_MembershipCancellationRequestForm():
    write_to_db(MembershipCancellationRequestForm(11, 1001, 4, 'Too expensive' ,  str(date(2023, 4,12)), 'Declined'))
    write_to_db(MembershipCancellationRequestForm(12, 1002, 12, 'Arriving difficulties', str(date(2023, 4,28)), ' Declined'))
    write_to_db(MembershipCancellationRequestForm(13, 1004, 80, 'Schedule difficulties', str(date(2023, 4,15)), 'In Process'))

def create_TrainingRegistrationForm():
    write_to_db(TrainingRegistrationForm(111, 1000, 1, 'Approved', str(date(2023, 6 ,4)), str(date(2023, 5 ,18)))) 
    write_to_db(TrainingRegistrationForm(112, 1001, 3, 'Approved', str(date(2023, 6, 5)), str(date(2023, 3, 1))))
    write_to_db(TrainingRegistrationForm(113, 1003, 2, 'Approved', str(date(2023, 6, 6)), str(date(2023, 5, 8))))
    write_to_db(TrainingRegistrationForm(114, 1004, 4, 'Approved', str(date(2023, 6, 4)), str(date(2023, 4, 10))))
    write_to_db(TrainingRegistrationForm(115, 1002, 1, 'Approved', str(date(2023, 6, 8)) ,str(date(2023, 5, 18))))

def create_TrainingCancellationRequestForm():
    write_to_db(TrainingCancellationRequestForm( 220, 1000, 'Timetable constraints ' , 'Approved', str(date(2023, 6,8)),2 ,str(date(2023, 5,9))))
    write_to_db(TrainingCancellationRequestForm( 221, 1001, 'Health conditions' , 'Approved',  str(date(2023,6, 4)), 1 , str(date(2023,5, 19)))) 
    write_to_db(TrainingCancellationRequestForm( 222, 1000, 'Timetable constraints ' , 'Approved',  str(date(2023,6, 5)), 1 , str(date(2023,5, 19)))) 
    write_to_db(TrainingCancellationRequestForm( 223, 1004, 'Timetable constraints ' , 'Approved',  str(date(2023,6,4)), 1 ,str(date(2023,5,19)))) 
    write_to_db(TrainingCancellationRequestForm(224, 1002, 'Health conditions' , 'Approved',  str(date(2023, 6, 7)), 2, str(date(2023, 5, 9))))  

def create_BrandedMerchandise():
    write_to_db(BrandedMerchandise( 300, 50.00 , 20 ,'Water Bottle', 'Stainless steel bottle, contains 500 ml' ,1111))
    write_to_db(BrandedMerchandise(301, 80.00, 15, 'Towel' , 'Personal training towel, embroidered logo on the front', 1111))
    write_to_db(BrandedMerchandise(302, 70.00, 30, 'Bling Hat' , 'Designed hat made of 70% cotton fabric, embroidered logo on the front', 1111))

def create_Payment():
    write_to_db(Payment(2000, 480.0, 'Approved' , 1001, 8, None, str(date(2023, 5, 1)),))   
    write_to_db(Payment(2001, 520.0, 'Approved', 1004, 80, None, str(date(2022, 10, 1))))
    write_to_db(Payment(2002, 50.0, 'Approved', 1002, 12, 300, str(date(2023, 4, 20)) ))
    write_to_db(Payment(2003, 80.0, 'Approved', 1001, 8, 301, str(date(2023, 2, 20)) ))
    write_to_db(Payment(2004, 700.0, 'Approved', 1003, 100, None, str(date(2023, 3, 1))))
    write_to_db(Payment(2005, 700.0, 'Approved', 1000, 4, None , str(date(2023, 3, 12))))
