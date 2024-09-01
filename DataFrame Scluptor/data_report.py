# data_report.py
import pandas as pd

def print_column_info(df):
    print("Column Names with Data Types:")
    print(df.dtypes)

def group_columns_by_type(df):
    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    
    print("\nNumerical Columns:")
    print(numerical_columns)
    
    print("\nCategorical Columns:")
    print(categorical_columns)
    
    return numerical_columns, categorical_columns

def identify_null_columns(df):
    null_columns = df.columns[df.isnull().any()].tolist()
    null_counts = df.isnull().sum()[df.isnull().sum() > 0]
    
    print("\nColumns with Null Values:")
    print(null_counts)
    
    return null_columns

def detect_incorrect_data(df, numerical_columns, categorical_columns):
    incorrect_data = {}
    
    for col in numerical_columns:
        if df[col].dtype == 'object':
            incorrect_data[col] = df[col].unique()
            
    for col in categorical_columns:
        if df[col].dtype != 'object':
            incorrect_data[col] = df[col].unique()
    
    print("\nColumns with Incorrect Data:")
    for col, values in incorrect_data.items():
        print(f"{col}: {values}")
    
    return incorrect_data

def generate_data_report(file_path):
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        
        # Print column names with data types
        print_column_info(df)
        
        # Group columns by data type
        numerical_columns, categorical_columns = group_columns_by_type(df)
        
        # Identify columns with null values
        null_columns = identify_null_columns(df)
        
        # Detect incorrect data
        incorrect_data = detect_incorrect_data(df, numerical_columns, categorical_columns)
        
        # Report summary
        print("\n--- Data Report Summary ---")
        print(f"Total Columns: {df.shape[1]}")
        print(f"Numerical Columns: {len(numerical_columns)}")
        print(f"Categorical Columns: {len(categorical_columns)}")
        print(f"Columns with Null Values: {len(null_columns)}")
        print(f"Columns with Incorrect Data: {len(incorrect_data)}")
        
        # Create a summary DataFrame for column information
        report = pd.DataFrame({
            'Column Name': df.columns,
            'Data Type': df.dtypes,
            'Missing Values': df.isnull().sum(),
            'Unique Values': df.nunique()
        })
        
        return report
    
    except Exception as e:
        print(f"Error generating data report: {e}")
        return None
