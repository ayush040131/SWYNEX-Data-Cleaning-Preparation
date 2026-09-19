import pandas as pd

df = pd.read_csv("data/titanic.csv")

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())
print("\nUNIQUE VALUES")

print("\nSEX:")
print(df["sex"].unique())

print("\nEMBARKED:")
print(df["embarked"].unique())

print("\nCLASS:")
print(df["class"].unique())

print("\nWHO:")
print(df["who"].unique())

print("\nALIVE:")
print(df["alive"].unique())

print("\nDECK:")
print(df["deck"].unique())
print("\nDUPLICATE ROWS")
print(df[df.duplicated()].head(10))
print("\nALL DUPLICATE ROWS")

duplicates = df[df.duplicated(keep=False)]

print("Rows involved in duplicate groups:", len(duplicates))

print(duplicates.head(20))
print("\nMISSING VALUE PERCENTAGE")

missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage)