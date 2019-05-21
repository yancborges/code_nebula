### Importing libs #######################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

import urllib.request
import json
import pandas as pd
import re
from urllib.parse import quote_from_bytes
import pickle

import imp
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor

### Constants & global variables ##########################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

MAX_GENRES = 43

### Other functions #######################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

def binary_string_gen(non_binary):
		binary_array = []
		for i in range(1,MAX_GENRES):
			if(str(i) in non_binary):
				binary_array.append(1)
			else:
				binary_array.append(0)
		return binary_array

def toFloat(matrix):
	new_matrix = []
	for array in matrix:
		new_array = []
		for item in array:
			if(str(item) in '01'):
				new_array.append(float(item))
		new_matrix.append(new_array)
	return new_matrix



### Classes, data scrapping, object instantiation & file management #######################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

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
				f.write('%s=@%s=@%s=@%s=@%s=@%s \n' %(item.title,item.status,item.score,item.id,item.url,item.genres))

	def readPandas(self):
		try:
			return pd.read_csv(string, sep="=@", engine='python')
		except:
			self.toPandas()
			string = self.nick + '_data.csv'
			return pd.read_csv(string, sep="=@", engine='python')

	def create_dataSet(self):
		try:
			return pd.read_csv(self.nick + '_ds.csv', sep='=@', engine='python')
		except:
			with open(self.nick + '_ds.csv', 'w') as f:
				f.write('Title=@Genres_id=@Score \n')
			with open(self.nick + '_ds.csv', 'a', encoding='utf8') as f:
				for item in self.clean_list:
					if(item.status == 2):
						print(self.pd_series.Score)
						f.write('%s=@%s=@%s \n' %(item.title,str(binary_string_gen(item.genres)),item.isLikeable(self.pd_series.Score.mean(),item.score)))
			return pd.read_csv(self.nick + '_ds.csv', sep='=@', engine='python')

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
			'genres':str(self.genres)
		}

	def get_genres(self):

		try:
			resp = urllib.request.urlopen('https://myanimelist.net' + self.url).read().decode("utf-8")
			
		except:
			resp = urllib.request.urlopen('https://myanimelist.net' + quote_from_bytes(self.url.encode('utf-8'))).read().decode("utf-8")
		gen_block = resp.split('<span class="dark_text">Genres:</span>')[1].split('</div>')[0].replace('<a href="/anime/genre/', '')
		return list(re.findall(r'\d{1,9}', gen_block))

	def isLikeable(self, mean, score):
		if( score < mean ):
			return 1
		return 0



### Analysis section ######################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

class analysis:

	def __init__(self, nick, data):
		self.nick = nick
		self.data = data

	def train_test(self, nick):
		
		X = toFloat(list(self.data.Genres_id))
		print(type(X))
		y = self.data.Score

		print(X[0])

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

		### Choosing algorithm

		algorithms = {
			'LogisticRegression':LogisticRegression(),
			'Knn':KNeighborsClassifier(n_neighbors=5),
			'DecisionTreeRegressor':DecisionTreeRegressor()
		}

		results = {}

		for alg in algorithms:
			clf = algorithms[alg]
			clf.fit(X_train,y_train)
			score = clf.score(X_test,y_test)
			results[alg] = score

		winner = max(results, key=results.get)
		print(results)
		print('Max accuracy: ' + str(results[winner] * 100) + '%')
		w_obj = algorithms[winner]

		with open(self.nick + '_trained.pkl', 'wb') as f:
			pickle.dump(w_obj, f)

	def predict(self, new_data):

		algorithm = None
		new_data = [binary_string_gen(new_data)]

		try:
			with open(self.nick + '_trained.pkl', 'rb') as f:
				algorithm = pickle.load(f)
		except:
			self.train_test(self.nick)
			with open(self.nick + '_trained.pkl', 'rb') as f:
				algorithm = pickle.load(f)
			self.predict(new_data)

		return algorithm.predict(new_data)


### Running section #######################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

#nick = 'ThousandAntas'
nick = 'ThousandAntas'
new_data = [[8,19,22,23,27]]

try:
	with open('object_list_from_' + nick + '.pkl', 'rb') as f:
		my_list = pickle.load(f)
	
except Exception as e:
	print(e)
	my_list = a_list(nick)
	
data = my_list.create_dataSet()

test = analysis(nick,data)
print(test.predict(new_data))




