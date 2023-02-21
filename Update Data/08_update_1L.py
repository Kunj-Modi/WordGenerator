import pandas as pd

# p = {}
# indices = [' ', "a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for i in indices:
#     p[i] = [0]
#
# df = pd.DataFrame(p)
# df.to_csv("07_1L_data.csv", index=False)

with open("01_data.txt") as text:
    data = text.read()

indices = {' ': 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, 'i': 9, 'j': 10, 'k': 11,
           'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
           'w': 23, 'x': 24, 'y': 25, 'z': 26}

df = pd.read_csv("07_1L_data.csv")

pre = " "
kiki = True
for i in data:
    if kiki:
        pre = i
        kiki = False
        df[i][0] += 1
    if i == " ":
        kiki = True

df.to_csv("07_1L_data.csv", index=False)
