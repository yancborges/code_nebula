import mysql.connector
from bridge_sql import bridge

#Defining the user class
#Contains the user db insert and its objects

class usu_user:
	
	#Instancing
	def __init__( self, usu_name, usu_password, usu_accountCreationDate ):
		self.usu_name = usu_name
		self.usu_password = usu_password
		self.usu_accountCreationDate = usu_accountCreationDate
	
	#Creating user insert query and executing it
	def usu_insert(self):
		query = "INSERT INTO usu_user (usu_name, usu_password, usu_accountCreationDate) VALUES ('%s', '%s', '%s');" %(self.usu_name, self.usu_password, self.usu_accountCreationDate)
		bridge.query(query)
    
    

