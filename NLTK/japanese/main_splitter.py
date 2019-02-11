import writter
import kanji_scrapper

def analyse(text):

	kanji_scrapper.create()
	data = kanji_scrapper.load()

	with open('hiraganaChart.txt', 'r', encoding='utf8') as h:
		hiraganaData = h.read()
	with open('katakanaChart.txt', 'r', encoding='utf8') as k:
		katakanaData = k.read()
	with open('punct.txt', 'r', encoding='utf8') as p:
		punctData = p.read()

	for char in text:

		if(char not in punctData):
			if(char not in hiraganaData and char not in katakanaData):
				kanji = kanji_scrapper.kanji(char,'','','','')
				kanji_scrapper.seek(kanji,data)
				print(text.index(char))


text = '私は子供です。だから、お菓子を食べてが好き！'
analyse(text)





