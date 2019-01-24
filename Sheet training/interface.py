import random



def main():
    while( True ):
        x = input("Train what (help for.. well, you know): ")
        if( x == "scale" ):
            scale()
        elif( x == "time" ):
            time()
        elif( x == "both" ):
            both()
        elif( x == "help" ):
            print("soon, soon.")
        elif( x == "exit" ):
            break
    
def scale():
    x = int(input("Times: "))
    score = 0
    notes = ["Do","Re","Mi","Fa","Sol","La","Si"]
    for i in range(x):
        print("=== %d of %d ===" %(i,x))
        updown = random.randint(0,1)
        wnote = random.randint(0,len(notes)-1)
        if( updown == 1 ):
            nnote = wnote - 1
            if( nnote < 0 ):
                nnote = len(notes)-1
            aws = input( "%s _ : " %(notes[nnote]))
        else:
            nnote = wnote + 1
            if( nnote >= len(notes)):
                nnote = 0
            aws = input( "_ %s : " %(notes[nnote]))
        if( aws == notes[wnote] ):
            score += 1
            print( "Right!" )
        else:
            print( "Wrong (%s)." %(notes[wnote]) )
    print( "=== Training Ended ===" )
    print( "Score: %d/%d" %(score, x))
    
    
main()
    
    

