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

def create_Trainer():
    db.session.add(Trainer(55, 'Shay Levi', 'Barre', str(date(2021, 5, 22)), '10-154-850274', 'shaked201098@gmail.com' , '052- 5843564', 'ShayLevi55', '70.00', 1111))
    db.session.add(Trainer(66, 'Miri Bar Lev', 'Power and MatPilates' , str(date(2022, 7, 18)), '12-294-972547', 'miri@gmail.com'  ,'052-8653908' , 'MiriBarLev66' , '65.00',1111 ))
    db.session.add(Trainer(77, 'Hadar Oz', 'MatPilates', str(date(2021, 10, 7)), '9-398-846298', 'shirelyakim2@gmail.com' , '050-8364980', 'HadarOz77', '60.00', 1111 ))
    db.session.add(Trainer(88, 'Bar Gur', 'ReformerPilates', str(date(2023, 2, 12)), '5-625-835298', 'bar@gmail.com', '052-6452989' , 'BarGur88', '80.00', 1111 ))
    db.session.add(Trainer(99, 'Noa Maor', 'Hit', str(date(2023, 2, 18)), '4-768-758940', 'noa@gmail.com', '052-7564839' , 'NoaMaor99', '70.00', 1111 ))
    db.session.commit()


def create_Trainings():
    db.session.add(Training('Power',8, 60, "Functional training with weights and other instruments incorporates resistance exercises that mimic real-life movements to enhance overall strength, stability, and mobility."))
    db.session.add(Training('Barre',10, 60, "Barre training is a low-impact workout that combines elements of ballet, Pilates, and yoga to improve flexibility, strength, and posture."))
    db.session.add(Training('MatPilates' , 12 , 60 , " Mat Pilates training is a floor-based exercise method that focuses on core strength, flexibility, and body awareness through controlled movements and proper breathing techniques."))
    db.session.add(Training('ReformerPilates' , 6 , 60, " Reformer Pilates training is a form of exercise that utilizes a specialized machine called a reformer to enhance strength, flexibility, and body alignment through controlled movements and resistance."))
    db.session.add(Training('Hit' , 12 , 60, "HIIT workouts involve short bursts of intense exercises followed by periods of rest or low-intensity activity. These sessions are designed to improve cardiovascular fitness, burn calories, and boost metabolism."))
    db.session.commit()

def create_SystemManager():
    db.session.add(SystemManager(1111, 'Bar Diamant',  '10-350-789543', 'bar154@gmail.com', '054-7895279', 'Bar Diamant1111'))
    db.session.commit()


def create_MembershipPlan():
    db.session.add(MembershipPlan(4," 4 monthly entries", " does not include reformer Pilates ", 260.0))
    db.session.add(MembershipPlan(8 ," 8 monthly entries", " does not include reformer Pilates ", 480.0))
    db.session.add(MembershipPlan(12 ,"12 monthly entries", " does not include reformer Pilates ", 580.0))
    db.session.add(MembershipPlan(40," 4 monthly entries", " includes reformer Pilates ", 280.0))
    db.session.add(MembershipPlan(80," 8 monthly entries", " includes reformer Pilates ", 520.0))
    db.session.add(MembershipPlan(120," 12 monthly entries", " includes reformer Pilates ", 650.0))
    db.session.add(MembershipPlan(100," unlimited", " includes reformer Pilates ", 700.0))
    db.session.add(MembershipPlan(10," unlimited", " does not include reformer Pilates ", 650.0))
    db.session.commit()



def create_Trainee():
    db.session.add(Trainee(1000, 'Dana Cohen' , '10-356-659384' , str(date(1990, 5, 22)), 'shaked201098@gmail.com' ,'052-6265698', str(date(2020, 7, 20)), 4, 'DanaCohen1000', 'StudioMember: 1003'))
    db.session.add(Trainee(1001, 'Yuval Zak', '9-564-254979',str(date(1996, 10, 20)), 'YuvalZa@colman.ac.il' , '052-7852490', str(date(2020, 8, 10)), 8, 'YuvalZak1001', 'Instagram' ))
    db.session.add(Trainee(1002, 'Orit Mizrahi' , '5-153-692478', str(date(2000, 12, 27)), 'nmizra7@gmail.com' , '050-7496820' , str(date(2021, 1, 6)), 12, 'OritMizrahi1002', 'Facebook'))
    db.session.add(Trainee(1003, 'Idit Solomon' , '8-239-967352' , str(date(2002, 8, 10)), 'Orsolomon24@gmail.com ' , '050-2459875' , str(date(2019, 6, 25)), 100, 'IditSolomon1003' , 'SystemManager'))
    db.session.add(Trainee(1004, 'Stav Shalom' , '10-367-768306',  str(date(1999, 1, 15)), 'shirelyakim2@gmail.com ' , '052-8753095' ,  str(date(2023, 12, 18)), 80, 'StavShalom1004', 'StudioMember: 1003' ))
    db.session.add(Trainee(1005, 'Sapir Levi' , '5-246-654328',  str(date(1998, 2, 30)), 'tzvika.tubis@gmail.com ' , '052-6543234' ,  str(date(2021, 6, 6)), 80, 'SapirLevi1005', 'StudioMember: 1002' ))
    db.session.add(Trainee(1006, 'Mor Hadad' , '6-764-190876',  str(date(1997, 10, 16)), 'mor@gmail.com ' , '054-8765320' ,  str(date(2020, 3, 30)), 4, 'MorHadad1006', 'Instagram' ))
    db.session.add(Trainee(1007, 'Amit Marchiano' , '8-898-358964',  str(date(1998, 3, 12)), 'amit@gmail.com ' , '054-6547890' ,  str(date(2021, 4, 5)), 100, 'AmitMarchiano1007', 'Facebook' ))
    db.session.add(Trainee(1008, 'Rona Segal' , '6-544-674832',  str(date(2000, 8, 17)), 'rona@gmail.com ' , '053-6578498' ,  str(date(2023, 5, 8)), 12, 'RonaSegal1008', 'StudioMember: 1001' ))
    db.session.commit()


def create_SpecificTimeTraining():
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 4)), 1, str(time(16, 00)), str(time(17, 00)), 55, 66))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 4)), 2, str(time(17, 00)), str(time(18, 00)), 66, 77))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 4)), 3, str(time(18, 00)), str(time(19, 00)), 77, 55))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 4)), 4, str(time(19, 00)), str(time(20, 00)), 88, 66)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 4)), 5, str(time(20, 00)), str(time(21, 00)), 99, 88)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 5)), 1, str(time(16, 00)), str(time(17, 00)), 99, 66)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 5)), 4, str(time(17, 00)), str(time(18, 00)), 77, 88))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 5)), 3, str(time(18, 00)), str(time(19, 00)), 55, 99))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 5)), 2, str(time(19, 00)), str(time(20, 00)), 88, 66)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 5)), 5, str(time(20, 00)), str(time(21, 00)), 66, 77)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 6)), 3, str(time(16, 00)), str(time(17, 00)), 55, 99)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 6)), 5, str(time(17, 00)), str(time(18, 00)), 88, 66))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 6)), 2, str(time(18, 00)), str(time(19, 00)), 99, 88))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 6)), 1, str(time(19, 00)), str(time(20, 00)), 77, 66)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 6)), 4, str(time(20, 00)), str(time(21, 00)), 66, 55)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 7)), 5, str(time(16, 00)), str(time(17, 00)), 66, 77)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 7)), 2, str(time(17, 00)), str(time(18, 00)), 88, 99))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 7)), 3, str(time(18, 00)), str(time(19, 00)), 99, 55))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 7)), 4, str(time(19, 00)), str(time(20, 00)), 77, 66)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 7)), 1, str(time(20, 00)), str(time(21, 00)), 55, 88)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 8)), 3, str(time(16, 00)), str(time(17, 00)), 77, 99)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 8)), 5, str(time(17, 00)), str(time(18, 00)), 88, 66))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 8)), 2, str(time(18, 00)), str(time(19, 00)), 55, 88))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 8)), 1, str(time(19, 00)), str(time(20, 00)), 66, 55)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 8)), 4, str(time(20, 00)), str(time(21, 00)), 99, 77)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 9)), 2, str(time(8, 00)), str(time(9, 00)), 88, 99)) 
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 9)), 1, str(time(9, 00)), str(time(10, 00)), 77, 66))
    db.session.add(SpecificTimeTraining(str(date(2023, 6, 9)), 5, str(time(10, 00)), str(time(11, 00)), 55, 88))
    db.session.commit()


def create_MembershipCancellationRequestForm():
    db.session.add(MembershipCancellationRequestForm(11, 1001, 4, 'Too expensive' ,  str(date(2023, 4,12)), 'Declined'))
    db.session.add(MembershipCancellationRequestForm(12, 1002, 12, 'Arriving difficulties', str(date(2023, 4,28)), ' Declined'))
    db.session.add(MembershipCancellationRequestForm(13, 1004, 80, 'Schedule difficulties', str(date(2023, 4,15)), 'In Process'))
    db.session.commit()

def create_TrainingRegistrationForm():
    db.session.add(TrainingCancellationRequestForm(111, 1000, 1, 'Approved', str(date(2023, 5 ,20)), str(date(2023, 5 ,18)))) 
    db.session.add(TrainingCancellationRequestForm(112, 1001, 3, 'Approved', str(date(2023, 3, 3)), str(date(2023, 3, 1))))
    db.session.add(TrainingCancellationRequestForm(113, 1003, 2, 'Approved', str(date(2023, 5, 10)), str(date(2023, 5, 8))))
    db.session.add(TrainingCancellationRequestForm(114, 1004, 4, 'Approved', str(date(2023, 4, 12)), str(date(2023, 4, 10))))
    db.session.add(TrainingCancellationRequestForm(115, 1002, 1, 'Approved', str(date(2023, 5, 20)) ,str(date(2023, 5, 18))))
    db.session.commit()

def create_TrainingCancellationRequestForm():
    db.session.add(TrainingCancellationRequestForm( 220, 1000, 'Timetable constraints ' , 'Approved', str(date(2023, 5,10)),2 ,str(date(2023, 5,9))))
    db.session.add(TrainingCancellationRequestForm( 221, 1001, 'Health conditions' , 'Approved',  str(date(2023,5, 20)), 1 , str(date(2023,5, 19)))) 
    db.session.add(TrainingCancellationRequestForm( 222, 1000, 'Timetable constraints ' , 'Approved',  str(date(2023,5, 20)), 1 , str(date(2023,5, 19)))) 
    db.session.add(TrainingCancellationRequestForm( 223, 1004, 'Timetable constraints ' , 'Approved',  str(date(2023,5,20)), 1 ,str(date(2023,5,19)))) 
    db.session.add(TrainingCancellationRequestForm(224, 1002, 'Health conditions' , 'Approved',  str(date(2023, 5, 10)), 2, str(date(2023, 5, 9))))  
    db.session.commit()


def create_BrandedMerchandise():
    db.session.add(BrandedMerchandise( 300, 50.00 , 20 ,'Water Bottle', 'Stainless steel bottle, contains 500 ml' ,1111))
    db.session.add(BrandedMerchandise(301, 80.00, 15, 'Towel' , 'Personal training towel, embroidered logo on the front', 1111,))
    db.session.add(BrandedMerchandise(302, 70.00, 30, 'Bling Hat' , 'Designed hat made of 70% cotton fabric, embroidered logo on the front', 1111))
    db.session.commit()


def create_Payment():
    db.session.add(Payment(2000, 480.0, str(date(2023, 5, 1)), 'Approved' , 1001, 8, None))
    db.session.add(Payment(2001, 520.0, str(date(2022, 10, 1)) ,'Approved', 1004, 80, None))
    db.session.add(Payment(2002, 50.0, str(date(2023, 4, 20)) , 'Approved', 1002, 12, 300))
    db.session.add(Payment(2003, 80.0, str(date(2023, 2, 20)) , 'Approved', 1001, 8, 301))
    db.session.add(Payment(2004, 700.0, str(date(2023, 3, 1)) , 'Approved', 1003, 100, None))
    db.session.add(Payment(2005, 700.0, str(date(2023, 3, 12)) , 'Approved', 1000, 4, None ))
    db.session.commit()

   





