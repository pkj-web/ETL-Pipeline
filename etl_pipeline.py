# Step 1: Extract
import pandas as pd

df = pd.read_csv('data/2020-2025.csv')
print(df.head())


# Step 2: Transform

# --- 1. Check for missing values ---
# Counts the number of missing (NaN) values in each column
print("Missing values per column:")
print(df.isnull().sum())
print()

# --- 2. Check for duplicate rows ---
# Counts how many rows are exact duplicates
print("Number of duplicate rows:")
print(df.duplicated().sum())
print()

# --- 3. Check data types ---
# Displays the data type of each column
print("Data types of each column:")
print(df.dtypes)
print()

# --- 4. Check for outliers / invalid values ---
# Shows basic statistics; can help identify extreme or invalid values
print("Summary statistics (numerical columns):")
print(df.describe())
print()

# --- 5. Check for inconsistent formatting in categorical columns ---
# Lists unique values in each object/string column
for col in df.select_dtypes(include='object').columns:
    print(f"Unique values in '{col}':")
    print(df[col].unique())
    print()

# --- 6. Check for index/key issues ---
# Checks if a column (e.g., 'id') is unique
if 'id' in df.columns:
    print("Unique IDs check:")
    print(df['id'].is_unique)
    print()

# --- 7. Check for unnecessary or empty columns ---
# Lists columns that are completely empty
print("Empty columns:")
print([col for col in df.columns if df[col].isnull().all()])
print()

# --- 8. Check date/time columns ---
# Converts date columns to datetime to find parsing issues
for col in df.select_dtypes(include='object').columns:
    try:
        parsed = pd.to_datetime(df[col], errors='coerce')
        if parsed.notnull().sum() > 0:
            print(f"Date column '{col}' successfully parsed to datetime.")
    except:
        pass