class twt_tweet:
    
    def __init__(self, twt_id, usr_id, twt_text, twt_source, twt_liked):
        self.twt_id = twt_id
        self.usr_id = usr_id
        self.twt_text = twt_text
        self.twt_source = twt_source
        self.twt_liked = twt_liked
        
    def twt_insert(self, conn):
        
        try:
            query = ("INSERT INTO twt_tweet (twt_id, usr_id, twt_text, twt_source,twt_liked) VALUES (%s,%s,%s,%s,%s);" )
            data_query = (self.twt_id, self.usr_id, self.twt_text, self.twt_source, self.twt_liked)
            
            cursor = conn.cursor()
            cursor.execute(query, data_query)
            conn.commit()
            return True
        except:
            return False
            
    def twt_getAll(self, conn):
        
        query = ("SELECT * FROM twt_tweet WHERE twt_liked = 0")
            
        cursor = conn.cursor()
        cursor.execute(query)
        
        table = []
        
        for i in cursor:
            table.append(i)
            
        cursor.close()
        conn.close()
            
        return table  
        
    def twt_update(self, conn):
        
        try:
            query = ("UPDATE twt_tweet SET twt_liked = %s;" )
            data_query = self.twt_liked
            
            cursor = conn.cursor()
            cursor.execute(query, data_query)
            conn.commit()
            return True
        except:
            return False
        
        
            
        
