# This is a data cleaning application 

"""
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""

# Importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

def Data_Cleaning(data_path, data_name):
    print("Dataset has been received and is ready for processing.")

    sec = random.randint(1, 4)  # Generating a random number

    # Print delay message
    print(f"Please wait for {sec} seconds! Checking file path...")
    time.sleep(sec)

    # Checking if the path exists
    if not os.path.exists(data_path):
        print("Incorrect path! Please enter the correct path.")
        return  

    # Checking the file type
    if data_path.endswith('.csv'):
        print("Dataset is a CSV file!")
        data = pd.read_csv(data_path, encoding_errors='ignore')

    elif data_path.endswith('.xlsx'):
        print("Dataset is an Excel file!")
        data = pd.read_excel(data_path)

    else:
        print("Unknown file type. Please provide a CSV or Excel file.")
        return  

    # Print delay message
    print(f"Please wait for {sec} seconds! Checking total columns and rows...")
    time.sleep(sec)

    # Showing number of records
    print(f"Dataset contains Total Rows: {data.shape[0]}\nTotal Columns: {data.shape[1]}")

    # Print delay message
    print(f"Please wait for {sec} seconds! Checking for duplicate values...")
    time.sleep(sec)

    # Checking duplicates (Fix applied here)
    duplicates = data.duplicated(keep=False)  # Capture all duplicates including the first occurrence
    total_duplicates = duplicates.sum()
    print(f"Total Number of Duplicate Records: {total_duplicates}")

    # Save the duplicated values
    if total_duplicates > 0:
        duplicates_records = data[duplicates].copy()
        duplicates_records.to_csv(f'{data_name}_duplicates.csv', index=False)
        print(f"Duplicate records saved as: {data_name}_duplicates.csv")
    else:
        print("No duplicate records found.")

    # Removing duplicate values (with .copy() to prevent SettingWithCopyWarning)
    df = data.drop_duplicates().copy()

    # Print delay message
    print(f"Please wait for {sec} seconds! Checking for missing values...")
    time.sleep(sec)

    # Finding missing values
    total_missing_values = df.isnull().sum().sum()
    missing_values_columns = df.isnull().sum()

    print(f"Dataset has Total Missing Values: {total_missing_values}")
    print(f"Missing values per column:\n{missing_values_columns.to_frame()}")

    # Print delay message
    print(f"Please wait for {sec} seconds! Cleaning dataset...")
    time.sleep(sec)

    # Handling missing values (avoid SettingWithCopyWarning)
    for col in df.columns:
        if df[col].dtype in (float, int):
            # Fill missing numeric values with column mean
            df.loc[:, col] = df[col].fillna(df[col].mean())  
        else:
            # Handling missing categorical values
            if df[col].nunique() > 0:  
                # Fill categorical missing values with the most frequent value (mode)
                df.loc[:, col] = df[col].fillna(df[col].mode()[0])
            else:
                # If no mode is found (all values are NaN), fill with "Unknown"
                df.loc[:, col] = df[col].fillna("Unknown")

    # Print delay message
    print(f"Please wait for {sec} seconds! Exporting cleaned dataset...")
    time.sleep(sec)

    # Data is cleaned
    print(f"Congrats! Dataset is cleaned! \nNumber of Rows: {df.shape[0]}, Number of Columns: {df.shape[1]}")

    # Saving the cleaned dataset
    df.to_csv(f'{data_name}_Clean_data.csv', index=False)
    print(f"Cleaned dataset saved as: {data_name}_Clean_data.csv")

if __name__ == "__main__":
    print("Welcome to Data Cleaning Master!")
    
    # Ask for path and file name
    data_path = input("Please enter the dataset path: ")
    data_name = input("Please enter the dataset name (without extension): ")
    
    # Calling the function
    Data_Cleaning(data_path, data_name)

# Run This Code in Your Terminal
