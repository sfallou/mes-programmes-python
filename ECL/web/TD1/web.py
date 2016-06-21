import csv
import sqlite3
import time
######################################################################################################################
conn = sqlite3.connect('sncf.sqlite')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS regularite_tgv")
# Create table
c.execute("CREATE TABLE regularite_tgv(id INTEGER PRIMARY KEY, annee INTEGER, mois INTEGER, axe text, depart text, arrive text, nb_prevus INTEGER, nb_train real,nb_annules INTEGER, nb_retards INTEGER, regularite real, commentaire text)")

####################################################################################
with open('regularite-mensuelle-tgv.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    got_header= False
    t1=time.clock()
    for row in reader:
        if (not got_header):
            got_header=True
            continue
        annee,mois= row[0].split(sep='-')
        c.execute('INSERT INTO regularite_tgv VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)',(annee,mois)+tuple(v for v in row[1:]))
    t2=time.clock()
conn.commit()
conn.close()
print("Temps de chargement:",t2-t1," secondes")