import pandas as pd

'''Data about first letter'''

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

df = pd.read_csv("07_1L_data.csv")

pre = " "
new_word = True
for i in data:
    if new_word:
        pre = i
        new_word = False
        df[i][0] += 1
    if i == " ":
        new_word = True

df.to_csv("07_1L_data.csv", index=False)
