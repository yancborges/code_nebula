import imp

from nltk.corpus import wordnet

text = input('text: ')

mean = wordnet.synsets(text)
print(mean)
for s in mean:
	print(s.definition())
	for l in s.lemmas():
		print(s.wup_similarity(wordnet.synsets(l.name())))