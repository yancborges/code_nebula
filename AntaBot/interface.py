import methods
import tweepy
import threading
import terminal

def act(cmd):
    if(cmd == "/boot"):
        global api
        api = methods.boot()
        if(isItBooted() == True):
            print("Conexão pronta.")
        else:
            print("Erro ao abrir conexão.")
            
    elif(cmd == "/search"):
        if(isItBooted() == True):
            text = input("Pesquisar por: ")
            methods.search(text, api)
            print("Busca concluída.")
        else:
            print( "Erro. A conexão precisa ser iniciada primeiro (/boot)")
            
    elif(cmd == "/post"):
        if(isItBooted() == True):
            text = input("Mensagem: ")
            methods.post(text, api)
            print("Tweet enviado!")
        else:
            print( "Erro. A conexão precisa ser iniciada primeiro (/boot)")
            
    elif(cmd == "/like"):
        if(isItBooted() == True):
            twid = input("ID: ")
            methods.like(twid, api)
            print("Tweet curtido")
        else:
            print( "Erro. A conexão precisa ser iniciada primeiro (/boot)")
            
    elif(cmd == "/message"):
        if(isItBooted() == True):
            uid = input("Id do usuário: ")
            text = input("Mensagem: ")
            methods.message(uid,text,api)
            print("Mensagem enviada.")
        else:
            print( "Erro. A conexão precisa ser iniciada primeiro (/boot)")
            
    elif(cmd == "/start_analisys"):
        if(isItBooted() == True):
            print("Iniciando busca e analise de dados...")
            print("Aperte 'enter' para interromper a busca")
            print("")
            
            threads = []
            
            t = threading.Thread(target=methods.analysis, args=(api,))
            threads.append(t)
            t.start()
            #methods.analysis(api)
            
            #x = threading.Thread(target=input, args=("",))
            #threads.append(x)
            #x.start()
            
            #m = threading.Thread(target=terminal.open_terminal)
            ##threads.append(m)
            #m.start()
            
            x = input("")
            print("Busca interrompida pelo usuário")
            print("O fim da busca pode durar até 1 minuto..")
            
        else:
            print( "Erro. A conexão precisa ser iniciada primeiro (/boot)")
    
            
    elif(cmd == "/leave"):
        if(isItBooted() == True):
            methods.shutdown()
        return False
    else:
        print("Comando desconhecido, use /help para ajuda.")
    return True
        


def begin():

    api = None
    out = True
    
    print(" --- AntaBot Interface --- ")
    print(" Bem-vindo(a) ")
        
    while(out == True):
        print("Comandos: /boot /search /post /help /leave /like /message /start_analisys")
        cmd = input("Aguardando ordens: ")
        out = act(cmd)
        print("")
        
def isItBooted():
    if(api == None):
        return False
    return True
    
   
        
    
