# Create an Employee Table with employee name,employee ID & Salary

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="8421436728",
)

mycursor = mydb.cursor()
print(mydb)
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE employee_mangement")

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="8421436728",
  database="employee_mangement"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)

dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for value in dbse:
  print(value)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a query to get the maximum and minimum salary from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select max(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a query to get the number of employees working with the company
mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employee")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a query to get the first 3 characters of first name from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT * from employee WHERE EMP_NAME LIKE('ANU%')")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
