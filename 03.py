import pandas as pd

df = pd.read_csv("StudentsPerformance (1).csv")

# columna reading score
reading = df['reading score']

print(reading)

# cantidad de datos
print("Cantidad:", reading.count())

# suma total
print("Suma:", reading.sum())