import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)


    #Q: What can you print here to make each line show only
    #   a name and its ID?
    #   eg,
    #   sasha, 3

q = "CREATE TABLE students (name TEXT, id INTEGER)"

for key in d:
    ans = ""
    for name in key:
        if name == 'name':
            field1 = key[name]
        if name == 'id':
            field2 = key[name]
    q+= "INSERT INTO students VALUES(" + field1 +","+field2+");"


c.execute(q)    #run SQL query

'''
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
'''

#==========================================================
db.commit() #save changes
db.close()  #close database


