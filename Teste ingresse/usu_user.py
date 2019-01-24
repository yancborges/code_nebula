class usu_user:
    
    # Initializing the object
    def __init__(self, usu_id, usu_name, usu_password):
        self.usu_id = usu_id
        self.usu_name = usu_name
        self.usu_password = usu_password
        
    # Inserting into DB
    def usu_insert(self, conn):
        
        try:
            
            # Setting the query for DB
            query = ("INSERT INTO usu_user (usu_name, usu_password) VALUES (%s,%s);" )
            data_query = (self.usu_name, self.usu_password)
            
            cursor = conn.cursor()
            cursor.execute(query, data_query)
            conn.commit()
            
            return True
        
        except:
            return False
            
    # Retrieving data of all users
    def usu_getAll(self, conn):
        
        query = ("SELECT * FROM usu_user")
            
        cursor = conn.cursor()
        cursor.execute(query)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
            
        return table
        
    # Getting data from an user by its ID
    def usu_get(self, conn):
        
        query = ("SELECT * FROM usu_user WHERE usu_id = %s")
        data_query = (self.usu_id)
            
        cursor = conn.cursor()
        cursor.execute(query, data_query)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
            
        if(len(table) < 1):
            return False
        else:
            self.usu_name = table[0][1]
            self.usu_password = table[0][2]
            return True
            
    def usu_login(self,conn):
        
        query = ("SELECT * FROM usu_user WHERE usu_id = %s AND usu_password - %s")
        data_query = (self.usu_id,self.usu_password)
            
        cursor = conn.cursor()
        cursor.execute(query)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
            
        if(len(table) < 1):
            return False
        else:
            return True

        
