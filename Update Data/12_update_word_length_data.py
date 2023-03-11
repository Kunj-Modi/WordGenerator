import pandas as pd

file = "11_word_length_data.csv"

# p = []
# for i in range(27):
#     p.append([])
#     for j in range(27):
#         p[i].append(0)
# indices = [' ', "a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# columns_ = [' ', "a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# df = pd.DataFrame(p, columns=columns_)
# df.to_csv(file, index=False)

with open("01_data.txt") as text:
    data = text.read()

df = pd.read_csv(file)

pre = " "
wl = 0
new_word = True
for i in data:
    if new_word:
        pre = i
        new_word = False
        try:
            df[pre][wl] += 1
        except KeyError:
            df[pre][wl] = 1
        wl = 0
    if i == " ":
        new_word = True
    else:
        wl += 1

df.to_csv(file, index=False)
