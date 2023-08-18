#!python

#
# gen_animals.py
#

count = 0

with open("animals.txt", "rb") as fin:
    for line in fin.readlines():
        line = line.strip()
        if not line:
            continue
        with open(f"animals/a{count}.txt", "wb") as fout:
            fout.write(line)
        count += 1
