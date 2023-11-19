#!python

#
# Generate food
#

import itertools
import random

AT_BYTE = 64
POUND_BYTE = 35
SPACE_BYTE = 32
UTF = "utf_8_sig"

words = {}

def readfile(filename):
    result = []
    with open(filename, 'rb') as fh:
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

def gen_file(keys, filename, preamble='', emoji_postprocess=False ):
    idx = 0
    valid = [words[k] for k in keys]

    for items in itertools.product(*valid):
        buf = bytes(preamble, encoding=UTF)
        adj, noun = items

        article = ""
        if noun[0] == AT_BYTE:
            noun = noun[1:]
            if adj[0] == POUND_BYTE:
                adj = adj[1:]
                article = "an "
            else:
                article = "a "
        if adj[0] == POUND_BYTE:
            adj = adj[1:]
        if emoji_postprocess:
            noun_bd = noun.rfind(SPACE_BYTE) + 1
            adj_bd = adj.rfind(SPACE_BYTE) + 1
            noun = noun[:noun_bd] + adj[adj_bd:] + noun[noun_bd:]
            adj = adj[:adj_bd]
        else:
            adj += b" "
        buf += bytes(article, encoding=UTF) + adj + noun
        with open(f"{filename}{idx}.fd", "wb") as fh:
            fh.write(buf)
        idx += 1

    print(f"{filename}: {idx-1}")

if __name__ == "__main__":
    init_data()
    gen_file( ["app_type", "app_base"], "app", preamble="prepared ", emoji_postprocess=True )
    gen_file( ["main_cook", "main_food"], "mainA", preamble="followed by " )
    gen_file( ["main_amt", "main_add"], "mainB", preamble="cooked with " )
    gen_file( ["des_flavor", "des_food"], "des", preamble="Dessert was ", emoji_postprocess=True )
