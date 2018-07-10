# -*- coding: utf-8 -*-

import random
import pymysql
import sys
import datetime

try:
    db = pymysql.connect(host="localhost",    \
                         user="root",         \
                         passwd="",           \
                         db="progress",    \
                         charset="utf8")
except pymysql.err.OperationalError:
    print ("Πρόβλημα σύνδεσης...προσπάθησε ξανά!")
    input("Έξοδος...")
    sys.exit(0)
    
cur = db.cursor()

#---------------------------------------------------------------------------------------------------
def printres(cur,stiles):
    result=cur.fetchall()
    for row in result:
        print()
        print(" ----------------------------------------------------------")
        for i in stiles:
            
            if type(row[i]) is int:
                print ("| %32s: | %20d |" % (cur.description[i][0],row[i]))
            else:
                print ("| %32s: | %20s |" % (cur.description[i][0],row[i]))
        print(" ----------------------------------------------------------")
        
#########################################################################
def stoixeia():
    sql='''SELECT * FROM `φοιτητής` WHERE `αρ μητρωου`=%d and `κωδικός`='%s' ;''' % (username,password)
    cur.execute(sql)
    printres(cur,[0,2,3,4,5,6,7,8,9,10,11])
 
#########################################################################
def bathmologia():

    sql='''SELECT `τίτλος` as Μάθημα,βαθμολογία,κατάσταση,`εξεταστική περίοδος` FROM `βαθμολογια` join `μαθημα` on `κωδικός`=`κωδ μαθήματος`  where `αρ μητρωου φοιτητη`=%d''' % (username)
    cur.execute(sql)
    printres(cur,[0,1,2,3])

def mesosoros():
    sql='''SELECT AVG(`βαθμολογία`) as Βαθμολογία FROM `βαθμολογια` join `μαθημα` on `κωδικός`=`κωδ μαθήματος` where `αρ μητρωου φοιτητη`=%d and `βαθμολογία`>=5''' % (username)
    cur.execute(sql)
    result=cur.fetchall()
    print ()
    print ("Μέσος Όρος Μαθημάτων: %.2f" % result[0])

def batheksamino():
    sql='''SELECT `εξεταστική περίοδος`,AVG(`βαθμολογία`) as `ΜΟ εξεταστικής` FROM `βαθμολογια` join `μαθημα` on `κωδικός`=`κωδ μαθήματος` where `αρ μητρωου φοιτητη`=%d and `βαθμολογία`>=5 GROUP by `εξεταστική περίοδος`''' % (username)
    cur.execute(sql)
    print ()
    print("Mέσος όρος μαθημάτων ανά εξεταστική περίοδο")
    printres(cur,[0,1])

    
 

#########################################################################
def mathimata():
    sql='''SELECT `τίτλος`,`κωδικός`,`εξάμηνο`,`ομάδα` as Τομέας,`διδακτ μοναδ`,`περίοδος`,`ακ έτος`,`καθηγητής` FROM `μαθημα` ORDER by `εξάμηνο`'''
    cur.execute(sql)
    printres(cur,[0,1,2,3,4,5,6,7])

#########################################################################
def aitiseis():

    sql='''    SELECT `αίτηση`.`αρ αίτησης`,`αναμενώμενη ημ/νια αποφοίτησης`,`έτος αποφοίτησης`,`ημ/νια αίτησης`,`κατάσταση` FROM `αίτηση` JOIN `αίτηση αποφοίτησης` on `αίτηση`.`αρ αίτησης`=`αίτηση αποφοίτησης`.`αρ αίτησης` where `αρ μητρώου φοιτητή`=%d''' % (username) 
    cur.execute(sql)
    print ("Αιτήσεις αποφοίτησης:")
    printres(cur,[0,1,2,3,4])
    print ()

    sql='''SELECT `αίτηση`.`αρ αίτησης`,`τύπος εγγραφής`,`ημ/νια αίτησης`,`κατάσταση` FROM `αίτηση` JOIN `αίτηση εισαγωγής/επανεγγραφών` on `αίτηση`.`αρ αίτησης`=`αίτηση εισαγωγής/επανεγγραφών`.`αρ αίτησης` where `αρ μητρώου φοιτητή`=%d''' % (username)  
    cur.execute(sql)
    print ("Αιτήσεις εισαγωγής/επανεγγραφών:")
    printres(cur,[0,1,2,3])
    print ()

    sql='''SELECT `αίτηση`.`αρ αίτησης`,`λόγος χορήγησης`,`τύπος βεβαίωσης`,`επιλογή αναλυτικής`,`ημ/νια αίτησης`,`κατάσταση` FROM `αίτηση` JOIN `αίτηση πιστοποιητικών` on `αίτηση`.`αρ αίτησης`=`αίτηση πιστοποιητικών`.`αρ αίτησης` where `αρ μητρώου φοιτητή`=%d''' % (username) 
    cur.execute(sql)
    print ("Αιτήσεις πιστοποιητικών:")
    printres(cur,[0,1,2,3,4,5])
    print ()
    
    sql='''SELECT `αίτηση`.`αρ αίτησης`,`ημ/νια αίτησης`,`φορέας`,`τύπος υποτροφίας`,`έναρξη παροχής`,`λήξη παροχής`,`κατάσταση` FROM `αίτηση` JOIN `υποτροφίες` on `αίτηση`.`αρ αίτησης`=`υποτροφίες`.`αρ αίτησης` where `αρ μητρώου φοιτητή`=%d''' % (username) 
    cur.execute(sql)
    print ("Αιτήσεις υποτροφίας:")
    printres(cur,[0,1,2,3,4,5,6])
    print ()

    
date=datetime.datetime.utcnow().strftime('%Y-%m-%d')
#########################################################################
def dimaitisis():
    print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
    print('1: Αίτηση αποφοίτησης')
    print('2: Αίτηση επανεγγραφής')
    print('3: Αίτηση πιστοποιητικών')
    print('4: Αίτηση υποτροφιας')

    answer = ' '
    while not answer in '1 2 3 4 5 6 7'.split():
        answer = input('επιλογή.....')
        if answer == '': return 0
        elif not answer: break
        else:
            sql='SELECT `αρ αίτησης` FROM `αίτηση` ORDER BY 1 DESC'
            cur.execute(sql)
            result=cur.fetchall()
            a=int(result[0][0])

            
            sql='''INSERT INTO αίτηση VALUES ('%d','%s','%d','%d',NULL,NULL);''' %  \
                (2018,date,a+1,username)
            cur.execute(sql)
            
            if answer == '1':
                sql='''INSERT INTO `αίτηση αποφοίτησης` VALUES ('%d','%d','%s');''' %  \
                (a+1,2018,"0000-00-00")
                
            elif answer == '2':
                sql='''INSERT INTO `αίτηση εισαγωγής/επανεγγραφών` VALUES ('%d','%s');''' %  \
                (a+1,"εγγραφή στο εξάμηνο")
            
            elif answer == '3':
                try:
                    tupos = input('Τύπος βεβαίωσης:')
                    logos = input('Λόγος χορήγησης:')
                    anal = int(input('Επιλογή αναλυτικής(1/0):'))
                    sql='''INSERT INTO `αίτηση πιστοποιητικών` VALUES ('%d','%s','%s','%d');''' %  \
                    (a+1,tupos,logos,anal)
                except ValueError:
                    print ("Υπήρξε πρόβλημα...Προσπάθησε ξανά")
                    dimaitisis()
                    return
                    
            elif answer == '4':
                try:
                    foreas = input('Φορέας:')
                    tupos = input('Τύπος υποτροφίας:')
                    sql='''INSERT INTO `υποτροφίες` VALUES ('%d','%s',NULL,NULL,'%s');''' %  \
                        (a+1,foreas,tupos)
                except ValueError:
                    print ("Υπήρξε πρόβλημα...Προσπάθησε ξανά")
                    dimaitisis()
                    return
            print ("Η αίτηση σας δημιουργήθηκε")   
            cur.execute(sql)
            db.commit()

#########################################################################
def dilwsi():
    kwd="kati"
    while kwd is not "":
        print()
        print("Enter για εξοδο απο την δήλωση")
        kwd = input('Κωδικός μαθήματος:')
        if kwd=='':break
        try:
            kwd=int(kwd)
        except ValueError:
            print ("Λάθος...προσπάθησε ξανα")
            continue
        
        sql="SELECT `κωδικός` FROM `μαθημα`"
        cur.execute(sql)
        res1=cur.fetchall()
        sql="SELECT `κωδ μαθήματος` FROM `δήλωση` WHERE `αρ μητρώου`=%d" %(username)
        cur.execute(sql)
        res2=cur.fetchall()
        
        if any(kwd in res for res in res1):
            if not any (kwd in ress for ress in res2):
                sql='''INSERT INTO `δήλωση` VALUES ('%d','%s','%s');''' %(username,kwd,date)
                cur.execute(sql)
                print("Επιτυχής δήλωση μαθηματος")
                db.commit()
            else:
                print ("Το έχεις δηλώσει ήδη το μάθημα")
        else:
            print ("Το μάθημα δεν είναι υπάρχει...προσπάθησε κάποιο άλλο")
        
        
        
        


#########################################################################
def prodilwsi():
    
    sql='''SELECT `κωδ μαθήματος`,`ημ/νια δήλωσης`,`τίτλος`,`διδακτ μοναδ`,`εξάμηνο`,`ομάδα`,`περίοδος`,`ακ έτος`,`καθηγητής`  \
    FROM `δήλωση` join `μαθημα` on `κωδ μαθήματος`=`κωδικός` \
    where `αρ μητρώου`=%d ORDER BY `εξάμηνο` DESC''' % (username)
    cur.execute(sql)
    printres(cur,[0,1,2,3,4,5,6,7,8])

#--------------------------------------------------------------------------
def proeidikeusis():
    sql='''SELECT * FROM `δήλωση ειδίκευσης/κατεύθυνσης` where `αρ μητρώου φοιτητή`=%d''' % (username)
    if cur.execute(sql)==0:
        print ("Δεν έχετε πραγματοποιήσει δήλωση ειδίκευσης")
    else:
        cur.execute(sql)
        printres(cur,[0,1,2,3,5])

def eidikeusi():
    if (cur.execute('''SELECT * FROM `δήλωση ειδίκευσης/κατεύθυνσης` where `αρ μητρώου φοιτητή`=%d''' % (username))==1):
        print ("Η δήλωση ειδίκευσης/κατεύθυνσης έχει πραγματοποιηθεί")
    else:
        print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
        print('1: Η/Υ')
        print('2: ΣΑΕ')
        print('3: ΣΗΕ')
        print('4: Τ&ΤΠ')

        tomeas=['Η/Υ','ΣΑΕ','ΣΗΕ','Τ&ΤΠ']
        
        try:
            a = int(input('επιλογή.....'))
        except ValueError:
            print ("Λάθος...προσπάθησε ξανα")
        
        sql='''INSERT INTO `δήλωση ειδίκευσης/κατεύθυνσης` VALUES (NULL,NULL,NULL,'%s','%d','%s');''' %(tomeas[a-1],username,date)
        cur.execute(sql)
        print("Επιτυχής δήλωση ειδίκευσης")
        db.commit()
        
        
    

#########################################################################
#########################################################################
def main_menu(answer):
        
        if answer == '1':
            stoixeia()
        elif answer == '2':
            print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
            print('1: Βαθμολογία μαθημάτων')
            print('2: Βαθμολογία ανά εξάμηνο')
            print('3: Μέσος όρος μαθημάτων')
            a = input('επιλογή.....')
            if a=="1": bathmologia()
            elif a=="2": batheksamino()
            elif a=="3": mesosoros()
  
        elif answer == '3': mathimata()
        elif answer == '4':
            print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
            print('1: Λίστα αιτήσεων')
            print('2: Δημιουργία αίτησης')
            a = input('επιλογή.....')
            if a=="1": aitiseis()
            elif a=="2": dimaitisis()
            
        elif answer == '5':
            print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
            print('1: Προβολή δήλωσης')
            print('2: Δημιουργία δήλωσης')
            a = input('επιλογή.....')
            if a=="1": prodilwsi()
            elif a=="2": dilwsi()
        elif answer == '6':
            print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
            print('1: Προβολή δήλωσης')
            print('2: Δημιουργία δήλωσης')
            a = input('επιλογή.....')
            if a=="1": proeidikeusis()
            elif a=="2": eidikeusi()
        
        

#########################################################################

def main():
    while (True):
        print('\nΕΠΙΛΟΓΕΣ (enter για έξοδο)')
        print('1: Καρτέλα φοιτητή')
        print('2: Βαθμολογίες')
        print('3: Μαθήματα')
        print('4: Αιτήσεις')
        print('5: Δήλωση μαθημάτων')
        print('6: Δήλωση ειδίκευσης/κατεύθυνσης')
        
        answer = ' '
        while not answer in ' 1 2 3 4 5 6 '.split():
            answer = input('επιλογή.....')
            if answer == '': return 0
        main_menu(answer)
    

########################################################################
########################## MAIN PROGRAM ##########################

        
print ("Καλωσόρισες στην υπηρεσία διαχείρησης δεδομένων φοιτητή")

while (True):
    try:
        print ("Σύνδεση:")
        username = int(input('Αριθμός μητρώου: ')) #ginetai elenxos an am einai int alliws typeerror
        password = input('Κωδικός: ')

        if username>9999999 or len(password)!=6 or password.find("'")!=-1 or password.find('''"''')!=-1: #apofugi injection
            print ("Λάθος...προσπάθησε ξανά")
            continue
        sql='''SELECT * FROM `φοιτητής` WHERE `αρ μητρωου`=%d and `κωδικός`='%s';''' % (username,password)
        
        rows_count=cur.execute(sql)
        if rows_count > 0:
            for row in cur.fetchall():
                print ()
                print ("Γεια σου",row[2])
            main()
            break
        else:
             print ("Λάθος...προσπάθησε ξανά")
    except TypeError:
        print ("Λάθος...προσπάθησε ξανά")
        continue



db.commit()
db.close()



