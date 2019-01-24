from usu_user import usu_user
from ist_instrument import ist_instrument
from itm_item import itm_item
from ply_play import ply_play
import Errors
import Session
import datetime

# Login function
# If theres someone logged in, this command will be a logout function
def usu_login():
    if(Session.sessionExists() == True):
        Session.closeSession()
        print(Errors.setMessage("1_6"))
    else:
        print( "=== Login ===" )
        usu_name = input("user: " )
        usu_password = input("password: ")
        login_response = usu_user.usu_login(usu_name,usu_password)
        print(Errors.setMessage(login_response))
        log_user = usu_user('','','','','')
        x = log_user.usu_get(usu_name, 1)
        
        if(x == "1_0"):
            Session.createSession(log_user)
        else:
            print(Errors.setMessage("0_0"))
    
# User register function
def usu_register():
    print( "=== Account creation ===" )
    usu_name = input("User: ")
    usu_password = input("Password: ")
    usu_email = input("Email: ")
    new_user = usu_user(usu_name, usu_password, usu_email,1,'')
    insert_response = usu_user.usu_insert(new_user)
    print(Errors.setMessage(insert_response))
    
# Instrument register function    
def ist_register():
    print( "=== Instrument registration ===" )
    ist_name = input("Instrument name: ")
    new_instrument = ist_instrument(ist_name,'')
    insert_response = new_instrument.ist_insert()
    print(Errors.setMessage(insert_response))
    
# Getting user data from DB    
def usu_get():
    print( "=== View user info ===" )
    usu_id = input( "Input username: " )
    get_user = usu_user('','','','','')
    response_user = get_user.usu_get(usu_id, 1)
    if(response_user == "0_5"):
        print(Errors.setMessage(response_user))
    else:
        print( "   --- User info ---   ")
        print( "   Name: " + get_user.usu_name )
        print( "   ID: " + str(get_user.usu_id) )
        print( "   Number of plays: soon" )
        
# Getting instrument data from DB    
def ist_get():
    print( "=== Search instrument ===" )
    print( " - - - Under maintenance - - - " )
    # This command is weird,
    # Only relevant info is the ist_name
    # but the user must input the name for searching '-'
    
# Show all instruments from the list returned by the class method
def ist_getAll():
    print( '--- test ---' )
    x = ist_instrument('','')
    all_ist = x.ist_getAll()
    print( "[ID] - Name" )
    for i in all_ist:
        print("[%s] - %s" %(i.ist_id, i.ist_name))
    print( '--- end ---' )
    
# A little menu for code shorting
def itm_stateGet():
    print( '0 - Learning')
    print( '1 - Praticing' )
    x = 5
    while( x != 1 and x != 0 ):
        x = int(input("Select state: "))
    return x
    
# Collets some data from the user to intert it
def itm_insert():
    if(Session.sessionExists() == False):
        print(Errors.setMessage("0_6"))
    else:
        
        found = False
        while( found == False ):
            ist_id = input("Instrument (search by name/'exit' to cancel): ")
            if( ist_id != 'exit' ):
                x = ist_instrument( '', '' )
                ist_response = x.ist_get(ist_id, 1)
                if(ist_response != "1_0"):
                    print(Errors.setMessage(ist_response))
                else:
                    found = True
                    ist_id = x.ist_id
            else:
                break
        if( found == True ):
            itm_state = itm_stateGet()
            itm_name = input( "Input item's name: " )
            
            new_item = itm_item( '', Session.getSession().usu_id, ist_id, itm_state, itm_name )
            response = new_item.itm_insert()
            print(Errors.setMessage(response))
    

# Showing all user's saved items
def itm_showAll():
    x = itm_item('', Session.getSession().usu_id, '','','' )
    all_list = x.itm_getAll()
    print( "[ID] - Name" )
    for i in all_list:
        print("[%s] - %s" %(i.itm_id, i.itm_name))
    print( '--- end ---' )
    
    
# Registering a play, every time a song is played this command may be executed by the user
def ply_register():
    if(Session.sessionExists() == False):
        print(Errors.setMessage("0_6"))
    else:
        
        found = False
        while( found == False ):
            itm_id = input("Item (search by name/'exit' to cancel): ")
            if( itm_id != 'exit' ):
                x = itm_item('', Session.getSession().usu_id, '','','' )
                itm_response = x.itm_get(itm_id, 1)
                if(itm_response != "1_0"):
                    print(Errors.setMessage(itm_response))
                else:
                    found = True
                    itm_id = x.itm_id
            else:
                break
        if( found == True ):
            
            new_ply = ply_play('','',itm_id,Session.getSession().usu_id,'')
            response_ply = new_ply.ply_insert()
            print(Errors.setMessage(response_ply))
            

# Gets all plays registered
# User can filter it by Instrument, Song or Both
def ply_getAll():
    
    found = False
    while( found == False ):
        ist_id = input("Instrument (search by name/'exit' to cancel): ")
        if( ist_id != 'exit' ):
            x = ist_instrument( '', '' )
            ist_response = x.ist_get(ist_id, 1)
            if(ist_response != "1_0"):
                print(Errors.setMessage(ist_response))
            else:
                found = True
                ist_id = x.ist_id
        else:
            found = True
            ist_id = ''
        if( found == True ):
            
            foundB = False
            while( foundB == False ):
                itm_id = input("Item (search by name/'exit' to cancel): ")
                if( itm_id != 'exit' ):
                    x = itm_item('', Session.getSession().usu_id, '','','' )
                    itm_response = x.itm_get(itm_id, 1)
                    if(ist_response != "1_0"):
                        print(Errors.setMessage(itm_response))
                    else:
                        foundB = True
                        itm_id = x.itm_id
                else:
                    foundB = True
                    itm_id = ''
            if( found == True ):
                
                x = ply_play('','',itm_id,Session.getSession().usu_id,ist_id)
                table = x.ply_getAll()
                
                if( table == "0_12" ):
                    print(Errors.setMessage(table))
                else:
                    print( "Play date | Song name | Instrument" )
                    
                    count = 1
                    for i in table:
                        
                        #print( "#%s: {:%d %b %Y} | %s | %s" %(i[0],i[1],i[5],i[6]))
                        print( "#%s: %s | %s | %s" %(count,i[1],i[5],i[6]))
                        count += 1
                        
                    print( "--- end ---" )
                    
            
def song_remind():
    x = ply_play('','','',Session.getSession().usu_id, '')
    table = x.ply_getAll()
    
        
        
    
# Show all the avaliable commands
# Some commands require permission (status = 2) for being used
def showMenu(status):
    print( " ===== Pick your poison ====== ")
    print( "1 - Register" )
    if(Session.sessionExists() == True):
        print( "2 - Logout" )
    else:
        print( "2 - Login" )
    if(status == '2'):
        print( "3 - Register instrument" )
    print( "4 - Register song play" )
    print( "5 - View user info" )
    print( "6 - Search instrument" )
    print( "7 - See all instruments" )
    if(status == '2'):
        print( "8 - Promote user" )
    print( "9 - Add item" )
    print( "10 - Show all songs" )
    print( "11 - Show all plays" )
    print( "99 - Exit" )
    print( "---- More soon ----" )
    
# Gets user's input then execute it (if its logged and its allowed for)
def act():
    option = int(input("Option: "))
    if(option == 1):
        usu_register()
    elif(option == 2):
        usu_login()
    elif(option == 3):
        ist_register()
    elif(option == 4):
        ply_register()
    elif(option == 5):
        usu_get()
    elif(option == 6):
        ist_get()
    elif(option == 7):
        ist_getAll()
    elif(option == 8):
        print('nothing here.')
    elif(option == 9):
        itm_insert()
    elif(option == 10):
        itm_showAll()
    elif(option == 11):
        ply_getAll()
    elif(option == 99):
        return False
    return True
        

# Some greetings if session is off
if(Session.sessionExists() == False):
    print( "Welcome, for the 'Unamed 1.0 system!!!'" )
    print( "Developed, with love by: AntaLord" )
    print( "Special thanks to: My self, My mom, and everyone who doesnt care about me and makes me sad :(" )   
    print( "I hope you enjoy." )     
    print( "Make sure to Login before start using!" )
else:
    # if session is on...
    print( "Welcome back, " + Session.getSession().usu_name + "!" )


# Looping, after an action ends, the system will make possible the user choose another command withou
# restarting the code, selection the action number '99' the loop will break.
x = True
while(x == True):
    if(Session.sessionExists() == True):
        value = Session.getSession().usu_status
    else:
        value = 1
    showMenu(value)
    x = act()

    
    
    

