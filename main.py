import numpy as np
import pandas as pd

matrix = []
with open("final2D.msh", "r") as f:
     data = f.readlines()

add = False
for row in data:
    if row == "$Entities\n":
        add = True
    if row == "$EndEntities\n":
        add = False
    if add and row not in {"$Entities\n","$EndEntities\n"}:
        row = row.strip(',')
        row = row.split()
        row = list(map(float, row))
        matrix.append(row)

df = pd.DataFrame(matrix)
df.rename(columns = {0:'identifier'},
            inplace = True)

print(df)
