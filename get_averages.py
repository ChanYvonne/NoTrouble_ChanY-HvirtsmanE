import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f = "discobandit.db"

db = sqlite3.connect(f)
cur = db.cursor()
cmd = "SELECT name, mark FROM students,courses WHERE students.id = courses.id"
cur.execute(cmd)
sel = cur.execute(cmd)

int sum = 0
int amt = 0
for record in sel:
    if students.id == courses.id:
        sum += record['mark']
        amt += 1
    
