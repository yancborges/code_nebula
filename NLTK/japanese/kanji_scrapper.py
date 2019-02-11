import urllib.request
import pandas as pd
import writter

class kanji:

	def __init__(self,name,strokes,frequency,grade,jlpt):
		self.name = name
		self.strokes = strokes
		self.frequency = frequency
		self.grade = grade
		self.jlpt = jlpt

	def save(self):
		with open('kanji_dict.txt', 'a') as f:
			f.write(toString())

	def toString(self):
		return self.name + ',' + str(self.strokes) + ',' + str(self.frequency) + ',' + self.grade + ',' + self.jlpt

	def scrap(self):
		url = 'https://jisho.org/search/%23kanji%20' + self.name
		resp = urllib.request.urlopen(url).read().decode("utf-8")
		writter.hey(resp,'htmltest.html','w',False,True)
		self.strokes = resp.split('<div class="kanji-details__stroke_count">')[0].split('<strong>')[1].split('</strong>')[0]
		



def create():
	try:
		with open('kanji_dict.txt', 'r') as f:
			size = len(f.read())
	except:
		with open('kanji_dict.txt', 'w') as f:
			f.write('name,strokes,frequency,grade,jlpt')


def load():
	kanji_dict = pd.read_csv('kanji_dict.txt')
	return kanji_dict

def seek(kanji, kanji_dict):
	kanji_dict = list(kanji_dict.name)
	if(kanji.name not in kanji_dict):
		kanji.scrap()
		return False
	return True


