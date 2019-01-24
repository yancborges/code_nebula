class itm_item:
    
    def __init__(self, itm_id, sec_section_sec_id, itm_name, itm_origin, itm_desc):
        self.itm_id = itm_id
        self.sec_section_sec_id = sec_section_sec_id
        self.itm_name = itm_name
        self.itm_origin = itm_origin
        self.itm_desc = itm_desc

    def itm_insert(self, conn):
        
        try:
        
            
            # Setting the query for DB
            query = ("INSERT INTO itm_item (sec_section_sec_id, itm_name, itm_origin, itm_desc) VALUES (%s,%s,%s,%s);" )
            data_query = (self.sec_section_sec_id,self.itm_name,self.itm_origin,self.itm_desc)
            
            cursor = conn.cursor()
            cursor.execute(query,data_query)
            conn.commit()
            
            return True
        
        except:
            return False
            
    def itm_getAll(self, conn):
        
        query = ("SELECT * FROM itm_item")
            
        cursor = conn.cursor()
        cursor.execute(query)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
            
        return table
        
    def itm_get(self, conn):
        
        query = ("SELECT * FROM itm_item WHERE itm_id = %s")
            
        cursor = conn.cursor()
        cursor.execute(query,self.sec_id)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
            
        return table
