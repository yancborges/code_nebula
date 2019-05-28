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
from sklearn.model_selection import cross_val_score

### Constants & global variables ##########################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

MAX_GENRES = 43

### Other functions #######################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

def binary_string_gen(non_binary, new):
		binary_array = []
		for i in range(1,MAX_GENRES):
			if(new == True):
				x = i
			else:
				x = str(i)
			if(x in non_binary):
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
			url = ("http://myanimelist.net/animelist/" + nick + '?status=7')
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
			f.write('Title=@Score=@Status=@url=@Genre_Id\n')
		with open(string,'a', encoding='utf8') as f:
			for item in self.clean_list:
				f.write('%s=@%s=@%s=@%s=@%s \n' %(item.title,item.score,item.status,item.url,item.genres))

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
			print(self.pd_series[self.pd_series.Status == 2].Score.mean())
			with open(self.nick + '_ds.csv', 'w') as f:
				f.write('Title=@Genres_id=@Score \n')
			with open(self.nick + '_ds.csv', 'a', encoding='utf8') as f:
				for item in self.clean_list:
					if(item.status == 2):
						f.write('%s=@%s=@%s \n' %(item.title,str(binary_string_gen(item.genres,False)),item.isLikeable(self.pd_series[self.pd_series.Status == 2].Score.mean())))
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

	def isLikeable(self, mean):
		if( self.score > mean ):
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
		y = self.data.Score

		#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

		### Choosing algorithm

		'''
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
		'''
		w_obj = LogisticRegression()
		w_obj.fit(X, y)
		
		print('Score:', cross_val_score(w_obj, X, y, cv=5, scoring='accuracy').mean())

		#y_pred = w_obj.predict(X_test)
		#print('Precision score:', metrics.precision_score(y_test, y_pred))

		with open(self.nick + '_trained.pkl', 'wb') as f:
			pickle.dump(w_obj, f)
		return w_obj

	def predict(self, new_data):

		algorithm = None
		resp_arr = []

		try:
			with open(self.nick + '_trained.pkl', 'rb') as f:
				algorithm = pickle.load(f)

		except:
			algorithm = self.train_test(self.nick)
			

		for item in new_data:

			item_x = [binary_string_gen(item,True)]
			resp_arr.append(algorithm.predict_proba(item_x)[:,1][0])

		return resp_arr


### Running section #######################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

nick = 'Xinil'
new_data = [[1,2,10,11,16,37],[1,14,40,37,8,22,42],[24,19,8,22],[1,24,31,8,22,18],[4,37,22,32,10,23,27],[4,40,22,23,42],[22,42],[35,4,31,22,9,17,23],[1,36,4,37],[24,8,22],[1,24,18]]


try:
	with open('object_list_from_' + nick + '.pkl', 'rb') as f:
		my_list = pickle.load(f)
	
except Exception as e:
	print(e)
	my_list = a_list(nick)
	
data = my_list.create_dataSet()

test = analysis(nick,data)

for item in test.predict(new_data):
	print('Anime relevancy:','%.2f' %(float(item)*100), '%' )




