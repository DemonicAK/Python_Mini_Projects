"""
CSV File Duplicate Row Remover

This script reads a CSV file, removes duplicate rows, and saves the cleaned data to a new CSV file.

Usage:
    Ensure you have pandas installed: pip install pandas
    Place this script in the same directory as your input CSV file or provide the full path.
    Run the script: python script_name.py

Input:
    bitwarden_export_20240906212941.csv - The input CSV file to be cleaned.

Output:
    output_cleaned.csv - The cleaned CSV file with duplicate rows removed.

Dependencies:
    pandas - Used for CSV file handling and data manipulation.

"""

import pandas as pd

# Read the CSV file
df = pd.read_csv('german_english_words.csv')
# Note: 'bitwarden_export_20240906212941.csv' is the input file name. Adjust if necessary.

# Remove duplicate rows
df_cleaned = df.drop_duplicates()
# This creates a new DataFrame with duplicate rows removed.

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('output_cleaned.csv', index=False)
# The cleaned data is saved to 'output_cleaned.csv'. The index=False parameter
# ensures that pandas doesn't write row indices to the output file.

# Print statistics about the cleaning process
print(f"Original row count: {len(df)}")
print(f"Cleaned row count: {len(df_cleaned)}")
print(f"Removed {len(df) - len(df_cleaned)} duplicate rows")
# These print statements provide information about the number of rows in the
# original dataset, the cleaned dataset, and how many duplicate rows were removed.
