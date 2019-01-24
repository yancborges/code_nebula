import mysql.connector


def connect():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='twitter_api')
    except mysql.connector.Error as err:
        print("Erro ao conectar:")
        print(err)
    else:
        return cnx


def query(sql_query, parameters):
        
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql_query, parameters)
    conn.commit()
    conn.close() 

    
