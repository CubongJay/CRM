import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Ubong@1997',
    auth_plugin='mysql_native_password'


)

# Prepare a cursor object
cursorObject = database.cursor()


# Create a database
cursorObject.execute("CREATE DATABASE Alynes")

print("All Done")
