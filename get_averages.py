import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f = "discobandit.db"

db = sqlite3.connect(f)
cur = db.cursor()
cmd = "SELECT name, mark, students.id FROM students,courses WHERE students.id = courses.id"
cur.execute(cmd)
sel = cur.execute(cmd).fetchall()

sum = 0
amt = 0.0
name = sel[0][0]
id = sel[0][2]
for record in sel:
    if record[0] == name:
        sum += record[1]
        amt += 1
    else:
        avg = sum/amt
        print name + ", " + str(id) + ", " + str(avg)
        name = record[0]
        id = record[2]
        sum = record[1]
        amt = 1.0
avg = sum/amt
print name + ", " + str(id) + ", " + str(avg)

