import writter
import kanji_scrapper
import pandas as pd

def analyse_list(kanji_df):
	print(kanji_df.grade.value_counts())
	print(kanji_df.jlpt.value_counts(normalize=True))


def analyse_text(text):

	kanji_scrapper.create()
	data = kanji_scrapper.load()

	with open('hiraganaChart.txt', 'r', encoding='utf8') as h:
		hiraganaData = h.read()
	with open('katakanaChart.txt', 'r', encoding='utf8') as k:
		katakanaData = k.read()
	with open('punct.txt', 'r', encoding='utf8') as p:
		punctData = p.read()

	kanji_list = []
	kanji_names = []

	for char in text:

		if(char not in punctData):
			if(char not in hiraganaData and char not in katakanaData):
				kanji = kanji_scrapper.kanji(char,'','','','')
				kanji_scrapper.seek(kanji,data)
				kanji_list.append(kanji)
				kanji_names.append(char)

	kanji_df = kanji_scrapper.load()
	
	tof = []
	for name in kanji_df.name:
		if(name in kanji_names):
			tof.append(True)
		else:
			tof.append(False)

	is_there = pd.Series(tof)
	kanji_df = kanji_df[is_there]

	analyse_list(kanji_df)

text = '私は子供です。だから、お菓子を食べてが好き！'
analyse_text(text)





