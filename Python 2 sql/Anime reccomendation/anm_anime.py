import urllib.request
import mysql.connector
from bridge_sql import bridge

#Defining the anime class
#Contains the Anime object, db inserts and some web scrapping methods for retrieving data

class anm_anime:

	#Instancing	
	def __init__( self, anm_name, anm_score, anm_dateWatched, anm_episodes ):
		self.anm_name = anm_name
		self.anm_score = anm_score
		self.anm_dateWatched = anm_dateWatched
		self.anm_episodes = anm_episodes

	#Gets an URL from myanimelist.net with a name
	def getAnimeUrl(self, name):

		txt = name.replace(" ", "%20")

		page = urllib.request.urlopen("https://myanimelist.net/search/all?q=" + txt )
		resp = page.read().decode("utf8")

		tag = resp.find('<article>')
		start = resp.find('<a href="https://myanimelist.net/anime/', tag)
		end = resp.find('class="hoverinfo_trigger', start)-2

		cleanResp = resp[start+9:end]

		#return resp
		return cleanResp
	
	def getAnimeData(self, url):
		
		page = urllib.request.urlopen(url)
		resp = page.read().decode("utf8")
        
    
                    
