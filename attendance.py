import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kshitindra@123",
    database="attendance_system"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
