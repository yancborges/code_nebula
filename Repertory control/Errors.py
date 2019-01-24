#The Error messages will come as:

# Example: 0_32
# It means: 0<0 For error, 1 For success>_<split>32<ident of error, or succes>
# So: <0/1>_<Code>

# Spliting between error and success
def setMessage(text):
    if( text[0] == "0" ):
        return getError(text[2:])
    else:
        return getSuccess(text[2:])


# Gettting error's code message
def getError(ident):
    if(ident == '0'):
        return 'Something wont wrong.'
    elif(ident == '1'):
        return 'Unknown Error.'
    elif(ident == '2'):
        return 'Login or Password incorrect.'
    elif(ident == '3'):
        return 'Username already registered'
    elif(ident == '4'):
        return 'Email already registerd'
    elif(ident == '5'):
        return 'User not found'
    elif(ident == '6'):
        return 'You must be logged to use this command'
    elif(ident == '7'):
        return 'You do not have permission to use this command'
    elif(ident == '8'):
        return 'Session is already created.'
    elif(ident == '9'):
        return 'There is no session actived'
    elif(ident == '10'):
        return 'Instrument not found'
    elif(ident == '11'):
        return 'Item not found'
    elif(ident == '12'):
        return 'No plays were found'
            
# Getting success' code message
def getSuccess(ident):
    if(ident == '0'):
        return 'It works!'
    elif(ident == '1'):
        return 'Logged Succefully!'
    elif(ident == '2'):
        return 'Registered Succefully!'
    elif(ident == '3'):
        return 'Instrument registered succefully'
    elif(ident == '4'):
        return 'Session created sucefully'
    elif(ident == '5'):
        return 'Session closed sucefully'
    elif(ident == '6'):
        return 'Logged out sucefully'
    elif(ident == '7'):
        return 'Item added succefully'
    elif(ident == '8'):
        return 'Play registered succefully'
            
