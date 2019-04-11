import nltk
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

