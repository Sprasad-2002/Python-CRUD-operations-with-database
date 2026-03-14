import sqlite3
conobj=sqlite3.connect("mydb.db")
curobj=conobj.cursor()
curobj.execute(" update Students set sname='Bhosdiya' where sno=3")
conobj.commit()