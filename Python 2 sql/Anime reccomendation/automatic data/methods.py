import urllib.request
import random
import time

#This function will recieve the user's url and then scrap all the animes watched

# === NOT WORKING ===
def getAnimeList(uUrl):
    
    page = urllib.request.urlopen(uUrl)
    
    time.sleep(10)
    
    resp = page.read().decode("utf8")
    
    #Checks if the user exists
    if(resp.find('<h1 class="h1">Invalid Username Supplied</h1>') > 0 ):
        return False
    else:
        
        #Declaring the list
        a_start = 1
        lstart = 1
        anm_list = []
        
        if( a_start > 0 ):
            
            a_start = resp.find('<tbody class="list-item"><tr class="list-table-data"><td class="data status completed"></td>', lstart )
            start = resp.find('<a href="', a_start )
            end = resp.find('" class="link sort">', start )
            
            link = 'https://myanimelist.net/' + resp[start+8:end]
            
            xstart = resp.find('<td class="data score"><a href="#" class="link">', end )
            xend = resp.find('</a>', xstart )
            
            uScore = resp[xstart+13:end-12]
            
            #Passing to the next div of completed anime
            lsstart = xend
            
            #Testing
            print("#####################")
            print(link)
            print("#####################")
            print(start)
            print('/')
            print(end)
            print('===wtf===')
            print(a_start)
            #print(uScore)
            print('-------------')

#This function will recieve the anime's url and then scrap it's data
def getAnimeData(url, u_score):

    #Scrap page's HTML content
    page = urllib.request.urlopen(url)
    #Decoding script
    resp = page.read().decode("utf8")
    
    #Checks if the link is valid and the anime searched exists
    if(resp.find('<div class="error404"') > 0):
        #return False
        print('Nothing found')
    #If exists, start to scrap it's data
    else:
    
        #Seting variables for the anime object
        name = ''
        genere = []
        studio = ''
        nEpisodes = 0
        score = 0.0

        # === Getting Name ===
    
        #Looks for this tag in the HTML code
        start = resp.find('<span itemprop="name">')
        end = resp.find('</span>',start)
        
        #Then we filter the response from HTML with the tag found
        name = resp[start+22:end]
        
        # === Getting Score ===
        
        #Looks for this tag in the HTML code
        b_start = resp.find('<div class="fl-l score" data-title="score"')
        end = resp.find('</div>', b_start )
        start = resp.find('">', b_start )
        
        #Then we filter the response from HTML with the tag found
        score = resp[start+11:end-7]
        
        # === Getting Studio ===
        
        #Looks for this tag in the HTML code        
        b_start = resp.find('<span class="dark_text">Studios:</span>')
        bs_start = resp.find('<a href="/anime/producer', b_start )
        end = resp.find('</a>',bs_start)
        start = resp.find('">', bs_start )
                
        #Then we filter the response from HTML with the tag found
        studio = resp[start+2:end]
        
        # === Getting Number of Episodes ===
        
        #Looks for this tag in the HTML code
        start = resp.find('<span class="dark_text">Episodes:</span>')
        end = resp.find('</div>', start )
        
        #Then we filter the response from HTML with the tag found
        nEpisodes = resp[start+43:end-3]
        
        # === Getting Generes ===
        
        lstart = resp.find('<span class="dark_text">Genres:</span>')
        while( start > 0 ):
            b_start = resp.find('<a href="/anime/genre/', lstart)
            start = resp.find('">', b_start )
            end = resp.find('</a>', start )
            lstart = end
            genere.append(resp[start+2:end])
        
        # === Getting User Score ===
        
        #b_start = resp.find('<select name="myinfo_score"')
        #start = resp.find('<option selected="selected" value="', b_start)
        #end = start+38
        #uscore = resp[start+35:end]
        uscore = u_score
        
        # === Printing tests ===
        
        #print(name)
        #print(score)
        #print(studio)
        #print(nEpisodes)
        #print(genere[0:len(genere)-1])
        #print(uscore)
        
        #Creating object with the data saved
        anm = anime(name, nEpisodes, genere, studio, score, uscore)
        return anm
        
#Input testing

#url = []
#url.append('https://myanimelist.net/anime/23273/Shigatsu_wa_Kimi_no_Uso')
#url.append('https://myanimelist.net/anime/1575/Code_Geass__Hangyaku_no_Lelouch')
#url.append('https://myanimelist.net/anime/12355/Ookami_Kodomo_no_Ame_to_Yuki')
#url.append('https://myanimelist.net/anime/30276/One_Punch_Man')
#url.append('https://myanimelist.net/anime/1535/Death_Note')
#url.append('https://myanimelist.net/anime/227/FLCL')
#getAnimeData(url[random.randint(0,len(url)-1)])

getAnimeList('https://myanimelist.net/animelist/ThousandAntas')




  
