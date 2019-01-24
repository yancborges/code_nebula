import mysql.connector


#Connect the code into the DB
def connect():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='rep_control')
    except mysql.connector.Error as err:
        print("Erro ao conectar:")
        print(err)
    else:
        return cnx

    
#Standart Query, insert only (for now)
def query(sql_query, parameters):
        
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql_query, parameters)
    conn.commit()
    conn.close() 
    

