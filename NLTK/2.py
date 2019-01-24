import imp
from nltk.corpus import stopwords
from nltk.tokenize import work_tokenize

ex = "This is an example showing off stop words filtration."

stop_words = set(stopwords.words("englsih"))

#words = work_tokenize(ex)
#filtered = []
#
#for word in words:
#	if word not in stop_words:
#		filtered.append(word)
#
#print(filtered)

filtered = [w for w in words if not w in stop_words]
print(filtered)