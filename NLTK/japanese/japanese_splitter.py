import writter


# Splitting by punctuation
def sentenceSplit(text, p):
	start = 0
	s_list = []
	count = 0
	while( count < len(text)):
		if(text[count] in p):
			splitted = text[start:count]
			start = count+1
			s_list.append(splitted)
		count += 1
	return s_list

# Main takenizer function. Splits chars only when the word is complete
def jTokenize(text):

	main_response = []

	# Reading data from alphabets
	with open('hiraganaChart.txt', 'r', encoding='utf8') as h:
		hiraganaData = h.read()
	with open('katakanaChart.txt', 'r', encoding='utf8') as k:
		katakanaData = k.read()
	with open('punct.txt', 'r', encoding='utf8') as p:
		punctData = p.read()

	# Splitting by sentences
	
	sentences = sentenceSplit(text, punctData)
	return sentences

	
