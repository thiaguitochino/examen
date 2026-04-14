import pandas as pd

df = pd.read_csv("StudentsPerformance (1).csv")

# primeras 2 columnas
primeras_2 = df.iloc[:, :2]

print(primeras_2)

# tipo de dato
print(primeras_2.dtypes)

# últimas 10 filas
print(primeras_2.tail(10))