import sqlite3
import os
from time import sleep

# connecting to the database
connection = sqlite3.connect("Topics.db")

# cursor
cursor = connection.cursor()

# SQL command to create a table in the database
try:
	sql_command = """CREATE TABLE Topics (
	Topics_number INTEGER PRIMARY KEY,
	Topics_data TEXT);"""

	# execute the statement
	cursor.execute(sql_command)

except:
	pass




def publish_topic(Topics_number, Topics_data):
	
	
	cursor.execute("SELECT Topics_number FROM Topics WHERE Topics_number=?", (Topics_number,))
	data = cursor.fetchall()
	try:
		if data[0][0] == Topics_number:
		
			cursor.execute("UPDATE Topics SET Topics_data = ? WHERE Topics_number = ?",(Topics_data, Topics_number))	
			connection.commit()
			return Topics_data

	except:
		try:
			cursor.execute("""INSERT INTO Topics(Topics_number, Topics_data) VALUES (?,?)""", (Topics_number, Topics_data))
			connection.commit()
			return Topics_data
			
		except:
			pass




def subscribe_topic(Topics_number):

  
	try:
		    
    		cursor.execute("SELECT Topics_data FROM Topics WHERE Topics_number=?", (Topics_number,))
    		data = cursor.fetchall()
    		print(data[0][0])
    		return data[0][0]


	except:
		pass
	


	
	

def free_memory(Topics_number):
	
	# close the connection and delete the database
	cursor.execute("DELETE FROM Topics WHERE Topics_number = ?" , (Topics_number,))
	connection.commit()
	
	cursor.execute("SELECT Topics_number FROM Topics")
	data = cursor.fetchall()
	if len(data) == 0:
		
		connection.close()
		os.remove("Topics.db") 




