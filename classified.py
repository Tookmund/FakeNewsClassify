import nltk
import readFNC as ds

allwords = nltk.FreqDist(w.lower() for d in ds.data for w in d[0])

wordfeatures = [w[0] for w in allwords.most_common(2000)]

def documentFeatures(document):
    documentWords = set(document)
    features = {}
    for word in wordfeatures:
        features['contains({})'.format(word)] = (word in documentWords)
    return features

featuresets = [(documentFeatures(d[0]), d[1]) for d in ds.data]

TESTNUM = int(ds.total/2)
testSet = featuresets[:TESTNUM]
trainSet = featuresets[TESTNUM:]

