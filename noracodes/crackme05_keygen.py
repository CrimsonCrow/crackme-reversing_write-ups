import random

def part1():
    while True:
        p = ""
        s = 0
        p += random.choice(ch)
        p += random.choice(ch)
        p += 'B'
        p += random.choice(ch)
        for c in p:
            s += ord(c)
        if s % 3 == 0:
            return p

def part2():
    while True:
        p = ""
        s = 0
        p += random.choice(ch)
        p += random.choice(ch)
        p += random.choice(ch)
        p += random.choice(ch)
        for c in p:
            s += ord(c)
        if s % 4 == 0:
            return p

def part3():
    while True:
        p = ""
        s = 0
        p += random.choice(ch)
        p += random.choice(ch)
        p += random.choice(ch)
        p += random.choice(ch)
        for c in p:
            s += ord(c)
        if s % 5 == 0:
            return p

def part4():
    while True:
        p = ""
        s = 0
        p += random.choice(ch)
        p += 'Q'
        p += random.choice(ch)
        p += random.choice(ch)
        for c in p:
            s += ord(c)
        if s % 4 == 0:
            return p


def keygen():
    while True:
        p1 = part1()
        p2 = part2()
        p3 = part3()
        p4 = part4()
        key = p1+p2+p3+p4
        print (key)


ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
keygen()
