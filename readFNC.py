import csv
import sys

import cleantext

csv.field_size_limit(sys.maxsize)

totalReal = 0
totalFake = 0
total = 0
EACH = 1000

data = []

with open('data/FakeNewsCorpus.csv', 'rU', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        if len(row) < 16:
            continue
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
        print(row[1])
        total += 1
        if totalFake >= EACH and totalReal >= EACH:
            break

    print("Real: %d" % totalReal)
    print("Fake: %d" % totalFake)
    print("Total: %d" % total)
