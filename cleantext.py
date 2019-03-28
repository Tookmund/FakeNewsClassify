from nltk.corpus import stopwords
stop = stopwords.words('english')

def cleanText(text):
    return [w for w in text if w.isalpha() and w not in stop]
