import nltk
import random

import cleantext
import readFNC

random.shuffle(readFNC.data)

allwords = nltk.FreqDist(w.lower() for d in readFNC.data for w in d[0])

wordfeatures = list(allwords)[:2000]

def documentFeatures(document):
    documentWords = set(document)
    features = {}
    for word in wordfeatures:
        features['contains({})'.format(word)] = (word in documentWords)
    return features

featuresets = [(documentFeatures(d[0]), d[1]) for d in readFNC.data]

TESTNUM = int((readFNC.totalReal+readFNC.totalFake)/2)
testSet = featuresets[:TESTNUM]
trainSet = featuresets[TESTNUM:]

classifier = nltk.NaiveBayesClassifier.train(trainSet)

print(nltk.classify.accuracy(classifier, testSet))

classifier.show_most_informative_features(50)
