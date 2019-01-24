import mysql.connector

# Global var for the connection instance
gb_conn = None


# Sets the global var with the connection instance
def boot():
    try:
        global gb_conn
        gb_conn = connect()
        return gb_conn
    except:
        return None
        
def shutdown():
    global conn
    conn.close()
    conn = None
        
# Verifies if the connection was setted up
def isConnected():
    if(gb_conn == None):
        return False
    else:
        return True

# Creates the connection with the database
def connect():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='museumdb')
    except mysql.connector.Error as err:
        print("Unable to connect!")
        print(err)
    else:
        return cnx

# Sends a query to Database, used for creating request for the base (insert, select, etc)
def query(sql_query, parameters):
        
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql_query, parameters)
    conn.commit()
    conn.close() 
