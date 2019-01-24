import base64
    
def Vigenere_decode(key):
    
    #Decoding function
    #Cipher info: https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re
    
    #Opening the source file
    
    f = open("Source.txt", "r" )
    step0 = str(f.read()).upper()
    f.close()
    
    std = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    step1 = ""
    key_count = 0
    
    for i in range(len(step0)):
        if(isLetter(step0[i])):
            start = std.index(key[key_count])
            end = std.index(step0[i])
            nindex = end - start + 26
            if(nindex >= len(std)):
                nindex = nindex-len(std)
            value = std[nindex]
        else:
            value = step0[i]
        step1 += value
        key_count += 1
        if(key_count >= len(key)):
            key_count = 0
    
    fn = open( "Result.txt", "w" )
    fn.write(step1)
    fn.close()
        

def Vigenere_encode(key):
    
    #Enconding function
    #Cipher info: https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re
    
    #Opening the source file
    
    f = open( "Source.txt", "r" )
    step0 = str(f.read()).upper()
    f.close()
    
    std = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    step1 = ""
    key_count = 0
    
    #The magic is here!
    
    for i in range(len(step0)):
        if(isLetter(step0[i])):
            start = std.index(step0[i])
            end = std.index(key[key_count])
            nindex = start+end
            if(nindex >= len(std)):
                nindex = nindex-len(std)
            value = std[nindex]
        else:
            value = step0[i]
        
        #step1.append(value)
        step1 += value
        key_count += 1
        if(key_count >= len(key)):
            key_count = 0
    
    fn = open( "Result.txt", "w" )
    fn.write(step1)
    fn.close()
    
    
    


def doSomeThing(cmd):
    if(cmd == "hideText"):
        Vigenere_encode(input("Input key: ").upper())
    elif(cmd == "showText"):
        Vigenere_decode(input("Input Key: ").upper())
    else:
        print("Unknown comand.")
    

def isLetter(text):
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    if(text in letters):
        return True
    else:
        return False

def main():
	
	#Main execution of the code
    doSomeThing(input("Command: "))
    
if __name__ == '__main__':
	main()
