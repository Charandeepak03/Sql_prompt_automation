# pip install db-sqlite3
# pip install sqlite3
import sqlite3

#Connectt to SQlite
#Our database name: Naresh_it_student
connection=sqlite3.connect("Charan_sols.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

#create the table
#Our table name student
#Columns names are: name, course
table_info="""
Create table Charan_sols(employee_name varchar(30),
                    employee_role varchar(30),
                    employee_salary FLOAT);
"""
cursor.execute(table_info)

#Insert the records

cursor.execute('''Insert Into Charan_sols values('Omkar Nallagoni','Data Science',75000)''')
cursor.execute('''Insert Into Charan_sols values('vijay','Data Science',90000)''')
cursor.execute('''Insert Into Charan_sols values('Phani','Data Science',88000)''')
cursor.execute('''Insert Into Charan_sols values('Naga babu','Data Engineer',50000)''')
cursor.execute('''Insert Into Charan_sols values('Ajay','Data Engineer',35000)''')
cursor.execute('''Insert Into Charan_sols values('Pawan','Data Engineer',60000)''')

#Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from Charan_sols''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()  