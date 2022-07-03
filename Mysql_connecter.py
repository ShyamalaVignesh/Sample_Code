
#Need to install (pip install mysql-connector)
# create connection object
import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="shyamala")

# create cursor object
cursor = con.cursor()

# assign data query
query1 = "insert into employee values(102,'Shyam',200000)"

# executing cursor
cursor.execute(query1)
con.commit()
cursor.close()
# display all records
# table = cursor.fetchall()
# print(table)