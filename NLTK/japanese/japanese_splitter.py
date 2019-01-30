import imp

def jTokenize(text):
	with open('hiraganaChart.txt', 'r', encoding='utf8') as h:
		hiraganaData = h.read()
	with open('katakanaChart.txt', 'r', encoding='utf8') as k:
		katakanaData = k.read()
	sentences = wordpunct_tokenize(text)
	return_list = []
	sent_list = []
	for sentence in sentences:
		char_list = ''
		for char in sentence:
			char_list += char
			if((char not in hiraganaData) or (char not in katakanaData)):
				sent_list.append(char_list)
				char_list = ''
		return_list.append(sent_list)
	return return_list

