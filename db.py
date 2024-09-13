#!C:/Program Files/Python312/python.exe
print("Content-Type:text/html")
print()
import cgi

print("<h1>Welcome To Python</h1>")
print("<h1></h1>")
print("<h1>Using input</h1>")
print("<h1>Welcome To Python</h1>")

form=cgi.FieldStorage()

image=form.getvalue("file")
username=form.getvalue("username")
name=form.getvalue("name")
mail=form.getvalue("mail")
regno=form.getvalue("regno")
dob=form.getvalue("dob")
phoneno=form.getvalue("phoneno")
department=form.getvalue("department")
course=form.getvalue("course")

import mysql.connector

con=mysql.connector.connect(user='root',password='',host='localhost',database='student')
cur=con.cursor()

cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(image,username,name,mail,regno,dob,phoneno,department,course))

con.commit();

cur.close()
con.close()

print("<h3>record inserted sucessfully</h3>")
print("<a href='http://localhost/python/index.php'>cliclick here to go back)



