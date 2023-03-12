import pandas as pd
from random import random


def selectLetter():
    p = random()/2
    for j in letters:
        p -= df1[j][0]
        if p < 0:
            if j == " " or j is None:
                return selectLetter()
            return j


def selectLength(letter):
    p = random()
    for j in range(27):
        p -= df2[letter][j]
        if p < 0:
            return j
    return 4


def createWord(l, ls):
    pp = 0
    word = l
    while pp < ls-1:
        p = random()
        for j in letters:
            p -= df3[j][letters[l]]
            if p < 0 and j != " ":
                word += j
                l = j
                pp += 1
                break
    return word


df1 = pd.read_csv("Update Data/09_probability_1L.csv")
df2 = pd.read_csv("Update Data/13_word_length_probability.csv")
df3 = pd.read_csv("Update Data/05.1_probability_data.csv")

letters = {' ': 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, 'i': 9, 'j': 10, 'k': 11,
           'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
           'w': 23, 'x': 24, 'y': 25, 'z': 26}

i, text, pre = 0, " ", ""

num = int(input("Enter number of words: "))
ln = int(input("Enter length of words(If want random length enter '0'): "))

if ln == 0:
    while i < num:
        pre = selectLetter()
        ln = selectLength(pre)
        text += (createWord(pre, ln) + " ")
        i += 1
else:
    while i < num:
        pre = selectLetter()
        text += (createWord(pre, ln) + " ")
        i += 1

print(text)
