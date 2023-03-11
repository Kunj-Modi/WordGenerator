import pandas as pd
from random import randint

df = pd.read_csv("Update Data/05_probability_data.csv")

text, pre, i, w = "", 0, 0, 5

indices = {0: ' ', 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: 'i', 10: 'j', 11: 'k',
           12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v',
           23: 'w', 24: 'x', 25: 'y', 26: 'z'}

while i < 10000:
    k = randint(1, 100)
    for j in indices:
        k -= df[indices[j]][pre] * 100
        if k < 0:
            text += indices[j]
            w -= 1
            if text[-1] == " ":
                w = randint(5, 10)
            pre = j
            break
        if w <= 0:
            text += " "
            w = randint(8, 12)
    i += 1

print(text)
