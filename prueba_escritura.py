import sqlite3
don= sqlite3.connect('personas.db')

don.execute("INSERT INTO Persona VALUES(1, 6, 'Daniel', 'Douma', 16)")
don.execute("INSERT INTO Persona VALUES(2, 7,'Ana', 'Rivas', 42)")
don.execute("INSERT INTO Persona VALUES(3, 8,'Josy', 'Douma', 21)")
don.execute("INSERT INTO Persona VALUES(4, 9,'Fernando', 'Rivas', 73)")

don.commit()

don.close()