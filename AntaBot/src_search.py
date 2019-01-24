import dbMethods

class src_search:
    
    def __init__(self, src_id, src_source, src_parameter):
        self.src_id = src_id
        self.src_source = src_source
        self.src_parameter = src_parameter
        
        
    def src_insert(self):
        try:
            query = ("INSERT INTO src_search (src_sourc, src_parameter) VALUES (%s, %s);" )
            data_query = (self.src_source, self.src_parameter)
            dbMethods.query(query, data_query)
            return True
        except:
            return False
        
