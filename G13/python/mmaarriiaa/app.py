import mysql.connector

mydb = mysql.connector.connect(
  host="raspberrypi.local",
  user="matt",
  password="kikikiki",
  database="matt"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM survey")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)