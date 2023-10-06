#!python

import sys

#
# gen_animals.py
#

count = 0
filename = sys.argv[1] if len(sys.argv) >= 2 else "animals.txt"
destpath = sys.argv[2] if len(sys.argv) >= 3 else "animals"

with open(filename, "rb") as fin:
    for line in fin.readlines():
        line = line.strip()
        if not line:
            continue
        with open(f"{destpath}/a{count}.txt", "wb") as fout:
            fout.write(line)
        count += 1
