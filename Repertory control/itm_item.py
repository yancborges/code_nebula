import methods

class itm_item:
    
    # Object inicialization
    def __init__( self, itm_id, usu_id, ist_id, itm_state, itm_name ):
        self.itm_id = itm_id
        self.usu_id = usu_id
        self.ist_id = ist_id
        self.itm_state = itm_state
        self.itm_name = itm_name
        
    # Item insert
    def itm_insert(self):
        
        conn = methods.connect()
        
        query = ("INSERT INTO itm_item (usu_id, ist_id, itm_state, itm_name) VALUES (%s,%s,%s,%s);" )
        data_query = (self.usu_id, self.ist_id, self.itm_state, self.itm_name)
        
        methods.query(query, data_query)
        
        conn.close()
        
        return "1_7"
        
    # Getting the item data (only 1 at once)    
    def itm_get(self, itm_id, op):
        
        # OP means the method of searching
        # 0 For user Id selection
        # 1 For user name selection
        
        if( op == 0 ):
            query = ("SELECT * FROM itm_item WHERE itm_id = '" + str(itm_id) + "';")
        else:
            query = ("SELECT * FROM itm_item WHERE itm_name = '" + str(itm_id) + "';")
            
        conn = methods.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        
        table = []
        
        for i in cursor:
            table.append(i)
            
        cursor.close()
        conn.close()
            
        if(len(table) < 1):
            return "0_11"
        else:
            self.itm_name = table[0][1]
            self.itm_id = table[0][0]
            return "1_0"
            
       
        
    # Returns a list of objects with all rows found on DB    
    def itm_getAll(self):
        
        query = ("SELECT * FROM itm_item")
        conn = methods.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        
        table = []
        
        for i in cursor:
            new_itm = itm_item(i[0],i[1],i[2],i[3],i[4])
            table.append(new_itm)
        
        cursor.close()
        conn.close()
        
        return table
        
        
        
        

