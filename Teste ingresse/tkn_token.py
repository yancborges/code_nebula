import secrets

class tkn_token:
    
    def __init__(self, tkn_id, tkn_hash, usu_user_usu_id, tkn_status):
        self.tkn_id = tkn_id
        self.tkn_hash = tkn_hash
        self.usu_user_usu_id = usu_user_usu_id
        self.tkn_status = tkn_status
    
    def tkn_get(self, conn):
        
        # Setting SQL query
        query = ("SELECT tkn_id, usu_user_usu_id, tkn_status FROM tkn_token WHERE tkn_hash = %s AND usu_user_usu_id = %s AND tkn_status = 1")
        data_query = (self.tkn_hash,self.usu_user_usu_id)
            
        cursor = conn.cursor()
        cursor.execute(query,data_query)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
    
        # List -> Object
        if(len(table) > 0):
            self.usu_user_usu_id = table[0][1]
            self.tkn_id = table[0][0]
            return True
        return False
    
    # Token creation
    def tkn_generate(self, conn):
        
        # If the user gets a new token, we must deactive all other it has
        try:
            query = ("UPDATE tkn_token SET tkn_status = %s WHERE usu_user_usu_id = %s" )
            data_query = (0,self.usu_user_usu_id)
            
            cursor = conn.cursor()
            cursor.execute(query, data_query)
            conn.commit()
            cursor.close()
            
            # Each token must be unique, so we have to check if the new one is not a duplicate
            while(True):
        
                # Generate a random string in hexadecimal
                self.tkn_hash = str(secrets.token_hex(16))
                
                query = ("SELECT tkn_id FROM tkn_token WHERE tkn_hash = '%s'")
                    
                cursor = conn.cursor()
                cursor.execute(query,self.tkn_hash)
                
                # List for storing all the data found
                table = []
                
                # Cursor -> List
                for i in cursor:
                    table.append(i)
            
                cursor.close()
                if(len(table) < 1 ):
                    break
        
            # If the new token is REALLY new, we can insert it
            
            # Setting the query for DB
            query = ("INSERT INTO tkn_token (tkn_hash,usu_user_usu_id,tkn_status) VALUES (%s,%s,%s);" )
            data_query = (self.tkn_hash, self.usu_user_usu_id, self.tkn_status)
            
            cursor = conn.cursor()
            cursor.execute(query, data_query)
            conn.commit()
            cursor.close()
                
            return True
                
        except:
            return False
        
        
        
