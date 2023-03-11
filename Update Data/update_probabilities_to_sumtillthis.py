import pandas as pd

file = "05_probability_data.csv"
df = pd.read_csv(file)

indices = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in indices:
    for j in range(27):
        l = indices[indices.index(i) - 1]
        if i != "a":
            df[i][j] = df[i][j] - df[l][j]

df.to_csv(file, index=False)

file = "09_probability_1L.csv"
df = pd.read_csv(file)

for i in indices:
    j = 0
    l = indices[indices.index(i) - 1]
    if i != "a":
        df[i][j] = df[i][j] - df[l][j]

df.to_csv(file, index=False)
