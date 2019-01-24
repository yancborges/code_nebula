import urllib.request
import json
import os
import tweepy
from tweepy import OAuthHandler


# Getting API data from local file
print("Opening api data...")
f = open('C:\\Users\\Yan\\Desktop\\Scripting\\TWITTER_API_KEY.txt', 'r')
api_key= f.readlines()
f.close()

# Setting the found data
print("Setting new data...")
consumer_key = api_key[0][:-1]
consumer_secret = api_key[1][:-1]
access_token = api_key[2][:-1]
access_secret = api_key[3]


print("Validating...")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
#api.update_status('Primeiro tweet via código!')

r = open("teste.txt", "w")

search = api.search(q=input("Pesquisar por: "),locale="pt",showuser="true")
#printable = "1234567890-=qwertyuiop[]asdfghjklçzxcvbnm,.;<>:!@#$%*()_+/*'áéíóúàêãõ|\"

print("Realizando busca...")
#for x in tweepy.Cursor(search).items(200):
for x in search:
    try:
        r.write("<" + x.text + ">\n")
    except:
        print("Erro: Não foi possivel abrir o tweet.")
    
f.close()
print("Busca concluída, verifique o arquivo de logs para os resultados.")
    
    

