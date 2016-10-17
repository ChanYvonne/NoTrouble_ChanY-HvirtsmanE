import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

fObj1 = open("peeps.csv") 
fObj2 = open("courses.csv")
d1=csv.DictReader(fObj1)
d2=csv.DictReader(fObj2)


    #Q: What can you print here to make each line show only
    #   a name and its ID?
    #   eg,
    #   sasha, 3

q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query

for key in d1:
    field1 = key['name']
    field2 = key['id']
    q = "INSERT INTO students VALUES('" + field1 + "','" +field2 + "');"
    c.execute(q)


q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)

for key in d2:
    field1 = key['code']
    field2 = key['id']
    field3 = key['mark']
    q = "INSERT INTO courses VALUES('" + field1 + "','" + field2 + "','" + field3 + "');" 
    c.execute(q)

#==========================================================
db.commit() #save changes
db.close()  #close database


