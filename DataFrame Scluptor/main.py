import data_collection as dc
import data_report as dr
import data_cleaning as cl

def main():
    # Load the dataset
    csv_path = 'surat_uncleaned.csv'
    data = dc.load_csv(csv_path)
    
    # Generate data report
    report = dr.generate_data_report(csv_path)
    
    if report is None:
        print("Failed to generate data report.")
        return
    
    print("Data Report:")
    print(report)
    
    # Display columns with their order numbers
    print("Columns available for cleaning:")
    for i, col in enumerate(report['Column Name'].tolist()):
        print(f"{i + 1}. {col}")
    
    # Allow user to specify which columns to clean by number
    selected_numbers = input("Enter column numbers to clean (comma-separated): ").split(',')

    # Clean and convert specified columns
    for num in selected_numbers:
        try:
            index = int(num.strip()) - 1  # Convert to zero-based index
            if 0 <= index < len(data.columns):
                col = data.columns[index]
                data = cl.clean_numeric_column(data, col)
                print(f"Cleaned column: {col}")
            else:
                print(f"Invalid column number: {num}")
        except ValueError:
            print(f"Invalid input: {num}")

    # Save the cleaned data back to CSV
    cleaned_csv_path = 'surat_uncleaned.csv'
    data.to_csv(cleaned_csv_path, index=False)
    print(f"Cleaned data saved to {cleaned_csv_path}")

    # Print cleaned data for verification
    print("Cleaned Data:")
    print(data.head())

if __name__ == "__main__":
    main()
