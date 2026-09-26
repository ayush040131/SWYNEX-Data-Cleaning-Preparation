# Titanic Dataset Data Cleaning Project

## 1. Project Overview

This project focuses on cleaning and preparing the Titanic dataset using Python and Pandas.

The dataset was inspected for:
- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent values

The original dataset was kept unchanged, and a separate cleaned dataset was created.

## 2. Tools Used

- Python
- Pandas
- NumPy
- VS Code

## 3. Dataset

The Titanic dataset is a publicly available dataset containing information about passengers on the Titanic.

Original dataset:
- Rows: 891
- Columns: 15

## 4. Data Problems Identified

### Missing Values

Missing values were found in:

- `age` - 177 missing values
- `embarked` - 2 missing values
- `deck` - 688 missing values
- `embark_town` - 2 missing values

### Duplicate Records

The dataset contained 107 duplicate records according to Pandas' duplicate-record check.

### Incorrect Data Types

The data types of the columns were inspected. No major incorrect data types requiring conversion were identified.

### Inconsistent Values

Categorical columns such as `sex`, `embarked`, `class`, `who`, and `alive` were checked for inconsistent values. No obvious formatting inconsistencies were found.

## 5. Cleaning Steps

The following cleaning operations were performed:

1. Duplicate records were removed.
2. Missing `age` values were replaced with the median age.
3. Missing `embarked` values were replaced with the most common value.
4. Missing `embark_town` values were replaced with the most common value.
5. The `deck` column was removed because approximately 77% of its values were missing.
6. Duplicate records were checked and removed again after the cleaning operations.
7. The cleaned dataset was saved as `cleaned_titanic.csv`.

## 6. Final Dataset

After cleaning:

- Final rows: 780
- Final columns: 14
- Missing values: 0
- Duplicate records: 0

The cleaned dataset is available in:

`data/cleaned_titanic.csv`

## 7. Project Structure

```text
Data_Cleaning_Internship/
│
├── data/
│   ├── titanic.csv
│   └── cleaned_titanic.csv
│
├── scripts/
│   ├── inspect_data.py
│   └── clean_data.py
│
├── notebooks/
│
└── README.md

# Task 2 - Exploratory Data Analysis

## 9. Exploratory Analysis

The cleaned Titanic dataset from Task 1 was analyzed using Python, Pandas, and Matplotlib.

The analysis focused on:
- Basic statistical summaries
- Survival patterns
- Passenger class
- Gender
- Age
- Fare
- Traveling alone
- Potential anomalies

## 10. Key Insights

### Insight 1: Survival by Gender

Female passengers had a survival rate of approximately 73.97%, while male passengers had a survival rate of approximately 21.72%.

This shows a substantial difference in survival rates between the two gender groups in the dataset.

### Insight 2: Survival by Passenger Class

First-class passengers had a survival rate of 63.68%, second-class passengers had a survival rate of 50.61%, and third-class passengers had a survival rate of 25.74%.

The dataset therefore shows a clear association between passenger class and survival.

### Insight 3: Average Age by Survival

Passengers who survived had an average age of 28.33 years, while passengers who did not survive had an average age of 30.50 years.

The difference is relatively small, so age alone does not appear to show a strong difference in this simple comparison.

### Insight 4: Average Fare by Survival

Passengers who survived paid an average fare of approximately 50.19, compared with 24.03 for passengers who did not survive.

This shows an association between fare level and survival in the dataset. Fare may also be related to passenger class.

### Insight 5: Survival by Traveling Status

Passengers traveling with someone had a survival rate of 51.18%, compared with 33.71% for passengers traveling alone.

This indicates an association between traveling status and survival in the dataset.

## 11. Anomaly Identified

The dataset contains unusually high fare values.

The median fare was 15.95, while the maximum fare was 512.3292.

The highest fare values were associated with first-class passengers. These values were retained because they may represent genuine high-priced tickets and were not identified as data-entry errors.

Therefore, these observations were treated as potential outliers rather than incorrect data.

## 12. Charts

The following charts were created using Matplotlib:

1. Survival Rate by Gender
2. Survival Rate by Passenger Class
3. Average Age by Survival Status
4. Average Fare by Survival Status
5. Survival Rate by Traveling Status

## 13. Conclusion

Exploratory analysis revealed several patterns in the cleaned Titanic dataset. Survival rates varied substantially by gender and passenger class. Differences were also observed based on fare and traveling status, while the average age difference between survivors and non-survivors was relatively small.

The analysis demonstrates how Python, Pandas, and Matplotlib can be used to summarize data, identify patterns, visualize relationships, and investigate potential anomalies.

## Task 3 – Interactive Power BI Dashboard

### Objective

Create an interactive dashboard using Power BI to communicate the main findings from the cleaned Titanic dataset.

### Tool Used

- Microsoft Power BI Desktop

### Dashboard Pages

#### Page 1 – Titanic Passenger Dashboard

The overview page contains the following KPI cards:

- Total Passengers: 780
- Total Survivors: 322
- Survival Rate: 41.28%
- Average Fare: 34.83

#### Page 2 – Titanic Survival Analysis

The analysis page contains interactive filters and charts.

### Interactive Filters

- Gender
- Passenger Class
- Traveling Status

### Visualizations

- Survival Rate by Gender
- Survival Rate by Passenger Class
- Survival Rate by Traveling Status
- Average Fare by Survival Status
- Average Age by Survival Status

### Key Features

- Interactive slicers for filtering the dashboard
- KPI cards for important summary statistics
- Charts for identifying survival patterns
- Data labels for easier interpretation
- Separate overview and analysis pages
- Dashboard created using the cleaned dataset from Task 1

### Dashboard File

Power BI dashboard file:

`SWYNEX_Titanic_Interactive_Dashboard.pbix`