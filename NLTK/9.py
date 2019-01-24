import imp

from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

sample = gutenberg.raw("bible-kjv.txt")
print(sent_tokenize(sample)[5:15])