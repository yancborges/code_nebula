import urllib.request
import json
import pandas as pd

class a_list:

	def __init__(self, nick):
		self.nick = nick
		self.raw_data = self.getJson(self.nick)
		self.clean_list = []
		self.fill_list()
		self.pd_series = self.readPandas()

	def fill_list(self):
		for raw_item in self.raw_data:
			i = item(raw_item)
			self.clean_list.append(i)

	def readJson(self, string):

		with open(string,'r') as f:
			data = json.load(f)
		return data


	def getJson(self, nick):

		url = ("http://myanimelist.net/animelist/" + nick)
		resp = urllib.request.urlopen(url).read().decode("utf-8")
		raw_list = resp.split('data-items="')[1].split('">')[0].replace('&quot;','"')
		string = nick + '_data.json'
	
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
			f.write('Title=@Score=@Status=@Id\n')
		with open(string,'a', encoding='utf8') as f:
			for item in self.clean_list:
				f.write('%s=@%s=@%s=@%s \n' %(item.title,item.score,item.status,item.id))

	def readPandas(self):
		self.toPandas()
		string = self.nick + '_data.csv'
		return pd.read_csv(string, sep="=@", engine='python')


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

	def toString(self):
		return {
			'Title':self.title,
			'Score':self.score,
			'Id':self.id,
			'Status':self.status
		}


my_list = a_list('ThousandAntas')
print(my_list.pd_series.describe)

