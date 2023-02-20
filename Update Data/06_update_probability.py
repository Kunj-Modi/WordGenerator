import pandas as pd

df = pd.read_csv("03_data.csv")
df = df.transpose()
sums = df.sum()
print(sums)
df = df.transpose()

indices = {' ': 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, 'i': 9, 'j': 10, 'k': 11,
           'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
           'w': 23, 'x': 24, 'y': 25, 'z': 26}

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
# df.to_csv("05_probability_data.csv", index=False)

df1 = pd.read_csv("05_probability_data.csv")
for i in indices:
    for j in range(27):
        df1[i][j] = int(df[i][j]) / int(sums[j])

df1.to_csv("05_probability_data.csv", index=False)
