import random

def keygen():
    key = ""
    score = 0
    while True:
        while len(key) < key_len:
            key += random.choice(characters)
        for c in key:
            score += ord(c)
        #print ("debug: ", key, score)
        if score == total_score:
            print (key)
        key = ""
        score = 0

total_score = 1762
characters = "abcdefghijklmnopqrstuvwxyz"
key_len = 16
keygen()
