import pandas as pd

df = pd.read_csv("03_data.csv")
df = df.transpose()
sums = df.sum()
print(sums)
df = df.transpose()

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
# df.to_csv("05_probability_data.csv", index=False)

df1 = pd.read_csv("05_probability_data.csv")
for i in indices:
    for j in range(27):
        df1[i][j] = int(df[i][j]) / int(sums[j])

df1.to_csv("05_probability_data.csv", index=False)
