import urllib.request
import re

class move:

	def __init__(self, name, ttype, category, power, accuracy, description):

		self.name = name
		self.ttype = ttype
		self.category = category
		self.power = power
		self.accuracy = accuracy
		self.description = description

	def scrap(self):

		try:
			
			url = "https://pokemon.fandom.com/wiki/" +  ' '.join(x.capitalize() for x in self.name.split()).replace(' ','_')
			resp = urllib.request.urlopen(url).read().decode('utf-8')

			if(resp.find('<a href="/wiki/Category:Moves" data-tracking="categories-top-0">Moves</a>') == -1):
				print('Move not found')
		
			else:
			
				data = re.findall(r'<td style="vertical-align:right; padding-right:1em;"> \S+', resp)

				for i in data:
					print(i,'\n')

				acc_index = data.index([s for s in data if "%" in s][0])

				self.ttype = re.findall(r'<a href="/wiki/\w+_type" title="\w+ type"><span class="t-type2">\w+</span></a>',resp)[0].split('wiki/')[1].split('_')[0]
				self.category = re.findall(r'<a href="/wiki/Move#\w+"', resp)[0].split('#')[1][:-1]
				self.power = data[acc_index-1].split('>')[1].replace(' ','').replace('<sup','')
				self.accuracy = data[acc_index].split('>')[1].replace(' ','')
				self.description = re.findall(r'<td style="text-align:left; background:#FFFFFF">\D+</td>', resp)[0].split('>')[1][:-5]

				

		except Exception as e:
			print('Something went wrong.', e)

	def toString(self):
		return 'Name: %s \nType: %s \nCategory: %s \nPower: %s \nAccuracy: %s \nDescription: %s' %(self.name, self.ttype, self.category, self.power, self.accuracy, self.description)


