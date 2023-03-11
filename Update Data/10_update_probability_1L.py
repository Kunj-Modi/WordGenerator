import pandas as pd

indices = [' ', "a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# p = {}
# for i in indices:
#     p[i] = [0]
#
# df = pd.DataFrame(p)
# df.to_csv("09_probability_1L.csv", index=False)

df = pd.read_csv("07_1L_data.csv")
df = df.transpose()
sums = df.sum()
Nletters = sums[0]
print(Nletters)
df = df.transpose()

df1 = pd.read_csv("09_probability_1L.csv")

for i in indices:
    df1[i][0] = int(df[i][0]) / Nletters

df1.to_csv("09_probability_1L.csv", index=False)
