import writter
import pandas as pd

# Splitting by punctuation
def jSentence_tokenize(text, p):
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

def check_word(text, d):
	if(text in d):
		return True
	return False

# Main tokenizer function. Splits chars only when the word is complete
def jTokenize(text):

	main_response = []

	# Reading data from alphabets
	with open('hiraganaChart.txt', 'r', encoding='utf8') as h:
		hiraganaData = h.read()
	with open('katakanaChart.txt', 'r', encoding='utf8') as k:
		katakanaData = k.read()
	with open('punct.txt', 'r', encoding='utf8') as p:
		punctData = p.read()
	dictData = pd.read_csv('dictionary.txt')

	# Splitting by sentences
	sentences = jSentence_tokenize(text, punctData)
	
	# Splitting each sentence by its words
	for sent in sentences:
		sent_tokenized = []
		char_string = ''
		# If the code does not recognize the parameter as a single word, the next char
		# is appended to it, until the word ends
		count = 0
		stopped = 0
		safe = 0

		while(count < len(sent)):
			print(stopped,safe,count)
			char_string += sent[count]
			if(check_word(char_string, list(dictData.Word))):
				safe = count
				if(len(char_string) == 1):
					stopped = count
			else:
				if(len(char_string) == 1):
					stopped = count
				if(len(sent[stopped:safe]) > 0):
					sent_tokenized.append(sent[stopped:safe+1])
					char_string = ''
					count = safe+1
			count += 1
			if(count >= len(sent)):
				count = stopped+1
				char_string = ''







		main_response.append(sent_tokenized)

	return main_response


	
