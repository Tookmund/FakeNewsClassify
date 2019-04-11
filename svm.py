from nltk.classify import SklearnClassifier
from sklearn.svm import SVC

import classified

svm = SklearnClassifier(SVC(), sparse=False).train(classified.trainSet)
test = svm.classify_many(x[0] for x in classified.testSet)

correct = 0

for i in range(len(test)):
    if test[i] == classified.readFNC.data[i+classified.TESTNUM][1]:
        correct += 1

correct /= len(test)
print(correct)
