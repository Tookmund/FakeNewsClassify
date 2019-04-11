import nltk

import classified

classifier = nltk.NaiveBayesClassifier.train(classified.trainSet)

print(nltk.classify.accuracy(classifier, classified.testSet))

classifier.show_most_informative_features(50)
