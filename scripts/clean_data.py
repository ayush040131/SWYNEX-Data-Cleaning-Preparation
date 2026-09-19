import pandas as pd

# Load the original dataset
df = pd.read_csv("data/titanic.csv")

print("ORIGINAL DATASET")
print("Rows and columns:", df.shape)

# 1. Remove duplicate records
df = df.drop_duplicates()

print("\nAFTER REMOVING DUPLICATES")
print("Rows and columns:", df.shape)

# 2. Fill missing age values with the median age
df["age"] = df["age"].fillna(df["age"].median())

# 3. Fill missing embarked values with the most common value
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# 4. Fill missing embark_town values with the most common value
df["embark_town"] = df["embark_town"].fillna(df["embark_town"].mode()[0])

# 5. Remove deck because most of its values are missing
df = df.drop(columns=["deck"])

# 6. Remove any duplicate records created after cleaning
df = df.drop_duplicates()

# Save the cleaned dataset
df.to_csv("data/cleaned_titanic.csv", index=False)

print("\nCLEANED DATASET")
print("Rows and columns:", df.shape)

print("\nREMAINING MISSING VALUES")
print(df.isnull().sum())

print("\nCLEANED DATASET SAVED SUCCESSFULLY")
