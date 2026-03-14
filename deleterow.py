import sqlite3
conobj=sqlite3.connect("mydb.db")
curobj=conobj.cursor()
curobj.execute(" delete from Students where sno=3")
conobj.commit()