import mysql.connector

class bridge:
    
    config = {
        'user':'root',
        'password':'',
        'host': '127.0.0.1',
        'database':'anime_db',
        'raise_on_warnings': True,
    }

    
    #Db connection cmd
    #returns a connection object
    def connect(self):

        try:
            connection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if( err.errno == errorcode.ER_ACESS_DENIED_ERROR):
                print('Access denied, sorry :(')
            else:
                print(err)
        else:
            #print('Connected!')
            return connection
     
    def query(self, sql_query):
        
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql_uery)
        conn.commit()
        print("Salvo!")
        conn.close() 
        
        
