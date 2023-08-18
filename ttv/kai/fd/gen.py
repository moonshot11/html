#!python

#
# Generate food
#

import random

words = {}

def readfile(filename):
    result = []
    with open(filename, 'r') as fh:
        result = [line.strip() for line in fh.readlines() if line.strip()]
    return result

def init_data():
    keys = ("app_base", "app_type",
            "des_flavor", "des_food",
            "main_add", "main_amt", "main_cook", "main_food")
    for key in keys:
        terms = readfile(f"{key}.txt")
        words[key] = terms

def pick(key):
    return random.choice(words[key])

def gen_files():
    for key in words:
        for i, term in enumerate(words[key]):
            with open(f"{key}_{i}.fd", "w") as fh:
                fh.write(term)

if __name__ == "__main__":
    init_data()
    gen_files()
    buf = f"USER prepares a {pick('app_type')} {pick('app_base')} for USER2, followed by a main course of {pick('main_cook')} {pick('main_food')} in {pick('main_add')} with {pick('main_amt')} of {pick('main_add')}. For dessert, USER prepared a {pick('des_flavor')} {pick('des_food')}. Yum!"

    print(buf)
