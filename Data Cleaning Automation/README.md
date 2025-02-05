# 🚀 Data Cleaning Master

## 📝 Overview

<img width="900" alt="Data Cleaning" src="image/1719422688409.png" />

The **Data Cleaning Master** is a Python application designed to efficiently clean datasets by handling duplicates, missing values, and providing a cleaned output within seconds. This application is user-friendly, highly performant, and has been tested on various datasets to ensure smooth execution and accuracy.

This tool can handle datasets with thousands of rows and quickly clean them without errors. It keeps a backup of duplicate records, replaces missing numeric values with column means, and replaces missing non-numeric values with the most frequent value (mode). It is an excellent solution for **data preprocessing** in data analysis workflows.

## 🎯 Objectives

The key objectives of this project are:

- 📂 Load and clean datasets in **various formats** (CSV and Excel).
- 🗑️ Identify and **remove duplicate records**, while keeping a backup of these duplicates.
- 🔄 Handle missing values:
  - 🔢 **For numeric columns**: Replace missing values with the column's **mean**.
  - 🔡 **For non-numeric columns**: Replace missing values with the **most frequent value (mode)**.
- 💾 Save the cleaned dataset and provide access to both the **cleaned data** and **duplicate records**.

## ⚙️ Project Requirements

To run this project, ensure you have the following dependencies installed:

To run this project, ensure you have the following dependencies installed:

- 🐍 **Python 3.x**
- 📊 **Pandas**
- 🔢 **Numpy**
- 📜 **Openpyxl** (for handling Excel files)
- 📘 **Xlrd** (for reading Excel files)
- 🖥️ **OS library** (for path verification)
- 📓 **Jupyter Notebook** (optional, for testing purposes)

You can install the required dependencies using:

```bash
pip install pandas numpy openpyxl xlrd
```

### 🔄 Alternate Installation (Using Conda)
If you encounter issues with `openpyxl` requiring an updated version, you can use Conda:

```bash
conda config --add channels conda-forge 
conda install openpyxl=3.1.0
```

## 🔄 Step-by-Step Process

### 1️⃣ Input and File Verification

- 🏗️ The application prompts the user for the **dataset path** and **dataset name**.
- 🔍 It verifies if the path is valid and checks whether the file format is **CSV or Excel**.

### 2️⃣ Duplicate Detection and Removal

- 🔄 The application checks for **duplicate records** in the dataset.
- 💾 Duplicate records are saved as a **separate file** named `{dataset_name}_duplicates.csv`.
- 🗑️ Duplicate rows are then removed from the main dataset.

### 3️⃣ Handling Missing Values

- 🔍 The application scans the dataset for **missing values**.
- 🔢 **For numeric columns (integers or floats)**: Missing values are replaced with the column’s **mean**.
- 🔡 **For non-numeric columns**: Missing values are replaced with the **most frequent value (mode)**.

### 4️⃣ Exporting Clean Data

- 💾 The cleaned dataset is saved as `{dataset_name}_Clean_data.csv`.
- ✅ A message confirms that the dataset has been cleaned successfully.

### 5️⃣ Multiple Testing & Performance Tuning

- 🏎️ The application has been **tested on more than 5 datasets**, each containing over **10,000 rows**.
- ⚡ It consistently cleaned datasets **within seconds**, without errors.
- 🔬 The program was also tested in **Jupyter Notebook**, proving seamless integration with **data science workflows**.

## 🌟 Key Features

✅ **Fast & Efficient**: Cleans large datasets (10k+ rows) in seconds.\
✅ **Duplicate Backup**: Saves duplicate records separately before removing them.\
✅ **Missing Values Handling**: Automatically fills missing numeric values and replaces missing non-numeric values with the most frequent value.\
✅ **User-Friendly Prompts**: Guides the user with step-by-step instructions.\
✅ **Multiple Formats Supported**: Handles both **CSV and Excel** files seamlessly.

## 🛠️ Usage

To run the application, simply execute the script in a Python environment:

```bash
python data_cleaning_master.py
```

### 🖥️ Example Execution

```
🚀 Welcome to Data Cleaning Master!
📂 Please enter dataset path: /usr/Desktop/amazon.csv
📄 Please enter dataset name: amazon_sales_data
```

#### 🎯 Expected Output

```
✅ Dataset is a CSV file!
⏳ Please wait for 3 seconds! Checking file path...
📊 Please wait for 2 seconds! Checking total columns and rows...
📈 Dataset contains Total Rows: 10500
📊 Total Columns: 12
🔍 Please wait for 3 seconds! Checking for duplicate values...
🔄 Total Number of Duplicate Records: 320
💾 Duplicate records saved as: amazon_sales_data_duplicates.csv
⏳ Please wait for 2 seconds! Checking for missing values...
❌ Dataset has Total Missing Values: 57
⚡ Please wait for 3 seconds! Cleaning dataset...
🎉 Congrats! Dataset is cleaned!
📊 Number of Rows: 10180, Number of Columns: 12
💾 Cleaned data saved as: amazon_sales_data_Clean_data.csv
```

## 🚀 Final Thoughts

The **Data Cleaning Master** is an efficient tool for **data pre-processing**. Its ability to handle large datasets, clean data accurately, and **save duplicate records for further inspection** makes it an ideal solution for **data science and data analysis projects**. 🔥

