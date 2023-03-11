import pandas as pd

file = "13_word_length_probability.csv"

df = pd.read_csv("11_word_length_data.csv")
sums = df.sum()

indices = [' ', "a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# p = []
# for i in range(27):
#     p.append([])
#     for j in range(27):
#         p[i].append(0)
# columns_ = [' ', "a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# df = pd.DataFrame(p, columns=columns_)
# df.to_csv(file, index=False)

df1 = pd.read_csv(file)
for i in indices:
    for j in range(27):
        if sums[i] != 0:
            df1[i][j] = int(df[i][j]) / int(sums[i])

df1.to_csv(file, index=False)
