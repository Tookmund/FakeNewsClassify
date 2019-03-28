import csv
import sys

csv.field_size_limit(sys.maxsize)

totalReal = 0
totalFake = 0

data = []

with open('data/FakeNewsCorpus.csv', 'rU') as csvfile:
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
        data.append((row[5], row[3]))

    print("Real: %d" % totalReal)
    print("Fake: %d" % totalFake)
