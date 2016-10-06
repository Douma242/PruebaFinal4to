import sqlite3
don= sqlite3.connect('personas.db')

resultados= don.execute("SELECT * FROM Persona")
for resultado in resultados:
	print (resultado)	

don.commit()

don.close()
