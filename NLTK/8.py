import imp

from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()

print(lem.lemmatize("cats"))
print(lem.lemmatize("wolves"))
print(lem.lemmatize("better", 'a'))