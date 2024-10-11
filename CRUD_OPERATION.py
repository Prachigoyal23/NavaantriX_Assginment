# Import the pandas library
import pandas as pd

# Load the dataset from a CSV file
def load_data():
    return pd.read_csv('sales_data_sample.csv')

# Create: Insert new records into the dataset
def create_record(new_record):
    df = load_data()
    df = df.append(new_record, ignore_index=True)
    df.to_csv('sales_data_sample.csv', index=False)
    print("Record added successfully.")

# Read: Retrieve and display specific records from the dataset
def read_records(filter_conditions=None):
    df = load_data()
    if filter_conditions:
        df = df.query(filter_conditions)
    display(df)  # Use display for better formatting in Jupyter

# Update: Modify existing records in the dataset
def update_record(index, updated_data):
    df = load_data()
    if index < len(df):
        for key, value in updated_data.items():
            df.at[index, key] = value
        df.to_csv('sales_data_sample.csv', index=False)
        print("Record updated successfully.")
    else:
        print("Index out of bounds.")

# Delete: Remove specific records from the dataset
def delete_record(index):
    df = load_data()
    if index < len(df):
        df = df.drop(index)
        df.to_csv('sales_data_sample.csv', index=False)
        print("Record deleted successfully.")
    else:
        print("Index out of bounds.")

# Example usage
# Display the current data
print("Current data:")
display(load_data())

# Create a new record (uncomment to run)
 new_record = {
     'ORDERNUMBER': '12346',
     'QUANTITYORDERED': 5,
     'PRICEEACH': 50,
     'ORDERLINENUMBER': 1,
     'SALES': 250,
     'ORDERDATE': '2024-10-10',
     'STATUS': 'Shipped',
     'QTR_ID': 4,
     'MONTH_ID': 10,
     'YEAR_ID': 2024,
     'PRODUCTLINE': 'Classic Cars',
     'MSRP': 60,
     'PRODUCTCODE': 'CAR123',
     'CUSTOMERNAME': 'John Doe',
     'PHONE': '555-1234',
     'ADDRESSLINE1': '123 Elm St',
     'ADDRESSLINE2': '',
     'CITY': 'Metropolis',
     'STATE': 'NY',
     'POSTALCODE': '10001',
     'COUNTRY': 'USA',
     'TERRITORY': 'North America',
     'CONTACTLASTNAME': 'Smith',
     'CONTACTFIRSTNAME': 'Jane',
     'DEALSIZE': 'Small'
 }
 create_record(new_record)

# Read records 
 read_records()  # Display all records
 read_records('STATUS == "Shipped"')  # Display filtered records

# Update a record (assuming a valid index)
 updated_data = {
     'STATUS': 'Delivered',
     'SALES': 300
 }
 update_record(0, updated_data)  # Replace 0 with a valid index

# Delete a record (assuming a valid index)
 delete_record(0)  # Replace 0 with a valid index

    create_record(file_path, new_record)

    # Read records
    read_records(file_path)  # Display all records
    read_records(file_path, 'STATUS == "Shipped"')  # Display filtered records

    # Update a record (assuming index 0 exists)
    updated_data = {
        'STATUS': 'Delivered',
        'SALES': 300
    }
    update_record(file_path, 0, updated_data)

    # Delete a record (assuming index 0 exists)
    delete_record(file_path, 0)
