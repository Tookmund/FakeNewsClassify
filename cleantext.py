from nltk.corpus import stopwords
stop = stopwords.words('english')

def toWords(text):
    return [w for w in text.split()]

def cleanText(text):
    text = toWords(text)
    return [w for w in text if w.isalpha() and w not in stop]
