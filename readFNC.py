import csv
import sys

import cleantext

csv.field_size_limit(sys.maxsize)

totalReal = 0
totalFake = 0
total = 0
MAX = 100000

data = []

with open('data/FakeNewsCorpus.csv', 'rU', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        if len(row) < 16:
            continue
        if row[3] == 'fake':
            totalReal += 1
        elif row[3] == 'reliable':
            totalFake += 1
        else:
            continue
        ct = cleantext.cleanText(row[5])
        data.append([ct, row[3]])
        print(row[1])
        total += 1
        if total > MAX:
            break

    print("Real: %d" % totalReal)
    print("Fake: %d" % totalFake)
    print("Total: %d" % total)
