# data_cleaning.py
import pandas as pd
import re

def clean_numeric_column(df, column):
    """
    Cleans a specified column in the DataFrame by removing non-numeric characters and converting it to numeric type.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    column (str): The column name to clean.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame with the specified column converted to numeric.
    """
    # Remove non-numeric characters
    df[column] = df[column].apply(lambda x: re.sub(r'[^0-9.]', '', str(x)))
    # Convert to numeric, setting errors='coerce' to handle conversion issues
    df[column] = pd.to_numeric(df[column], errors='coerce')
    
    return df

# Placeholder functions for other data cleaning tasks
def handle_missing_values(df, strategy='mean'):
    # Implementation for handling missing values
    pass

def remove_outliers(df, column):
    # Implementation for removing outliers
    pass

def normalize_data(df, columns):
    # Implementation for normalizing data
    pass


# print(df.head())