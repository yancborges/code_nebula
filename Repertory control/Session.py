from usu_user import usu_user

# This file will make the 'auto login' function,
# every time that an user id may be needed,
# this class will return witch user is logged in, and return its Id.

# Not only id, Storage var can be used for anything,
# Even other objects (inseption xD)

# It uses a temporary table in the DB
# Assosiating the id with an IP

# For now the data is saved in a txt file

# Saving the object formated
def createSession(storage):
    
    f  = open("Session.txt", 'r+')
    if(sessionExists() == False):
        # Format: status*usu_id*usu_name*usu_email*usu_status
        f.write("active*%s*%s*%s*%s" %(storage.usu_id, storage.usu_name, storage.usu_email,storage.usu_status) )
        f.close()
    
    else:
        text = f.read()
        x = text.split('*')
        if( x[0] == 'active' ):
            return '0_7'
        return '1_4'

# Brings the data from the file to the code
def getSession():
    if(sessionExists() == False):
        return "0_9"
    else:
        
        f = open("Session.txt", 'r')
        x = f.read()
        response = x.split('*')
        session_user = usu_user(response[2], '', response[3], response[4], response[1])
        return session_user
    
    
# Removes the saved information from the file, making it empty
def closeSession():
    
    if(sessionExists() == False):
        return "0_9"
    else:
        f = open("Session.txt", 'w')
        f.write('')
        f.close()
        return "1_5"

# Checking if there is something saved in the session    
def sessionExists():
    f = open("Session.txt", "r" )
    text = f.read()
        
    if(len(text) < 5):
        return False
    f.close()
    return True
    
