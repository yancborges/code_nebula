import methods

class ply_play:
    
    # Atributtes
    def __init__(self, ply_id, ply_date, itm_id, usu_id, ist_id):
        self.ply_id = ply_id
        self.ply_date = ply_date
        self.itm_id = itm_id
        self.usu_id = usu_id
        self.ist_id = ist_id
    
    
    # Insert command
    def ply_insert(self):
    
        conn = methods.connect()
        
        query = ("INSERT INTO ply_play (ply_date, itm_id, usu_id) VALUES (curdate(),%s,%s);" )
        data_query = (self.itm_id, self.usu_id)
        
        methods.query(query, data_query)
        
        conn.close()
        
        return "1_8"
        
    
    # Getting all plays registered
    # User can filter it by Song, By instrument or both
    def ply_getAll(self):
        
        conn = methods.connect()
        cursor = conn.cursor()
        
        if(self.itm_id == '' and self.ist_id == ''):
            
            query = ("SELECT p.ply_id, p.ply_date, p.usu_id, i.ist_id, i.itm_state, i.itm_name, it.ist_name FROM ply_play p INNER JOIN itm_item i ON p.itm_id = i.itm_id INNER JOIN ist_instrument it ON i.ist_id = it.ist_id WHERE p.usu_id = '" + self.usu_id + "';") 
            cursor.execute(query)
        
        elif(self.ist_id == ''):
            
            query = ("SELECT p.ply_id, p.ply_date, p.usu_id, i.ist_id, i.itm_state, i.itm_name, it.ist_name FROM ply_play p INNER JOIN itm_item i ON p.itm_id = i.itm_id INNER JOIN ist_instrument it ON i.ist_id = it.ist_id  WHERE p.usu_id = %s AND i.itm_id = %s;") 
            data_query = (self.usu_id, self.itm_id)
            
            cursor.execute(query, data_query)
            
        elif(self.itm_id == ''):
            
            query = ("SELECT p.ply_id, p.ply_date, p.usu_id, i.ist_id, i.itm_state, i.itm_name, it.ist_name FROM ply_play p INNER JOIN itm_item i ON p.itm_id = i.itm_id INNER JOIN ist_instrument it ON i.ist_id = it.ist_id  WHERE p.usu_id = %s AND i.ist_id = %s;") 
            data_query = (self.usu_id, self.ist_id)
            
            cursor.execute(query, data_query)
            
        else:
            
            query = ("SELECT p.ply_id, p.ply_date, p.usu_id, i.ist_id, i.itm_state, i.itm_name, it.ist_name FROM ply_play p INNER JOIN itm_item i ON p.itm_id = i.itm_id INNER JOIN ist_instrument it ON i.ist_id = it.ist_id  WHERE p.usu_id = %s AND i.ist_id = %s AND i.itm_id = %s") 
            data_query = (self.usu_id, self.ist_id, self.itm_id)
            
            cursor.execute(query, data_query)
        
        table = []
        
        for i in cursor:
            table.append(i)
            
        cursor.close()
        conn.close()
            
        if(len(table) == 0):
            return "0_12"
        else:
            return table
        
    
