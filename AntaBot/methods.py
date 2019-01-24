from usr_user import usr_user
from twt_tweet import twt_tweet
#import src_search
import dbMethods
import tweepy
from tweepy import OAuthHandler
import time
import ia
import datetime

conn = None

def dbBoot():
    global conn
    conn = dbMethods.connect()
    
def shutdown():
    global conn
    conn.close()
    conn = None

def boot():
    # Getting API data from local file
 
    f = open('C:\\Users\\Yan\\Desktop\\Scripting\\TWITTER_API_KEY.txt', 'r')
    api_key= f.readlines()
    f.close()

    # Setting the found data
 
    consumer_key = api_key[0][:-1]
    consumer_secret = api_key[1][:-1]
    access_token = api_key[2][:-1]
    access_secret = api_key[3]

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
 
    api = tweepy.API(auth)
    
    dbBoot()
    
    return api

def post(text, api):    
    
    api.update_status(text)
    
    
def search(text, api):

    search = api.search(q=text,lang="pt",include_entities="true")
    count = 0
    
    for x in search:
        try:
            if("RT" not in x.text):
                    
                usr_new = usr_user(x.user.id, x.user.screen_name)
                twt_new = twt_tweet(x.id, x.user.id, x.text, x.source, "0")
                        
                usr_bool = usr_new.usr_insert(conn)
                twt_bool = twt_new.twt_insert(conn)
                
                if(usr_bool == True and twt_bool == True):
                    count += 1
                else:
                    print("Erro ao inserir um tweet.")
            
        except:
            print("Erro: Não foi possivel abrir um tweet.")
            
    print("Total de entradas encontradas: %d" %count)
    
def message(uid, mtext, api):
    try:
        api.send_direct_message(user_id=uid,text=mtext)
    except:
        print("Erro. Só se pode mandar mensagens ao seus seguidores.")
        
running = False
next_time = None

def analysis(api):
    global running
    running = True
    global next_time
    next_time = 60
    odd = 0
    layout()
    while(running == True):
        if(next_time/6 == int(next_time/6)):
            print("*", end="", flush=True)
        if(next_time == 0):
            print("]Completo!")
            if(odd%2 == 0):
                text = "estou sentindo sozinho"
            else:
                text = "estou sentindo sozinha"
            print("Realizando busca...")
            search(text, api)
            print("Analizando dados encontrados...")
            verify()
            odd += 1
            next_time = 60
            layout()
        else:
            next_time -= 1
            
        time.sleep(60)
        
def like(twid, api):
    api.create_favorite(twid)
        
def verify():
    count = 0
    table = twt_tweet("", "", "", "", "").twt_getAll(conn)
    for i in table:
        x = ia.avaliate(i[2])
        value = 99
        if(x >= 2):
            like(i[0],api)
            value = 1
            count += 1
        else:
            value = 2
        c = twt_tweet(i[0], "0", "0", "0", value)
        c.twt_update(conn)
    print("Análise completa, %s tweets curtidos." %count)
            
        

def layout():
    print("     Ultima busca[          ]Próxima busca")
    print("                 [",end="", flush=True)
        
def time_remeaning():
    if(running == False):
        return -1
    return 60-next_time
        
def isItRunning():
    return running

def stopRunning():
    global running
    running = False
    
        
        
    
    
