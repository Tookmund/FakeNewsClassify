import csv
import sys
import random
from urllib.parse import urlparse
import pickle

import cleantext

csv.field_size_limit(sys.maxsize)

totalReal = 0
totalFake = 0
total = 0

EACH = 8000
PERSRC = 150
dontuse = [
#        "baptistnews.com",
#        "www.nfl.com", "m.mlb.com", "www.nba.com",
#        "www.cbssports.com",
#        "nz.sports.yahoo.com",
#        "sports.yahoo.com",
#        "olympics.blogs",
#        "de.finance.yahoo.com",
#        "der-postillon.com"
        ]

data = []
source = {}

def loaddata(cleaned=True):
    global data
    global total
    global totalReal
    global totalFake
    data = []
    with open('data/FakeNewsCorpus.csv', 'rU', newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            if len(row) < 16:
                continue
            loc = row[2]
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

            if cleaned:
                ct = cleantext.cleanText(row[5])
            else:
                ct = row[5]
            data.append([ct, row[3]])
            print(row[1], loc)
            total += 1
            if totalFake >= EACH and totalReal >= EACH:
                break

    for s, n in source.items():
        print(s, ":", n)

    if cleaned:
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
