import csv
import sys
import random
from urllib.parse import urlparse
import re
import pickle

import cleantext

csv.field_size_limit(sys.maxsize)

totalReal = 0
totalFake = 0
total = 0

EACH = 5000
PERSRC = 100
dontuse = [
        "baptistnews.com",
        "nfl.com", "mlb.com", "nba.com",
        "empiresports.co",
        "sportspickle.com",
        "cbssports.com",
        "nz.sports",
        "sports.yahoo",
        "olympics.blogs"]

data = []
source = {}

def loaddata():
    global total
    global totalReal
    global totalFake
    host = re.compile(r"(w+\S*\.|m\.|mobile\.)*([^\.\s]+\.[^\.\s]+)$")
    with open('data/FakeNewsCorpus.csv', 'rU', newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            if len(row) < 16:
                continue

            loc = urlparse(row[4]).netloc
            if loc == '':
                continue
            loc = host.match(loc).group(2)
            if loc in dontuse:
                continue
            if loc in source:
                if source[loc] >= PERSRC:
                    continue
                source[loc] += 1
            else:
                source[loc] = 1

            if row[3] == 'fake':
                if totalFake >= EACH:
                    continue
                totalFake += 1
            elif row[3] == 'reliable':
                if totalReal >= EACH:
                    continue
                totalReal += 1
            else:
                continue

            ct = cleantext.cleanText(row[5])
            data.append([ct, row[3]])
            print(row[1], loc)
            total += 1
            if totalFake >= EACH and totalReal >= EACH:
                break

    for s, n in source.items():
        print(s, ":", n)

    with open("data/fncdata.pkl", "wb") as p:
        pickle.dump([total, totalFake, totalReal, data], p)

try:
    with open("data/fncdata.pkl", 'rb') as p:
        ret = pickle.load(p)
        total = ret[0]
        totalFake = ret[1]
        totalReal = ret[2]
        data = ret[3]

except:
    loaddata()

random.shuffle(data)
print("Real: %d" % totalReal)
print("Fake: %d" % totalFake)
print("Total: %d" % total)
