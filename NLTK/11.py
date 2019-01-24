import imp
import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

docs = [(list(movie_reviews.words(fileid)), category)
		for category in movie_reviews.categories()
		for fileid in movie_reviews.fileids(category)]

random.shuffle(docs)

#print(docs[1])

all_words = []
for w in movie_reviews.words():
	all_words.append( w.lower() )

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))
#print(all_words["stupid"])


word_features = list(all_words.keys())[:3000]

def find_features(docs):
	words = set(docs)
	features = {}
	for w in word_features:
		features[w] = (w in words)

	return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featureSets = [(find_features(rev), category) for (rev, category) in docs]

training_set = featureSets[:1900]
testing_set = featureSets[1900:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)
classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print('Original Naive Bayes Algo accurancy:', (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

#save_classifier = open("naivebayes.pickle", "wb")
#pickle.dump(classifier, save_classifier)
#save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print('MNB_classifier Naive Bayes Algo accurancy:', (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

#GaussianNB_classifier = SklearnClassifier(GaussianNB())
#GaussianNB_classifier.train(training_set)
#print('GaussianNB_classifier Naive Bayes Algo accurancy:', (nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print('BernoulliNB_classifier Naive Bayes Algo accurancy:', (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

### SAME FOR: <LogicstRegression, SGDClassifier, SVC, LinearSVC and NuSVC

