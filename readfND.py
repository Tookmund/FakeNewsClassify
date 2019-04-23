import os
import random

import cleantext

DATASET="data/fakeNewsDatasets/fakeNewsDataset/"
data = []

totalReal = 0
totalFake = 0
total = 0

def loaddata(cleaned=True):
    global total
    global totalReal
    global totalFake
    global data
    data = []
    total = 0
    totalReal = 0
    totalFake = 0
    for n in os.listdir(DATASET+"/fake"):
        with open(DATASET+"/fake/"+n) as f:
            if cleaned:
                ct = cleantext.cleanText(f.read())
            else:
                ct = f.read()
            data.append([ct, "fake"])
            totalFake += 1
    for n in os.listdir(DATASET+"/legit"):
        with open(DATASET+"/legit/"+n) as f:
            if cleaned:
                ct = cleantext.cleanText(f.read())
            else:
                ct = f.read()
            data.append([ct, "reliable"])
            totalReal += 1

    random.shuffle(data)
    total = totalFake + totalReal

    print("Real: %d" % totalReal)
    print("Fake: %d" % totalFake)
    print("Total: %d" % total)

loaddata()
