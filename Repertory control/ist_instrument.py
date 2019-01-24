import methods

class ist_instrument:
    
    # Class atributtes
    def __init__ (self, ist_name, ist_id):
        self.ist_name = ist_name
        self.ist_id = ist_id
    
    # Inserting command
    def ist_insert( self ):
        
        conn = methods.connect()
        
        query = ("INSERT INTO ist_instrument (ist_name) VALUES ('" + self.ist_name + "');" )
        methods.query(query, self.ist_name)
        
        conn.close()
        
        return "1_3"
        
    # Getting the instrument data (only 1 at once)    
    def ist_get(self, ist_id, op):
        
        # OP means the method of searching
        # 0 For user Id selection
        # 1 For user name selection
        
        if( op == 0 ):
            query = ("SELECT * FROM ist_instrument WHERE ist_id = '" + str(ist_id) + "';")
        else:
            query = ("SELECT * FROM ist_instrument WHERE ist_name = '" + str(ist_id) + "';")
            
        conn = methods.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        
        table = []
        
        for i in cursor:
            table.append(i)
            
        cursor.close()
        conn.close()
            
        if(len(table) < 1):
            return "0_10"
        else:
            self.ist_name = table[0][1]
            self.ist_id = table[0][0]
            return "1_0"
            
       
        
    # Returns a list of objects with all rows found on DB    
    def ist_getAll(self):
        
        query = ("SELECT * FROM ist_instrument")
        conn = methods.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        
        table = []
        
        for i in cursor:
            new_ist = ist_instrument(i[1],i[0])
            table.append(new_ist)
        
        cursor.close()
        conn.close()
        
        return table
        
        
        
        
