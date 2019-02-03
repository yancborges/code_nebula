import urllib.request
import pandas
import writter
import re

# Info about level
class level:

	def __init__(self,name,count,url):
		self.name = name
		self.count = count
		if(url == ''):
			self.url = 'https://jisho.org/search/%23' + name
		else:
			self.url = url

# Info about words within the levels
class word:

	def __init__(self,text,function,level_name,ph_freq,common):
		self.text = text
		self.function = function
		self.level_name = level_name
		self.ph_freq = ph_freq
		self.common = common

	def toString(self):
		return self.text + ',' + self.function + ',' + self.level_name + ',' + self.ph_freq + ',' + self.common

# Main function
# Scraps the words from Jisho.org lists.
# When finishig the words of the first page, it goes to the second until the count ends,
# and then go to the next level and repeat.
def create_dictionary():

	levels = []
	levels.append(level('jlpt-n5',0,''))
	levels.append(level('jlpt-n4',0,''))
	levels.append(level('jlpt-n3',0,''))
	levels.append(level('jlpt-n2',0,''))
	levels.append(level('jlpt-n1',0,''))

	words_list = []
	words = []
	total_count = levels[0].count + levels[1].count + levels[2].count + levels[3].count + levels[4].count
	perc = 0

	#writter.hey('word,function,level,frequency,common','jishoDict.txt','w',True)
	
	l_count = 0
	page_count = 1
	while(l_count < 5):
		
		url = levels[l_count].url
		print('looking ' + url + '...')
		resp = urllib.request.urlopen(url).read().decode("utf-8")
		dirty_list = resp.split('<div class="concepts">')[1].split('<footer class="clearfix">')[0]
		
		start = dirty_list.find('<span class="result_count">')+30
		total = dirty_list[start:dirty_list.find(' found</span>', start)]

		levels[l_count].count = total

		print('Level total words: - ' + total)

		last_block = 0

		while(dirty_list.find('<span class="text">', last_block) > 0):

			
			# Taking the word
			text = dirty_list[last_block:].split('<span class="text">')[1][8:]
			text = text[:text.find('</span>')-7]
			if(text.endswith(' ')):
				text = text.split(' ')[0]
			
			# Taking function
			s_func = dirty_list.find('<div class="meaning-tags">', last_block)+26
			function = dirty_list[s_func:dirty_list.find('</div>', s_func)]

			#
			# Remeaning info: [level_name,ph_freq,common]
			#

			# Level_name
			level_name = ''

			# frequency
			freq = ''

			# Common?
			common = ''			

			# Setting the checkpoint (for not getting the same data twice)
			last_block = dirty_list.find('</span>', dirty_list.find('<span class="text">', last_block))+20

			# Creating object
			word_obj = word(text,function,level_name,freq,common)

			writter.hey(word_obj.toString(),'new_dict_test.txt','a',True,False)
			words.append(word_obj)
			
			# Number of words
			#print('%s of %s words.' %(len(words), levels[l_count].count))

		# If there are no more results in this page, go to the next one
		if(len(words) < int(levels[l_count].count)):
			page_count += 1
			levels[l_count].url = 'https://jisho.org/search/%23' + levels[l_count].name + '%20%23words?page=' + str(page_count)
		# If there are no more words left, let's go to the next level then
		else:
			l_count += 1
			page_count = 1
			words_list.append(words)
			words = []


create_dictionary()