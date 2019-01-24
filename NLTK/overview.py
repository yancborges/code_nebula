import imp
import nltk
from nltk.corpus import treebank

sent = input('sent: ')
tokens = nltk.word_tokenize(sent)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)
#entities.draw()

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()

