import sqlite3

conn =sqlite3.connect("example.db")
print("opened database successfully")

conn.execute("UPDATE COMPANY1 set salary=100000 where id = 1")

cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY FROM COMPANY1")

for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("age=",row[2])
    print("address=",row[3])
    print("salary=",row[4])

print("operation done successfully")
conn.close()