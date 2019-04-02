import nltk

import cleantext
import readFNC

allwords = nltk.FreqDist(w.lower() for d in readFNC.data for w in d[0])

wordfeatures = [w[0] for w in allwords.most_common(2000)]

def documentFeatures(document):
    documentWords = set(document)
    features = {}
    for word in wordfeatures:
        features['contains({})'.format(word)] = (word in documentWords)
    return features

featuresets = [(documentFeatures(d[0]), d[1]) for d in readFNC.data]

TESTNUM = int(readFNC.total/2)
testSet = featuresets[:TESTNUM]
trainSet = featuresets[TESTNUM:]

classifier = nltk.NaiveBayesClassifier.train(trainSet)

print(nltk.classify.accuracy(classifier, testSet))

classifier.show_most_informative_features(50)
