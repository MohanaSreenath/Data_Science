import pandas as pd
from sqlalchemy import create_engine

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data from CSV file: {e}")
        return None

def load_excel(file_path, sheet_name=None):
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Data loaded successfully from {file_path}, sheet: {sheet_name}")
        return data
    except Exception as e:
        print(f"Error loading data from Excel file: {e}")
        return None

def load_sql(connection_string, query):
    try:
        engine = create_engine(connection_string)
        data = pd.read_sql(query, engine)
        print("Data loaded successfully from SQL database")
        return data
    except Exception as e:
        print(f"Error loading data from SQL database: {e}")
        return None

def select_dataset(csv_path, excel_path, excel_sheet, sql_connection, sql_query):
    """
    Display a menu to select a dataset to process.
    """
    datasets = {
        "1": {"name": "CSV", "loader": load_csv, "params": [csv_path]},
        "2": {"name": "Excel", "loader": load_excel, "params": [excel_path, excel_sheet]},
        "3": {"name": "SQL", "loader": load_sql, "params": [sql_connection, sql_query]}
    }

    print("Select the dataset to process:")
    for key, value in datasets.items():
        print(f"{key}. {value['name']}")

    choice = input("Enter the number of your choice: ")

    if choice in datasets:
        selected_data = datasets[choice]["loader"](*datasets[choice]["params"])
        return selected_data
    else:
        print("Invalid choice. Please select a valid option.")
        return None
