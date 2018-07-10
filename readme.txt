Βήματα:
1)Εγκατάσταση MySQL,Python και pymysql(pip3 install pymysql) στον υπολογιστή μας.
2)Τρέχουμε το connector.py (κάνουμε edit με IDLE και αλλάζουμε τα στοιχεία μας για την σύνδεση στην βάση).
3)Επειδή τα accounts είναι randomly generated στην βάση δεν μπορούμε να σας δώσουμε κάποιο username και password.

Συνδεόμαστε λοιπόν με cmd και χρησιμοποιούμε την εντολή

mysql -u root -p -h localhost --default-character-set=utf8

(Προσοχή utf8 charset)

Στην συνέχεια εκτελούμε τα παρακάτω query.

USE progress;
SELECT * FROM φοιτητής;

Διαλέγουμε ένα από τα accounts (username,password)

4)Τρέχουμε το application.py και συνδεόμαστε με τα credentials που προμηθευτήκαμε.
