import sqlite3
conobj=sqlite3.connect("mydb.db")
curobj=conobj.cursor()
records=curobj.execute(" select * from Students")
for record in records:
    print(record)
