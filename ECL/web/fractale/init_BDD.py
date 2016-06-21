import sqlite3
import os
import shutil


#Creation de la bdd percolation
conn = sqlite3.connect('percolation.sqlite')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS image")
# Create table
c.execute("CREATE TABLE image(id INTEGER PRIMARY KEY, nom_image text, chemin text)")
conn.commit()
conn.close()
## on supprime le repertoire images
shutil.rmtree('client/images')
## on recrée le repertoire images
os.makedirs('client/images')