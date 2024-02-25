import pandas as pd

df = pd.read_excel('Sales.xlsx')

df_filtered =df[df['Sales'] == 969]

print(df_filtered)
df_filtered.to_excel('xyz.xlsx',index=False)