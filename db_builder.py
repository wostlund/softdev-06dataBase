import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

q = "CREATE TABLE students (name TEXT, id INTEGER)"
c.execute(q)    #run SQL query
peeps = open("peeps.csv")
p = csv.DictReader(peeps)
for a in p:
    q="INSERT INTO students VALUES ("+ "\'" + a["name"] + "\'," + a["id"] +")"
    c.execute(q)
    
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)
peeps = open("courses.csv")
p = csv.DictReader(peeps)
for a in p:
    q="INSERT INTO courses VALUES ('"+a["code"]+"','"+a["id"]+"','"+a["mark"]+"')"
c.execute(q)
 
#==========================================================
db.commit() #save changes
db.close()  #close database

#print("Error: discobandit.db already exists, delete it and try again")

