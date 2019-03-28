import csv

totalReal = 0
totalFake = 0

with open('data/FakeNewsCorpus.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) < 3:
            print row
        if row[3] == 'fake':
            totalFake += 1
        elif row[3] == 'reliable':
            totalReal += 1

    print "Real: %d" % totalReal
    print "Fake: %d" % totalFake
