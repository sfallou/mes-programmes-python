import csv
"""with open('regularite-mensuelle-tgv.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print('; '.join(row))"""
        
import sqlite3
conn = sqlite3.connect('sncf.sqlite')
c = conn.cursor()
c.execute('''SELECT * FROM regularite_tgv''')
all_rows = c.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print(row)
