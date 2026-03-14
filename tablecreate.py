import sqlite3
conobj=sqlite3.connect("mydb.db")
curobj=conobj.cursor()
curobj.execute(" create table Students(sno number primary key ,sname varchar(10))")