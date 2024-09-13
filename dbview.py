#!/usr/bin/env python3
print("Content-Type: text/html")
print()

import cgi
import mysql.connector

print("<h1>View the records</h1>")

form = cgi.FieldStorage()
find = form.getvalue("find")

con = mysql.connector.connect(user='root', password='', host='localhost', database='student')
cur = con.cursor()

cur.execute("SELECT * FROM student WHERE regno=%s", (find,))
student = cur.fetchone()  # Fetch one row

con.commit()
cur.close()
con.close()

if student:
    print(f"Name: {student[2]}, Email: {student[3]}")
else:
    print("No student found with the given registration number.")
