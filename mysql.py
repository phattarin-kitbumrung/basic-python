import mysql.connector

mydb = mysql.connector.connect(
  host="db-dev",
  user="dev",
  passwd="xxxx"
)

print(mydb) 