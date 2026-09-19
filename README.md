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