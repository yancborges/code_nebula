import imp
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

ex = ["python","pythoner","pythoning","pythoned","pythonly"]

#for word in ex:
	#print(ps.stem(w))

ex2 = "It is very important to be pythonly while you are pythoning. All pythoners have pythoned poorly at least once."

words = word_tokenize(ex2)

for w in words:
	print(ps.stem(w))