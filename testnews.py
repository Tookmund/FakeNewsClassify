import subprocess
import readfND as ds

ds.loaddata(False)

TOTAL = 20
correct = 0
for i in range(TOTAL):
    d = ds.data[i]
    subprocess.run(['less'], input=bytes(''.join(d[0]), 'utf-8'))
    inp = input("[r]eal or [f]ake?")
    if inp.startswith('r'):
        if d[1] == 'reliable':
            correct += 1
    elif inp.startswith('f'):
        if d[1] == 'fake':
            correct += 1
print(correct/TOTAL)
