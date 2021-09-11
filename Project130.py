import csv
import pandas as pd

df = pd.read_csv('final.csv')
del df['Luminosity']

df = df[df['Star Name'].notna()]
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

print(df)
print(list(df))

df = df.to_csv('cleaned_final.csv')