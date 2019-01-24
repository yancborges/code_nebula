import json
import dbMethods
from usu_user import usu_user
from tkn_token import tkn_token
from sec_section import sec_section
from itm_item import itm_item

# Test step: Reading local .json files for requisitions
print("Reading request...")
arq_json = open('request.json', 'r')
dados = json.load(arq_json)

#Spliting credentials and request data
x = dados["credentials"]
y = dados["request"]

print("* Validating...")

# Creating connection
conn = dbMethods.boot()

# Creating tkn_token objetc for validate the token recieved at .json file
tkn_current = tkn_token('', x[0]["token"], x[0]["id"],'')

if( tkn_current.tkn_get(conn) == False ):
    print( "Access denied, invalid credentials" )
else:
    print( "Acess granted!")
    
    # Reading request parameters
    print("* Working on request...")
    
    # Insertion
    if( y[0]["sog"] == "insert" ):
        
        # User insert
        if(y[0]["item"] == "user"):
            usu_new = usu_user('',y[0]["info"][0]["name"],y[0]["info"][0]["password"])
            if( usu_new.usu_insert(conn) == False ):
                print( "Error trying to insert new user." )
            else:
                print( "User created succefully!" )
        
        # Token insert
        elif(y[0]["item"] == "token"):
            tkn_new = tkn_token('','',y[0]["info"][0]["id"],1)
            if(tkn_new.tkn_generate(conn) == False ):
                print( "Error generating new token." )
            else:
                print( "New token generated: %s" %tkn_new.tkn_hash)
        
        # Section insert
        elif(y[0]["item"] == "section"):
            sec_new = sec_section('',y[0]["info"][0]["name"])
            if(sec_new.sec_insert(conn) == False):
                print( "Error inserting new section")
            else:
                print( "Section created succefully!" )
                
        elif(y[0]["item"] == "item"):
            itm_new = itm_item('',y[0]["info"][0]["section"],y[0]["info"][0]["name"],y[0]["info"][0]["origin"],y[0]["info"][0]["desc"])
            if(itm_new.itm_insert(conn) == False):
                print( "Error inserting new item" )
            else:
                print( "Item created succefully!" )
    
    # Getting
    elif( y[0]["sog"] == "get" ):
        
        # Section get
        if(y[0]["item"] == "section"):
            
            # Checks if 1 section or all of them for being selected
            # All
            if(y[0]["info"][0]["id"] == -1):
                sec_all = sec_section('','')
                l = sec_all.sec_getAll(conn)
                print(l)
            
            # One
            else:
                sec_all = sec_section(y[0]["info"][0]["id"],'')
                l = sec_all.sec_get(conn)
                print(l)
        
        # Item get
        elif(y[0]["item"] == "item"):
            
            # Checks if 1 item or all of them for being selected
            # All
            if(y[0]["info"][0]["id"] == -1):
                itm_all = itm_item('','','','','')
                l = itm_all.itm_getAll(conn)
                print(l)
            
            # One
            else:
                sec_all = sec_section(y[0]["info"][0]["id"],'')
                l = sec_all.sec_get(conn)
                print(l)
            
    
    



    

