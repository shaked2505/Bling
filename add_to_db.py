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
    write_to_db(Trainer("550000000", 'Shay Levi', 'Barre', str(date(2021, 5, 22)), '10-154-850274', 'shaked201098@gmail.com' , '052- 5843564', 'ShayLevi55', '70.00', "111100000"))
    write_to_db(Trainer("660000000", 'Miri Bar Lev', 'Power and MatPilates' , str(date(2022, 7, 18)), '12-294-972547', 'miri@gmail.com'  ,'052-8653908' , 'MiriBarLev66' , '65.00',"111100000" ))
    write_to_db(Trainer("770000000", 'Hadar Oz', 'MatPilates', str(date(2021, 10, 7)), '9-398-846298', 'shirelyakim2@gmail.com' , '050-8364980', 'HadarOz77', '60.00', "111100000" ))
    write_to_db(Trainer("880000000", 'Bar Gur', 'ReformerPilates', str(date(2023, 2, 12)), '5-625-835298', 'bar@gmail.com', '052-6452989' , 'BarGur88', '80.00', "111100000" ))

def create_Trainings():
    write_to_db(Training(1, 'Power',8, 60, "Functional training with weights and other instruments incorporates resistance exercises that mimic real-life movements to enhance overall strength, stability, and mobility."))
    write_to_db(Training(2, 'Barre',10, 60, "Barre training is a low-impact workout that combines elements of ballet, Pilates, and yoga to improve flexibility, strength, and posture."))
    write_to_db(Training(3, 'MatPilates' , 12 , 60 , " Mat Pilates training is a floor-based exercise method that focuses on core strength, flexibility, and body awareness through controlled movements and proper breathing techniques."))
    write_to_db(Training(4,'ReformerPilates' , 6 , 60, " Reformer Pilates training is a form of exercise that utilizes a specialized machine called a reformer to enhance strength, flexibility, and body alignment through controlled movements and resistance."))
    
def create_SystemManager():
    write_to_db(SystemManager("111100000",'Bar Diamant',  '10-350-789543', 'bar154@gmail.com', '054-7895279', 'Bar Diamant1111'))

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
    write_to_db(Trainee("100000000", 'Dana Cohen' , '10-356-659384' , str(date(1990, 5, 22)), 'shaked201098@gmail.com' ,'052-6265698', 4, 'DanaCohen1000', 'StudioMember: 1003', str(date(2020, 7, 20))))
    write_to_db(Trainee("100100000", 'Yuval Zak', '9-564-254979',str(date(1996, 10, 20)), 'YuvalZa@colman.ac.il' , '052-7852490', 8, 'YuvalZak1001', 'Instagram', str(date(2020, 8, 10))))
    write_to_db(Trainee("100200000", 'Orit Mizrahi' , '5-153-692478', str(date(2000, 12, 27)), 'nmizra7@gmail.com' , '050-7496820', 12, 'OritMizrahi1002', 'Facebook',str(date(2021, 1, 6))))
    write_to_db(Trainee("100300000", 'Idit Solomon' , '8-239-967352' , str(date(2002, 8, 10)), 'Orsolomon24@gmail.com ' , '050-2459875' , 100, 'IditSolomon1003' , 'SystemManager', str(date(2019, 6, 25))))
    write_to_db(Trainee("100400000", 'Stav Shalom' , '10-367-768306',  str(date(1999, 1, 15)), 'shirelyakim2@gmail.com ' , '052-8753095', 80, 'StavShalom1004', 'StudioMember: 1003', str(date(2023, 12, 18))))
    write_to_db(Trainee("100500000", 'Sapir Levi' , '5-246-654328',  str(date(1998, 4, 30)), 'tzvika.tubis@gmail.com ' , '052-6543234' , 80, 'SapirLevi1005', 'StudioMember: 1002', str(date(2021, 6, 6))))
    write_to_db(Trainee("100600000", 'Mor Hadad' , '6-764-190876',  str(date(1997, 10, 16)), 'mor@gmail.com ' , '054-8765320', 4, 'MorHadad1006', 'Instagram', str(date(2020, 3, 30)) ))
    write_to_db(Trainee("100700000", 'Amit Marchiano' , '8-898-358964',  str(date(1998, 3, 12)), 'amit@gmail.com ' , '054-6547890' , 100, 'AmitMarchiano1007', 'Facebook', str(date(2021, 4, 5)),))
    write_to_db(Trainee("100800000", 'Rona Segal' , '6-544-674832',  str(date(2000, 8, 17)), 'rona@gmail.com ' , '053-6578498' , 12, 'RonaSegal1008', 'StudioMember: 1001', str(date(2023, 5, 8)) ))
    
def create_SpecificTimeTraining():
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 1, str(time(16, 00)), str(time(17, 00)), "550000000", "660000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 2, str(time(17, 00)), str(time(18, 00)), "660000000", "770000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 3, str(time(18, 00)), str(time(19, 00)), "770000000", "550000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 4)), 4, str(time(19, 00)), str(time(20, 00)), "880000000", "660000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 1, str(time(16, 00)), str(time(17, 00)), "880000000", "660000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 2, str(time(19, 00)), str(time(20, 00)), "880000000", "660000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 3, str(time(18, 00)), str(time(19, 00)), "550000000", "880000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 5)), 4, str(time(17, 00)), str(time(18, 00)), "770000000", "880000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 1, str(time(19, 00)), str(time(20, 00)), "770000000", "660000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 2, str(time(18, 00)), str(time(19, 00)), "770000000", "880000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 3, str(time(16, 00)), str(time(17, 00)), "550000000", "660000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 6)), 4, str(time(20, 00)), str(time(21, 00)), "660000000", "550000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 1, str(time(16, 00)), str(time(17, 00)), "660000000", "770000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 2, str(time(17, 00)), str(time(18, 00)), "880000000", "770000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 3, str(time(18, 00)), str(time(19, 00)), "660000000", "550000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 7)), 4, str(time(19, 00)), str(time(20, 00)), "770000000", "660000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 1, str(time(19, 00)), str(time(20, 00)), "660000000", "550000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 2, str(time(16, 00)), str(time(17, 00)), "770000000", "880000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 3, str(time(17, 00)), str(time(18, 00)), "880000000", "660000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 8)), 4, str(time(20, 00)), str(time(21, 00)), "880000000", "770000000"))
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 9)), 1, str(time(9, 00)), str(time(10, 00)) , "770000000", "660000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 9)), 2, str(time(8, 00)), str(time(9, 00))  , "880000000", "550000000")) 
    # write_to_db(SpecificTimeTraining(str(date(2023, 6, 9)), 3, str(time(10, 00)), str(time(11, 00)), "550000000", "880000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 11)), 1, str(time(16, 00)), str(time(17, 00)), "550000000", "660000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 11)), 2, str(time(17, 00)), str(time(18, 00)), "660000000", "770000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 11)), 3, str(time(18, 00)), str(time(19, 00)), "770000000", "550000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 11)), 4, str(time(19, 00)), str(time(20, 00)), "880000000", "660000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 18)), 1, str(time(16, 00)), str(time(17, 00)), "880000000", "660000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 18)), 2, str(time(19, 00)), str(time(20, 00)), "880000000", "660000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 18)), 3, str(time(18, 00)), str(time(19, 00)), "550000000", "880000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 18)), 4, str(time(17, 00)), str(time(18, 00)), "770000000", "880000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 19)), 1, str(time(19, 00)), str(time(20, 00)), "770000000", "660000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 19)), 2, str(time(18, 00)), str(time(19, 00)), "770000000", "880000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 19)), 3, str(time(16, 00)), str(time(17, 00)), "550000000", "660000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 19)), 4, str(time(20, 00)), str(time(21, 00)), "660000000", "550000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 20)), 1, str(time(16, 00)), str(time(17, 00)), "660000000", "770000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 20)), 2, str(time(17, 00)), str(time(18, 00)), "880000000", "770000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 20)), 3, str(time(18, 00)), str(time(19, 00)), "660000000", "550000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 20)), 4, str(time(19, 00)), str(time(20, 00)), "770000000", "660000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 21)), 1, str(time(19, 00)), str(time(20, 00)), "660000000", "550000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 21)), 2, str(time(16, 00)), str(time(17, 00)), "770000000", "880000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 21)), 3, str(time(17, 00)), str(time(18, 00)), "880000000", "660000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 21)), 4, str(time(20, 00)), str(time(21, 00)), "880000000", "770000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 22)), 1, str(time(16, 00)), str(time(17, 00)) , "770000000", "660000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 22)), 2, str(time(17, 00)), str(time(18, 00))  , "880000000", "550000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 22)), 3, str(time(18, 00)), str(time(19, 00)), "550000000", "880000000"))
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 23)), 1, str(time(9, 00)), str(time(10, 00)) , "770000000", "660000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 23)), 2, str(time(8, 00)), str(time(9, 00))  , "880000000", "550000000")) 
    write_to_db(SpecificTimeTraining(str(date(2023, 6, 23)), 3, str(time(10, 00)), str(time(11, 00)), "550000000", "880000000"))

def create_MembershipCancellationRequestForm():
    write_to_db(MembershipCancellationRequestForm("100100000", 4, 'Too expensive' , 'Declined',  str(date(2023, 4,12))))
    write_to_db(MembershipCancellationRequestForm("100200000", 12, 'Arriving difficulties', ' Declined', str(date(2023, 4,28))))
    write_to_db(MembershipCancellationRequestForm("100300000", 80, 'Schedule difficulties','In Process', str(date(2023, 4,15))))

def create_TrainingRegistrationForm():
    write_to_db(TrainingRegistrationForm("100000000", 1, 'Approved', str(date(2023, 6 ,4)), str(date(2023, 5 ,18))))
    write_to_db(TrainingRegistrationForm("100100000", 3, 'Approved', str(date(2023, 6, 5)), str(date(2023, 3, 1))))
    write_to_db(TrainingRegistrationForm("100300000", 2, 'Approved', str(date(2023, 6, 6)), str(date(2023, 5, 8))))
    write_to_db(TrainingRegistrationForm("100400000", 4, 'Approved', str(date(2023, 6, 4)), str(date(2023, 4, 10))))
    write_to_db(TrainingRegistrationForm("100200000", 1, 'Approved', str(date(2023, 6, 8)) ,str(date(2023, 5, 18))))

def create_TrainingCancellationRequestForm():
    write_to_db(TrainingCancellationRequestForm("100000000", 'Timetable constraints ' , 'Approved', str(date(2023, 6,8)),2 ,str(date(2023, 5,9))))
    write_to_db(TrainingCancellationRequestForm("100100000", 'Health conditions' , 'Approved',  str(date(2023,6, 4)), 1 , str(date(2023,5, 19)))) 
    write_to_db(TrainingCancellationRequestForm("100000000", 'Timetable constraints ' , 'Approved',  str(date(2023,6, 5)), 1 , str(date(2023,5, 19)))) 
    write_to_db(TrainingCancellationRequestForm("100400000", 'Timetable constraints ' , 'Approved',  str(date(2023,6,4)), 1 ,str(date(2023,5,19)))) 
    write_to_db(TrainingCancellationRequestForm("100200000", 'Health conditions' , 'Approved',  str(date(2023, 6, 7)), 2, str(date(2023, 5, 9))))  

def create_BrandedMerchandise():
    write_to_db(BrandedMerchandise( 300, 50.00 , 20 ,'Water Bottle', 'Stainless steel bottle, contains 500 ml' ,"111100000"))
    write_to_db(BrandedMerchandise(301, 80.00, 15, 'Towel' , 'Personal training towel, embroidered logo on the front', "111100000"))
    write_to_db(BrandedMerchandise(302, 70.00, 30, 'Bling Hat' , 'Designed hat made of 70% cotton fabric, embroidered logo on the front', "111100000"))

def create_Payment():
    # write_to_db(Payment(2000, 480.0, 'Approved' , "100100000", 8, None, str(date(2023, 5, 1)),))   
    # write_to_db(Payment(2001, 520.0, 'Approved', "100400000", 80, None, str(date(2022, 10, 1))))
    # write_to_db(Payment(2002, 50.0, 'Approved', "100200000", 12, 300, str(date(2023, 4, 20)) ))
    # write_to_db(Payment(2003, 80.0, 'Approved', "100100000", 8, 301, str(date(2023, 2, 20)) ))
    # write_to_db(Payment(2004, 700.0, 'Approved', "100300000", 100, None, str(date(2023, 3, 1))))
    # write_to_db(Payment(2005, 700.0, 'Approved', "100000000", 4, None , str(date(2023, 3, 12))))

    # write_to_db(Payment(2006, 520.0, 'Approved' , "100500000", 80, None, str(date(2023, 6, 1)),))   
    # write_to_db(Payment(2007, 50.0, 'Approved', "100600000", 4, 302, str(date(2022, 6, 1))))
    # write_to_db(Payment(2008, 50.0, 'Approved', "100200000", 12, 300, str(date(2023, 6, 2)) ))
    # write_to_db(Payment(2009, 80.0, 'Approved', "100100000", 8, 301, str(date(2023, 6, 3)) ))
    # write_to_db(Payment(2010, 700.0, 'Approved', "100700000", 100, None, str(date(2023, 6, 4))))
    # write_to_db(Payment(2011, 580.0, 'Approved', "100800000", 12, None , str(date(2023, 6, 5))))

    write_to_db(Payment(2012, 260.0, 'Approved' , "100000000", 4, None, str(date(2023, 5, 6)),))   
    write_to_db(Payment(2013, 480.0, 'Approved', "100100000", 8, None, str(date(2022, 10, 7))))
    write_to_db(Payment(2014, 50.0, 'Approved', "100200000", 12, 300, str(date(2023, 4, 8)) ))
    write_to_db(Payment(2015, 80.0, 'Approved', "100300000", 100, 301, str(date(2023, 2, 9)) ))
    write_to_db(Payment(2016, 700.0, 'Approved', "100700000", 100, None, str(date(2023, 3, 10))))
    write_to_db(Payment(2017, 50.0, 'Approved', "100800000", 12, 302 , str(date(2023, 3, 12))))

    write_to_db(Payment(2018, 260.0, 'Approved' , "100000000", 4, None, str(date(2023, 1, 6)),))   
    write_to_db(Payment(2019, 480.0, 'Approved', "100100000", 8, None, str(date(2022, 2, 7))))
    write_to_db(Payment(2020, 50.0, 'Approved', "100200000", 12, 300, str(date(2023, 5, 8)) ))
    write_to_db(Payment(2021, 80.0, 'Approved', "100300000", 100, 301, str(date(2023, 1, 4)) ))
    write_to_db(Payment(2022, 700.0, 'Approved', "100600000", 4, None, str(date(2023, 4, 4))))
    write_to_db(Payment(2023, 50.0, 'Approved', "100500000", 80, 302 , str(date(2023, 1, 1))))

    write_to_db(Payment(2024, 700.0, 'Approved' , "100300000", 100, None, str(date(2023, 1, 6)),))   
    write_to_db(Payment(2025, 520.0, 'Approved', "100400000", 80, None, str(date(2021, 2, 7))))
    write_to_db(Payment(2026, 50.0, 'Approved', "100500000", 80, 300, str(date(2021, 5, 8)) ))
    write_to_db(Payment(2027, 80.0, 'Approved', "100400000", 80, 301, str(date(2021, 1, 4)) ))
    write_to_db(Payment(2028, 700.0, 'Approved', "100600000", 4, None, str(date(2022, 4, 10))))
    write_to_db(Payment(2029, 50.0, 'Approved', "100700000", 100, 302 , str(date(2023, 1, 1))))

    write_to_db(Payment(2030, 700.0, 'Approved' , "100300000", 100, None, str(date(2023, 2, 2)),))   
    write_to_db(Payment(2031, 520.0, 'Approved', "100400000", 80, None, str(date(2023, 6, 6))))
    write_to_db(Payment(2032, 50.0, 'Approved', "100500000", 80, 300, str(date(2023, 5, 5)) ))
    write_to_db(Payment(2033, 80.0, 'Approved', "100400000", 80, 301, str(date(2023, 4, 4)) ))
    write_to_db(Payment(2034, 700.0, 'Approved', "100600000", 4, None, str(date(2023, 4, 10))))
    write_to_db(Payment(2035, 50.0, 'Approved', "100700000", 100, 302 , str(date(2023, 1, 1))))

    write_to_db(Payment(2036, 260.0, 'Approved' , "100000000", 4, None, str(date(2023, 1, 6)),))   
    write_to_db(Payment(2037, 480.0, 'Approved', "100100000", 8, None, str(date(2022, 5, 5))))
    write_to_db(Payment(2038, 50.0, 'Approved', "100200000", 12, 300, str(date(2023, 5, 5))))
    write_to_db(Payment(2039, 80.0, 'Approved', "100300000", 100, 301, str(date(2023, 1, 4))))
    write_to_db(Payment(2040, 700.0, 'Approved', "100600000", 4, None, str(date(2023, 4, 6))))
    write_to_db(Payment(2041, 50.0, 'Approved', "100500000", 80, 302 , str(date(2023, 1, 2))))
