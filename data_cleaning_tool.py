import pandas as pd
import numpy as np

def read_csv_file(filename):
    data=pd.read_csv(filename)
    print(f"Loaded: {len(data)} rows, {len(data.columns)} columns")
    return data

def check_missing(data):
    print("\nMissing Values")
    missing=data.isnull().sum()
    print(missing[missing>0])

def handle_missing_data(data):
    print("\nFixing Missing Values")
    for col in data.columns:
        if data[col].isnull().any():
            if data[col].dtype in ['int64','float64']:
                avg=data[col].mean()
                data[col].fillna(avg,inplace=True)
                print(f"Filled {col} with average:{avg:.2f}")
    return data

def delete_duplicate_rows(data):
    print("\nRemoving Duplicates")
    before=len(data)
    data=data.drop_duplicates()
    removed=before-len(data)
    print(f"Removed {removed} duplicate rows")
    return data

def find_outliers(data):
    print("\nFinding Outliers")
    for col in data.select_dtypes(include=[np.number]).columns:
        Q1=data[col].quantile(0.25)
        Q3=data[col].quantile(0.75)
        IQR=Q3-Q1
        lower=Q1 - 1.5 * IQR
        upper=Q3 + 1.5 * IQR
        outliers=((data[col]<lower)|(data[col]>upper)).sum()
        if outliers>0:
            print(f"{col}:{outliers} outliers")

def save_data(data,filename):
    data.to_csv(filename,index=False)
    print(f"\nSaved to {filename}")

if __name__=="__main__":
    sample={
        'ID':[43,8,41,39,26],
        'Score':[98,93,None,78,67],
        'Attendance':[88,92,85,90,78]
    }

    df=pd.DataFrame(sample)
    df.to_csv('test_data.csv',index=False)
    print("\n"+"="*40)
    print("DATA CLEANING STARTED")
    print("="*40)
    data=read_csv_file('test_data.csv')
    check_missing(data)
    data=handle_missing_data(data)
    data=delete_duplicate_rows(data)
    find_outliers(data)
    save_data(data,'cleaned.csv')
    print("Done!")

