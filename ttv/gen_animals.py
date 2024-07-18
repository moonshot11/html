#!python

import sys

if len(sys.argv) >= 2:
    bases = [ sys.argv[1] ]
else:
    bases = [ "animals", "spooky", "askcat", "xmas", "nice_kai", "onetime", "boujie" ]


for base in bases:
    print(f"Generating {base}...")
    filename = base + ".txt"
    with open(filename, "rb") as fin:
        count = 0
        for line in fin.readlines():
            line = line.strip()
            if not line:
                continue
            with open(f"{base}/a{count}.txt", "wb") as fout:
                fout.write(line)
            count += 1
