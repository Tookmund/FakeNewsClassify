import nltk
import readFNC as ds
ds.loaddata(False)

allwords = nltk.FreqDist(w.lower() for d in ds.data for w in d[0])

wordfeatures = [w[0] for w in allwords.most_common(2000)]

def documentFeatures(document):
    documentWords = set(document)
    features = {}
    for word in wordfeatures:
        features['contains({})'.format(word)] = (word in documentWords)
    for word in document:
        c = 'count({})'.format(word)
        if c in features:
            features[c] += 1
        else:
            features[c] = 1
    return features

featuresets = [(documentFeatures(d[0]), d[1]) for d in ds.data]

TESTNUM = int(ds.total/2)
testSet = featuresets[:TESTNUM]
trainSet = featuresets[TESTNUM:]

