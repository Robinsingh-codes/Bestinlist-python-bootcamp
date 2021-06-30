import os
import mysql
import mysql.connector

mydb=mysql.connector.connect(host='Local Host',
                             database='database',
                             user='root',
                             password="Harsha0201"
                            )
print(mydb)

import mysql.connector
mydb = mysql.connector.connect(
                               host="localhost",
                               database = "HarshaReddy",
                               user ="root",
                               password="Harsha0201"
)

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Employee1 ( EMP_name VARCHAR(255), EMP_no int , EMP_city VARCHAR(255), EMPdep VARCHAR(255))")
dbse.execute("INSERT INTO Employee ( EMP_name, EMP_no, EMP_city, EMPdep) VALUES  ('Harsha',27,'HYD','BI')")
mydb.commit()

dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)

dbse.execute("SELECT * FROM Employee")

for value in dbse:
    print(value)


import mysql.connector
mydb= mysql.connector.connect(host='Local host',
                              database='database',
                              user='root',
                              password='Harsha02041')

dbse=mydb.cursor()
dbse.excute("CREATE TABLE Employee (Emp_name HARSHA(27),Emp_no int,Emp_city HARSHA(27),Emp_dept HARSHA(27))")
dbse.excute("SHOW Tables")
for value in dbse:
    print(dbse)

    import mysql.connector
mydb= mysql.connector.connect(host='Local host',
                              database='database',
                              user='root',
                              password='Harsha02041')

dbse=mydb.cursor()
dbse.excute("CREATE TABLE Employee (Emp_name HARSHA(27),Emp_no int,Emp_city HARSHA(27),Emp_dept HARSHA(27))")
dbse.excute("SHOW Tables")
for value in dbse:
    print(dbse)    
