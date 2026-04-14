import pandas as pd

df = pd.read_csv("StudentsPerformance (1).csv")

# últimas 3 columnas
ultimas_3 = df.iloc[:, -3:]
print(ultimas_3)

# verificar espacios vacíos
print(df.isnull().sum())

# cantidad total de vacíos
print("Total vacíos:", df.isnull().sum().sum())

# tipo de dato de la última columna
print("Tipo de dato última columna:", df.iloc[:, -1].dtype)