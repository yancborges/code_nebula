import imp
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwrods

text = 'Hey this is my list. I got a bunch o sentences. But since i\'m divorced i have to split them up.'

print(sent_tokenize(text))
print(word_tokenize(text))

stop_words = set(stopwords.words('english'))





