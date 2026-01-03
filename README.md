# Data Cleaning and Preprocessing Tool

## Overview
This tool automates data cleaning tasks like handling missing values,removing duplicates and detecting outliers.It makes datasets ready for machine learning and analysis by addressing common data quality issues found in real-world datasets.

## Problem Statement
Real-world datasets often have quality issues like:
- Missing values (empty cells)
- Duplicate records 
- Outliers (unusual extreme values)

These issues can reduce the accuracy of machine learning models.This tool solves these problems automatically,making data preprocessing faster and more reliable.

## Features
1. **Missing Value Detection** - Identifies which columns have missing data
2. **Missing Value Handling** -Fills missing numeric values with column average
3. **Duplicate Removal** - Finds and removes duplicate rows automatically
4. **Outlier Detection** - Uses IQR(Interquartile Range) method to find unusual values
5. **Data Export** - Saves cleaned data to CSV file for further use

## Technologies Used
- **Python** -Programming Language
- **Pandas** -Data manipulation and CSV file handling
- **Numpy** -Numerical calculations for outlier detection

## Installation 

### Prerequisites
Make sure Python 3 is installed on your system.

### Install Required Libraries
```bash
pip install pandas numpy
```

## Output
The cleaned dataset is saved as `cleaned.csv` and displays a summary showing:
- Number of rows and columns loaded
- Missing values found and filled
- Duplicate rows removed
- Outliers detected in each column

## Application
This tool can be used by data scientists and analysts to automate the data preprocessing step, saving time and ensuring better data quality for machine learning models.