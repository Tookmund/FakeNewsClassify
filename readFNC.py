import csv
import sys

csv.field_size_limit(sys.maxsize)

totalReal = 0
totalFake = 0

with open('data/FakeNewsCorpus.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) < 3:
            print(row)
            continue
        if row[3] == 'fake':
            totalFake += 1
        elif row[3] == 'reliable':
            totalReal += 1

    print("Real: %d" % totalReal)
    print("Fake: %d" % totalFake)
