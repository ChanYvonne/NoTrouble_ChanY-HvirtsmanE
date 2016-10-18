import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

q = "CREATE TABLE students (name TEXT, id INTEGER, average INTEGER)"

c.execute(q)    #run SQL query

for key in d1:
    field1 = key['name']
    field2 = key['id']
    field3 = key['average']
    q = "INSERT INTO students VALUES('" + field1 + "','" +field2 + "','"+ field3+ "');"
    c.execute(q)

db = sqlite3.connect(“discobandit.db”)
cur = db.cursor()
cmd = “SELECT mark FROM students,courses WHERE students.id = courses.id”
cur.execute(cmd)
sel = cur.execute(cmd)
for record in sel:
	print record
