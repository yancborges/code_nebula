import methods

class usu_user:

    # Class atributtes
    def __init__( self, usu_name, usu_password, usu_email, usu_status, usu_id ):
        self.usu_id = usu_id
        self.usu_name = usu_name
        self.usu_password = usu_password
        self.usu_email = usu_email
        self.usu_status = usu_status 
        
    # Inserting a new user on the db
    def usu_insert( self ):
        
        conn = methods.connect()
        
        # Verifying if the name is already taken
        query = ("SELECT usu_id FROM usu_user WHERE usu_name = '" + self.usu_name + "';")
        cursor = conn.cursor()
        cursor.execute(query)
        
        
        table = []

        for usu_name in cursor:
            table.append(usu_name)
        
        if( len(table) > 0 ):
            return "0_3"
        else:
            
            table.clear()
            
            # Verifying if the email is already taken
            query = ("SELECT usu_email FROM usu_user WHERE usu_email = '" + self.usu_email + "';")
            cursor = conn.cursor()
            cursor.execute(query)
            
            
            table = []

            for usu_name in cursor:
                table.append(usu_name)
        
                
            if( len(table) > 0 ):
                return "0_4"
            else:
        
                #Then, the data is stored
                query = ("INSERT INTO usu_user (usu_name, usu_password, usu_email, usu_status) VALUES (%s,%s,%s,%s);" )
                data_query = (self.usu_name, self.usu_password, self.usu_email, self.usu_status)
                methods.query(query, data_query)
                
                return "1_2"
        
        cursor.close()
        conn.close()
        
    #Logs in existing account
    def usu_login(usu_name, usu_password):
        
        #Verifying redentials on the DB
        query = ("SELECT usu_id FROM usu_user WHERE usu_name = %s AND usu_password = %s;")
        data_query = (usu_name, usu_password)
        
        conn = methods.connect()
        
        cursor = conn.cursor()
        cursor.execute(query, data_query)
        
        table = []
        
        #Appends all the results (only user ids) in this list
        for usu_id in cursor:
            table.append(usu_id)
        
        #Returns the error code
        if( len(table) <= 0 ):
            return "0_2"
        else:
            return "1_1"
            
        cursor.close()
        conn.close()
        
    # Collecting data from the DB with an user ID
    def usu_get( self, usu_id, op ):
        
        # OP means the method of searching
        # 0 For user Id selection
        # 1 For user name selection
        
        if( op == 0 ):
            query = ("SELECT usu_id, usu_email, usu_name, usu_status FROM usu_user WHERE usu_id = '" + str(usu_id) + "';")
        else:
            query = ("SELECT usu_id, usu_email, usu_name, usu_status FROM usu_user WHERE usu_name = '" + str(usu_id) + "';")
            
        conn = methods.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        
        table = []
        
        for i in cursor:
            table.append(i)
            
        if(len(table) < 1):
            return "0_5"
        else:
            self.usu_name = table[0][2]
            self.usu_email = table[0][1]
            self.usu_id = table[0][0]
            self.usu_status = table[0][3]
            return "1_0"
            
        cursor.close()
        conn.close()
        

            
