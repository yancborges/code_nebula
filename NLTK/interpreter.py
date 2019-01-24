import imp
import nltk

pos_value = {'CC':'coordinating conjunction',
			'CD':'cardinal digit',
			'DT':'determiner',
			'EX':'existential there',
			'FW':'foreign word',
			'IN':'preposition/subordinating conjunction',
			'JJ':'adjective',
			'JJR':'adjective, comparative',
			'JJS':'adjective, superlative',
			'LS':'list marker',
			'MD':'modal	could',
			'NN':'noun, singular',
			'NNS':'noun plural',
			'NNP':'proper noun, singular',
			'NNPS':'proper noun, plural',
			'PDT':'predeterminer',
			'POS':'possessive ending',
			'PRP':'personal pronoun',
			'PRP$':'possessive pronoun',
			'RB':'adverb',
			'RBR':'adverb, comparative',
			'RBS':'adverb, superlative',
			'RP':'particle',
			'TO':'to go',
			'UH':'interjection',
			'VB':'verb, base form',
			'VBD':'verb, past tense	took',
			'VBG':'verb, gerund/present participle',
			'VBN':'verb, past participle',
			'VBP':'verb, sing. present, non-3d',
			'VBZ':'verb, 3rd person sing. present',
			'WDT':'wh-determiner',
			'WP':'wh-pronoun',
			'WP$':'possessive wh-pronoun',
			'WRB':'wh-abverb'
}

#======= Word tagging =======
def process(text):
	try:
		return nltk.pos_tag(nltk.word_tokenize(text))
	except:
		return None

text = input('hey: ')
tagged_words = process(text)

#====== Sentence split ========
sent_split = nltk.sent_tokenize(text)

#====== [possible] Topic search ==========
topics = []

def isTopic(tag):
	if(tag == 'PRP' or tag == 'NN' or tag == 'NNP' or tag == 'NNS' or tag == 'NNPS' ):
		return True
	return False


for sent in sent_split:
	by_word = nltk.word_tokenize(sent)
	sent_topics = []
	for word in by_word:
		if(isTopic(nltk.pos_tag(nltk.word_tokenize(word))[0][1])):
			sent_topics.append(word)
	topics.append(sent_topics)

print(topics)


#====== Check topic for each sentence =====



'''POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent\'s
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
'''
