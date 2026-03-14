import sqlite3
conobj=sqlite3.connect("mydb.db")
curobj=conobj.cursor()
curobj.execute(" insert into Students values(1,'ab')")
curobj.execute(" insert into Students values(2,'cd')")
curobj.execute(" insert into Students values(3,'ef')")
conobj.commit()