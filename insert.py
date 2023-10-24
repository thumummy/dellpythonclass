import sqlite3

conn =sqlite3.connect("example.db")
print("opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(1,'EMOBILIS',7,'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(2,'SAFARICOM',7,'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(4,'SAFARICOM',7,'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(5,'SAFARICOM',7,'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(6,'SAFARICOM',7,'WESTLANDS',25000.00)");



conn.commit()
print("records created successfuly")
conn.close()