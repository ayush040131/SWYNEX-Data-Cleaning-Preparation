import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_titanic.csv")

print("TITANIC DATASET - EXPLORATORY ANALYSIS")

# --------------------------------------------------
# 1. BASIC DATASET INFORMATION
# --------------------------------------------------

print("\nDATASET SHAPE")
print(df.shape)

print("\nBASIC STATISTICS")
print(df.describe())

# --------------------------------------------------
# 2. SURVIVAL BY GENDER
# --------------------------------------------------

print("\nSURVIVAL BY GENDER")

gender_survival = df.groupby("sex")["survived"].mean() * 100
print(gender_survival)

plt.bar(gender_survival.index, gender_survival.values)
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.savefig("charts/survival_by_gender.png")
plt.show()

# --------------------------------------------------
# 3. SURVIVAL BY PASSENGER CLASS
# --------------------------------------------------

print("\nSURVIVAL BY PASSENGER CLASS")

class_survival = df.groupby("pclass")["survived"].mean() * 100
print(class_survival)

plt.bar(class_survival.index.astype(str), class_survival.values)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.savefig("charts/survival_by_class.png")
plt.show()

# --------------------------------------------------
# 4. AVERAGE AGE BY SURVIVAL
# --------------------------------------------------

print("\nAVERAGE AGE BY SURVIVAL")

age_survival = df.groupby("survived")["age"].mean()
print(age_survival)

plt.bar(["Did Not Survive", "Survived"], age_survival.values)
plt.title("Average Age by Survival Status")
plt.xlabel("Survival Status")
plt.ylabel("Average Age (Years)")
plt.savefig("charts/average_age_by_survival.png")
plt.show()

# --------------------------------------------------
# 5. AVERAGE FARE BY SURVIVAL
# --------------------------------------------------

print("\nAVERAGE FARE BY SURVIVAL")

fare_survival = df.groupby("survived")["fare"].mean()
print(fare_survival)

plt.bar(["Did Not Survive", "Survived"], fare_survival.values)
plt.title("Average Fare by Survival Status")
plt.xlabel("Survival Status")
plt.ylabel("Average Fare")
plt.savefig("charts/average_fare_by_survival.png")
plt.show()

# --------------------------------------------------
# 6. SURVIVAL BY TRAVELING ALONE
# --------------------------------------------------

print("\nSURVIVAL BY TRAVELING ALONE")

alone_survival = df.groupby("alone")["survived"].mean() * 100
print(alone_survival)

plt.bar(["With Someone", "Alone"], alone_survival.values)
plt.title("Survival Rate by Traveling Status")
plt.xlabel("Traveling Status")
plt.ylabel("Survival Rate (%)")
plt.savefig("charts/survival_by_traveling_status.png")
plt.show()

# --------------------------------------------------
# 7. ANOMALY CHECK - HIGHEST FARES
# --------------------------------------------------

print("\nHIGHEST FARE VALUES")

high_fares = df.sort_values("fare", ascending=False)[
    ["fare", "pclass", "sex", "age", "survived"]
].head(10)

print(high_fares)

print("\nEXPLORATORY ANALYSIS COMPLETED")