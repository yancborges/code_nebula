import imp
import nltk

def process(text):
	tokens = nltk.word_tokenize(text)
	tagged = nltk.pos_tag(tokens)
	#tag_pattern = r"""Chunk: {<PRP\$.?><NN>}"""
	tag_pattern = r"""Chunk: {<VB.?><PRP>}"""
	chunkParser = nltk.RegexpParser(tag_pattern)
	chunked = chunkParser.parse(tagged)
	chunked.draw()
	return chunked

x = process(input('text: '))

for i in x:
	print(i)