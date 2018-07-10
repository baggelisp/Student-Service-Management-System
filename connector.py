# -*- coding: utf-8 -*-

import random
import pymysql
import sys
import datetime
import warnings

warnings.filterwarnings("ignore")

names=['ΠΑΝΑΓΙΩΤΗΣ','ΧΡΗΣΤΟΣ','ΚΑΛΛΙΟΠΗ','ΚΥΡΙΑΚΟΣ','ΧΡΙΣΤΙΝΑ','ΜΑΝΩΛΗΣ','ΑΝΤΩΝΗΣ','ΑΝΤΩΝΙΑ','ΑΡΙΣΤΕΙΔΗΣ','ΑΡΤΕΜΗΣ', \
       'ΙΩΑΝΝΑ','ΔΗΜΗΤΡΗΣ','ΑΡΙΣΤΟΤΕΛΗΣ','ΧΑΡΑ','ΑΘΑΝΑΣΙΟΣ','ΝΙΚΟΛΑΟΣ','ΓΙΩΡΓΟΣ','ΣΤΕΛΙΟΣ','ΔΙΟΜΗΔΗΣ','ΙΩΑΝΝΗΣ','ΓΕΩΡΓΙΑ', \
       'ΑΓΓΕΛΙΚΗ','ΝΙΚΗ','ΛΕΩΝΙΔΑΣ','ΔΗΜΗΤΡΗΣ','ΝΙΚΟΛΑΟΣ','ΦΑΝΗΣ','ΕΛΛΗ','ΑΝΤΩΝΗΣ','ΗΛΙΑΣ','ΓΕΩΡΓΙΟΣ', \
       'ΣΤΑΜΑΤΗΣ','ΕΛΕΥΘΕΡΙΟΣ','ΔΗΜΟΣΘΕΝΗΣ','ΙΩΣΗΦΙΝΑ','ΑΝΕΣΤΗΣ','ΑΛΕΞΙΑ','ΒΑΣΙΛΙΚΗ','ΙΩΑΝΝΗΣ','ΑΧΙΛΛΕΑΣ','ΔΗΜΗΤΡΙΟΣ', \
       'ΑΝΤΡΕΑΣ','ΕΛΕΥΘΕΡΙΑ','ΜΕΛΕΤΗΣ','ΑΓΗΣΙΛΑΟΣ','ΑΛΕΚΑ','ΘΑΛΕΙΑ','ΑΝΤΡΕΑΣ','ΜΙΛΤΙΑΔΗΣ','ΔΗΜΗΤΡΙΟΣ']

lastnames=["ΚΑΠΡΑΛΟΣ",'ΚΟΥΛΟΧΕΡΗΣ','ΚΑΠΑΓΙΑΝΝΗ','ΙΩΑΝΝΟΥ','ΚΑΜΕΝΟΥ','ΜΑΡΓΑΡΙΤΗΣ','ΚΑΡΑΤΖΑΣ','ΠΟΛΥΧΡΟΝΑΚΗ','ΚΑΛΑΠΑΝΙΔΑΣ','ΛΙΑΚΟΠΟΥΛΟΣ', \
           'ΚΥΡΙΑΚΟΥ','ΚΑΖΑΤΖΗΣ','ΣΚΟΠΕΛΙΤΗΣ','ΚΑΤΣΑΤΟΥ','ΜΠΛΑΤΣΙΩΤΗΣ', 'ΘΑΛΑΣΣΙΝΟΣ','ΦΙΩΤΑΚΗΣ','ΔΡΙΛΛΗΣ','ΣΩΤΗΡΙΟΥ','ΓΕΩΡΓΙΟΥ', \
           'ΛΙΑΚΟΥ','ΔΕΜΕΤΗ','ΠΟΛΥΧΡΟΝΑΚΗ','ΑΡΑΧΤΟΣ','ΛΑΜΙΑΣ','ΓΙΑΝΝΟΥΛΗΣ','ΚΑΠΑΚΛΗΣ','ΚΑΦΑΝΤΑΡΗ','ΠΑΠΑΡΙΖΟΣ','ΠΟΛΙΤΗΣ', \
           'ΚΑΡΑΦΛΟΣ','ΔΗΜΗΤΡΙΟΥ','ΠΑΠΑΧΡΗΣΤΟΣ','ΚΙΤΡΙΝΟΣ','ΓΚΙΟΚΑ','ΓΚΙΩΝΑΚΗΣ','ΒΑΛΣΑΜΗ','ΒΑΛΣΑΜΗ','ΓΙΑΝΝΟΠΟΥΛΟΣ','ΜΑΝΙΑΤΗΣ', \
           'ΝΑΝΟΠΟΥΛΟΣ','ΧΑΣΑΠΟΓΛΟΥ','ΑΡΑΠΟΓΛΟΥ','ΝΙΑΡΧΟΥ','ΔΙΑΜΑΝΤΟΠΟΥΛΟΣ','ΛΑΜΠΡΟΠΟΥΛΟΥ','ΞΥΠΟΛΙΑ','ΨΑΡΙΑΝΟΣ','ΧΑΡΑΛΑΜΠΟΥΣ','ΚΑΛΠΑΚΙΔΗΣ']
tomeas=['Η/Υ','ΣΑΕ','ΣΗΕ','Τ&ΤΠ']
odos=['Μαιζώνος','Κορίνθου','Κανακάρη','Καραισκάκη','Αγίου Νικολάου','Βότση','Πατρέος','Νόρμαν','Ζαίμη','Αράτου']
dieuth=[]
am=[]
a=1000000
password=[]
email=[]


for i in range(50):
    am.append(a+i)
    password.append(''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(6)))
    dieuth.append(random.choice(odos)+ " " + str(random.randint(1,200)))
    email.append(str(am[i])+"@upnet.gr")



mathimata = ['Υπολογιστές', 'Βάσεις Δεδομένων', 'Κυκλώματα 1', 'Κυκλώματα 2',
           'Μαθηματικά 1', 'Μαθηματικά 2', 'Φυσική 1', 'Φυσική 2', 'Τηλεπικοινωνίες',
           'Ψηφιακά Συστήματα','Προγραμματισμός','Ηλεκτικές Μηχανές' ]

kathigites = ['Θραμπουλίδης','Αβούρης','Κούσουλας','Κούσουλας', \
              'Μαρκάκης','Περδίος','Κουνάβης','Σβάρνας','Αντωνακόπουλος', \
              'Θεοδωρίδης','Θραμπουλίδης','Καππάτου']


#############################################################################################################################


try:
    db = pymysql.connect(host="localhost",    \
                         user="root",         \
                         passwd="",           \
                         charset="utf8")
except pymysql.err.OperationalError:
    print ("Πρόβλημα σύνδεσης...προσπάθησε ξανά!")
    input("Έξοδος...")
    sys.exit(0)
        
cur = db.cursor()

sql = "DROP DATABASE IF EXISTS progress"
cur.execute(sql)

sql = "CREATE DATABASE progress CHARACTER SET utf8 COLLATE utf8_general_ci"
cur.execute(sql)

sql = "USE progress"
cur.execute(sql)

sql="SET FOREIGN_KEY_CHECKS=0"
cur.execute(sql)

sql="DROP TABLE IF EXISTS `φοιτητής`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `φοιτητής` (
	`αρ μητρωου` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`κωδικός` VARCHAR(255) NOT NULL ,
	`όνομα` VARCHAR(255) NOT NULL,
	`επώνυμο` VARCHAR(255) NOT NULL,
	`διεύθυνση` VARCHAR(255) NOT NULL,
	`τηλέφωνο` INT NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	`σχολή` VARCHAR(255) NOT NULL,
	`τμήμα` VARCHAR(255) NOT NULL,
	`κατάσταση` VARCHAR(255) NOT NULL,
	`τομέας` VARCHAR(255) ,
	`έτος` INT NOT NULL,
	PRIMARY KEY (`αρ μητρωου`))
	'''
cur.execute(sql)


sql="DROP TABLE IF EXISTS `ΜΑΘΗΜΑ`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `ΜΑΘΗΜΑ` (
	`κωδικός` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`διδακτ μοναδ` INT NOT NULL,
	`τίτλος` VARCHAR(255) NOT NULL,
	`εξάμηνο` INT NOT NULL,
	`ομάδα` VARCHAR(255),
	`περίοδος` VARCHAR(255) NOT NULL,
	`ακ έτος` INT NOT NULL,
	`καθηγητής` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`κωδικός`)
)'''
cur.execute(sql)

sql="DROP TABLE IF EXISTS `ΒΑΘΜΟΛΟΓΙΑ`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `ΒΑΘΜΟΛΟΓΙΑ` (
	`βαθμολογία` INT ,
	`κατάσταση` VARCHAR(255) ,
	`αρ μητρωου φοιτητη` INT NOT NULL,
	`κωδ μαθήματος` INT NOT NULL,
	`εξεταστική περίοδος` VARCHAR(255) NOT NULL
)'''
cur.execute(sql)

sql="DROP TABLE IF EXISTS `αίτηση εισαγωγής/επανεγγραφών`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `αίτηση εισαγωγής/επανεγγραφών` (
	`αρ αίτησης` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`τύπος εγγραφής` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`αρ αίτησης`)
)'''
cur.execute(sql)


sql="DROP TABLE IF EXISTS `αίτηση αποφοίτησης`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `αίτηση αποφοίτησης` (
	`αρ αίτησης` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`έτος αποφοίτησης` INT NOT NULL,
	`αναμενώμενη ημ/νια αποφοίτησης` DATE ,
	PRIMARY KEY (`αρ αίτησης`)
)'''
cur.execute(sql)

sql="DROP TABLE IF EXISTS `αίτηση ΠΙΣΤΟΠΟΙΗΤΙΚΏΝ`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `αίτηση ΠΙΣΤΟΠΟΙΗΤΙΚΏΝ` (
	`αρ αίτησης` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`τύπος βεβαίωσης` VARCHAR(255) NOT NULL,
	`λόγος χορήγησης` VARCHAR(255) NOT NULL,
	`επιλογή αναλυτικής` BOOLEAN NOT NULL,
	PRIMARY KEY (`αρ αίτησης`)
)'''
cur.execute(sql)

sql="DROP TABLE IF EXISTS `δήλωση ειδίκευσης/κατεύθυνσης`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `δήλωση ειδίκευσης/κατεύθυνσης` (
	`αρ δήλωσης` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`ημ/νια έναρξης` DATE ,
	`ημ/νια λήξης` DATE,
	`ειδίκευση` VARCHAR(255) NOT NULL,
	`αρ μητρώου φοιτητή` INT NOT NULL,
	`ημ/νια δήλωσης` DATE NOT NULL,
	PRIMARY KEY (`αρ δήλωσης`)
)'''
cur.execute(sql)

sql="DROP TABLE IF EXISTS `υποτροφίες`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `υποτροφίες` (
	`αρ αίτησης` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`φορέας` VARCHAR(255) NOT NULL,
	`έναρξη παροχής` DATE,
	`λήξη παροχής` DATE,
	`τύπος υποτροφίας` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`αρ αίτησης`)
)'''
cur.execute(sql)

sql="DROP TABLE IF EXISTS `ΔΉΛΩΣΗ`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `ΔΉΛΩΣΗ` (
	`αρ μητρώου` INT NOT NULL,
	`κωδ μαθήματος` INT NOT NULL,
	`ημ/νια δήλωσης` DATE NOT NULL
)'''
cur.execute(sql)

sql="DROP TABLE IF EXISTS `αίτηση`"
cur.execute(sql)
sql='''CREATE TABLE IF NOT EXISTS `αίτηση` (
	`ακαδ έτος` INT NOT NULL,
	`ημ/νια αίτησης` DATE NOT NULL,
	`αρ αίτησης` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`αρ μητρώου φοιτητή` INT NOT NULL,
	`κατάσταση` VARCHAR(255),
	`σχόλια φοιτητή` VARCHAR(255),
	PRIMARY KEY (`αρ αίτησης`)
)'''
cur.execute(sql)


s1='''ALTER TABLE `βαθμολογια` ADD CONSTRAINT `βαθμολογια_fk0` FOREIGN KEY (`αρ μητρωου φοιτητη`) REFERENCES `φοιτητής`(`αρ μητρωου`)'''

s2='''ALTER TABLE `βαθμολογια` ADD CONSTRAINT `βαθμολογια_fk1` FOREIGN KEY (`κωδ μαθήματος`) REFERENCES `μαθημα`(`κωδικός`)'''

s3='''ALTER TABLE `αίτηση εισαγωγής/επανεγγραφών` ADD CONSTRAINT `αίτηση εισαγωγής/επανεγγραφών_fk0` FOREIGN KEY (`αρ αίτησης`) REFERENCES `αίτηση`(`αρ αίτησης`)'''

s4='''ALTER TABLE `αίτηση αποφοίτησης` ADD CONSTRAINT `αίτηση αποφοίτησης_fk0` FOREIGN KEY (`αρ αίτησης`) REFERENCES `αίτηση`(`αρ αίτησης`)'''

s5='''ALTER TABLE `αίτηση πιστοποιητικών` ADD CONSTRAINT `αίτηση πιστοποιητικών_fk0` FOREIGN KEY (`αρ αίτησης`) REFERENCES `αίτηση`(`αρ αίτησης`)'''

s6='''ALTER TABLE `δήλωση ειδίκευσης/κατεύθυνσης` ADD CONSTRAINT `δήλωση ειδίκευσης/κατεύθυνσης_fk0` FOREIGN KEY (`αρ μητρώου φοιτητή`) REFERENCES `φοιτητής`(`αρ μητρωου`)'''

s7='''ALTER TABLE `υποτροφίες` ADD CONSTRAINT `υποτροφίες_fk0` FOREIGN KEY (`αρ αίτησης`) REFERENCES `αίτηση`(`αρ αίτησης`)'''

s8='''ALTER TABLE `δήλωση` ADD CONSTRAINT `δήλωση_fk0` FOREIGN KEY (`αρ μητρώου`) REFERENCES `φοιτητής`(`αρ μητρωου`)'''

s9='''ALTER TABLE `δήλωση` ADD CONSTRAINT `δήλωση_fk1` FOREIGN KEY (`κωδ μαθήματος`) REFERENCES `μαθημα`(`κωδικός`)'''

s10='''ALTER TABLE `αίτηση` ADD CONSTRAINT `αίτηση_fk0` FOREIGN KEY (`αρ μητρώου φοιτητή`) REFERENCES `φοιτητής`(`αρ μητρωου`)'''

cur.execute(s1)
cur.execute(s2)
cur.execute(s3)
cur.execute(s4)
cur.execute(s5)
cur.execute(s6)
cur.execute(s7)
cur.execute(s8)
cur.execute(s9)
cur.execute(s10)



#EISAGWGI STON PINAKA FOITHTHS
for i in range (50):
    etos=random.randint(1,5)
    if etos>3:
        tom=random.choice(tomeas)
    else:
        tom="-"
    sql='''INSERT INTO φοιτητής VALUES ('%d','%s','%s','%s','%s','%d','%s','%s','%s','%s','%s','%d');''' % \
        (am[i],password[i],names[i],lastnames[i],dieuth[i],random.randint(69000000,69999999),\
        email[i],"ΠΟΛΥΤΕΧΝΙΚΗ","ΗΜΤΥ","ΦΟΙΤΗΤΗΣ",tom,etos)
    cur.execute(sql)
    
kod=1000
tomeas.append("-")
for i in range (len(mathimata)):
    sql='''INSERT INTO μαθημα VALUES ('%d','%d','%s','%d','%s','%s','%d','%s');''' %  \
        (kod+i,random.randint(3,8),mathimata[i],random.randint(1,10),random.choice(tomeas),random.choice(["χειμερινό","εαρινό"]), \
        2018,kathigites[i])
    cur.execute(sql)
    


katastaithshs=['Εγκρίνεται','Απορρίπτεται','Εκκρεμής']

tuposbeaiosis=['Ενεργού Φοιτητή','Φοιτητικής κατάστασης','Στρατολογικής χρήσης','Κατεύθυνσης']

logosxorhghshs=['Κάθε νόμιμη χρήση','Εφορία','Άλλο']

foreas=['Aκαδημία Aθηνών','Εθνική τράπεζα','Ίδρυμα κρατικών υποτροφιών','Υπουργείο Παιδείας','Unesco','Κέντρου Ευρωπαϊκών Σπουδών','Πανεπιστήμιο Πατρών']

date=datetime.datetime.utcnow().strftime('%Y-%m-%d')

for i in range (40):
    sql='''INSERT INTO αίτηση VALUES ('%d','%s','%d','%d','%s','%s');''' %  \
        (2018,date,i+1,random.randint(1000000,1000050),random.choice(katastaithshs),"-")
    cur.execute(sql)
#datetime.datetime(year=2018, month=7, day=24).strftime('%Y-%m-%d')
for i in range (10):
    sql='''INSERT INTO `αίτηση αποφοίτησης` VALUES ('%d','%d','%s');''' %  \
        (i+1,2018,"2018-7-24")
    cur.execute(sql)
    sql1='''INSERT INTO `αίτηση εισαγωγής/επανεγγραφών` VALUES ('%d','%s');''' %  \
        (i+11,"εγγραφη στο εξάμηνο")
    cur.execute(sql1)
    sql2='''INSERT INTO `αίτηση πιστοποιητικών` VALUES ('%d','%s','%s','%s');''' %  \
        (i+21,random.choice(tuposbeaiosis),random.choice(logosxorhghshs),random.choice([0,1]))
    cur.execute(sql2)
    sql3='''INSERT INTO `υποτροφίες` VALUES ('%d','%s','%s','%s','%s');''' %  \
        (i+31,random.choice(foreas),date,"2022-6-30",random.choice(["Προπτυχιακές","Μεταπρυχιακές","Διδακτορικού","Μεταδιδακτορικου"]))
    cur.execute(sql3)

tomeas=['Η/Υ','ΣΑΕ','ΣΗΕ','Τ&ΤΠ']

for i in range (len(am)):
    sql='''SELECT `τομέας` FROM `φοιτητής` WHERE `αρ μητρωου`=%d''' %(am[i])
    cur.execute(sql)
    tom=cur.fetchall()[0][0]
    if tom=="-":
        continue
    else:
        sql='''INSERT INTO `δήλωση ειδίκευσης/κατεύθυνσης` VALUES ('%d','%s','%s','%s','%d','%s');''' %  \
            (i+1,"2018-9-1","2022-6-30",tom,am[i],date)
        cur.execute(sql)


for i in range (len(am)):
    for j in range (random.randint(1,len(mathimata))):
        sql='''INSERT INTO `δήλωση` VALUES ('%d','%d','%s');''' %  \
            (am[i],1000+j,date)
        cur.execute(sql)
        
        bathmos=random.randint(0,10)
        if bathmos>=5:
            katast="Επιτυχών"
        else:
            katast="Αποτυχών"
        sql='''INSERT INTO `βαθμολογια` VALUES ('%d','%s','%d','%d','%s');''' %  \
            (bathmos,katast,am[i],1000+j,random.choice(["Ιανουαρίου 2018","Ιουνίου 2018","Σεπτεμβρίου 2018"]))
        cur.execute(sql)
                                       

db.commit()
db.close()
print ("Επιτυχής εισαγωγή δεδομένων")
input("Έξοδος...")
