class usr_user:
    
    def __init__(self, usr_id, usr_name):
        self.usr_id = usr_id
        self.usr_name = usr_name
        
    def usr_insert(self, conn):
        try:
            
            query = ("INSERT INTO usr_user VALUES (%s,%s);" )
            data_query = (self.usr_id, self.usr_name)
            
            cursor = conn.cursor()
            cursor.execute(query, data_query)
            conn.commit()
            
            return True
        except:
            return False
