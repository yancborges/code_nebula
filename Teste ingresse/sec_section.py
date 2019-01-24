class sec_section:
    
    def __init__(self, sec_id, sec_name):
        self.sec_id = sec_id
        self.sec_name = sec_name

    def sec_insert(self, conn):
        
        try:
            
            # Setting the query for DB
            query = ("INSERT INTO sec_section (sec_name) VALUES ('" + self.sec_name + "');" )
            
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            
            return True
        
        except:
            return False
            
    def sec_getAll(self, conn):
        
        query = ("SELECT * FROM sec_section")
            
        cursor = conn.cursor()
        cursor.execute(query)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
            
        return table
        
    def sec_get(self, conn):
        
        query = ("SELECT * FROM sec_section WHERE sec_id = %s")
            
        cursor = conn.cursor()
        cursor.execute(query,self.sec_id)
        
        # List for storing all the data found
        table = []
        
        # Cursor -> List
        for i in cursor:
            table.append(i)
            
        cursor.close()
            
        return table
