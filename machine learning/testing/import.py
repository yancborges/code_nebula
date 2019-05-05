import urllib.request
import json
import pandas as pd
import re
from urllib.parse import quote_from_bytes
import pickle

class a_list:

	def __init__(self, nick):
		self.nick = nick
		self.raw_data = self.getJson(self.nick)
		self.clean_list = []
		self.fill_list()
		self.pd_series = self.readPandas()
		self.toPickle()

	def fill_list(self):
		for raw_item in self.raw_data:
			i = item(raw_item)
			self.clean_list.append(i)

	def readJson(self, string):

		with open(string,'r') as f:
			data = json.load(f)
		return data

	def toPickle(self):
		with open('object_list_from_' + self.nick + '.pkl', 'wb') as f:
			pickle.dump(self, f)

	def getJson(self, nick):

		string = nick + '_data.json'

		try:
			with open(string,'r') as f:
				return self.readJson(string)
		except:
			url = ("http://myanimelist.net/animelist/" + nick)
			resp = urllib.request.urlopen(url).read().decode("utf-8")
			raw_list = resp.split('data-items="')[1].split('">')[0].replace('&quot;','"')
			
			with open(string,'w') as f:
				f.write(raw_list)
			return self.readJson(string)

	def toString(self):
		resp_list = []
		for item in self.clean_list:
			resp_list.append(item.toString())
		return resp_list

	def toPandas(self):
		string = self.nick + '_data.csv'
		with open(string,'w') as f:
			f.write('Title=@Score=@Status=@Id=@url\n')
		with open(string,'a', encoding='utf8') as f:
			for item in self.clean_list:
				f.write('%s=@%s=@%s=@%s=@%s=@%s \n' %(item.title,item.score,item.status,item.id,item.url,item.genres))

	def readPandas(self):
		try:
			return pd.read_csv(string, sep="=@", engine='python')
		except:
			self.toPandas()
			string = self.nick + '_data.csv'
			return pd.read_csv(string, sep="=@", engine='python')

	def create_dataSet(self):
		print(self.clean_list)


class item:

	def __init__(self, raw_list):
		
		# 1 = Watching
		# 2 = Completed
		# 3 = On hold
		# 4 = Dropped
		# 6 = Plan to watch
		self.status = raw_list['status']
		self.score = raw_list['score']
		self.title = raw_list['anime_title']
		self.id = raw_list['anime_id']
		self.url = raw_list['anime_url'].replace('\\','')
		self.genres = self.get_genres()

	def toString(self):
		return {
			'Title':self.title,
			'Score':self.score,
			'Id':self.id,
			'Status':self.status,
			'url':self.url,
			'genres':self.genres
		}

	def get_genres(self):

		try:
			resp = urllib.request.urlopen('https://myanimelist.net' + self.url).read().decode("utf-8")
			
		except:
			resp = urllib.request.urlopen('https://myanimelist.net' + quote_from_bytes(self.url.encode('utf-8'))).read().decode("utf-8")
		gen_block = resp.split('<span class="dark_text">Genres:</span>')[1].split('</div>')[0].replace('<a href="/anime/genre/', '')
		return re.findall(r'\d{1,9}', gen_block)


nick = 'ThousandAntas'

try:
	with open('object_list_from_' + nick + '.pkl', 'rb') as f:
		my_list = pickle.load(f)
	
except Exception as e:
	print(e)
	my_list = a_list(nick)
	

my_list.create_dataSet()

