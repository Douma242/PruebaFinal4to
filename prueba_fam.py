import sqlite3
don= sqlite3.connect('personas.db')

don.execute("INSERT INTO Familia VALUES(1,'Daniel')")
don.execute("INSERT INTO Familia VALUES(2,'Ana')")
don.execute("INSERT INTO Familia VALUES(3,'Josy')")
don.execute("INSERT INTO Familia VALUES(4,'Fernando')")

don.commit()

don.close()