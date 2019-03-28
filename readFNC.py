import csv
import sys

csv.field_size_limit(sys.maxsize)

real = []
fake = []

with open('data/FakeNewsCorpus.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        if len(row) < 16:
            continue
        if row[3] == 'fake':
            fake.append(row)
        elif row[3] == 'reliable':
            real.append(row)

    print("Real: %d" % len(real))
    print("Fake: %d" % len(fake))
