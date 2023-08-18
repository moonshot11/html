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
        with open(f"animals/a{count}.txt", "w") as fout:
            fout.write(str(line))
        count += 1
