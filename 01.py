import pandas as pd

df = pd.read_csv("StudentsPerformance (1).csv")

# columnas específicas + primeras 12 filas
print(df[['gender', 'lunch', 'math score']].head(12))

# últimas 8 filas
print(df[['gender', 'lunch', 'math score']].tail(8))
