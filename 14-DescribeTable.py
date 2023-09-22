import boto3
from prettytable import PrettyTable
from datetime import datetime, timezone, timedelta

# Initialize DynamoDB client
db = boto3.client('dynamodb')

# Define the table name
table_name = 'Account'

try:
    # Describe the table
    response = db.describe_table(TableName=table_name)

    # Extract relevant data
    table_data = response['Table']
    fields = table_data['AttributeDefinitions']
    table_arn = table_data['TableArn']
    table_status = table_data['TableStatus']
    creation_date_time = table_data['CreationDateTime']
    read_capacity_units = table_data['ProvisionedThroughput']['ReadCapacityUnits']
    write_capacity_units = table_data['ProvisionedThroughput']['WriteCapacityUnits']
    table_size_bytes = table_data['TableSizeBytes']
    item_count = table_data['ItemCount']

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["Field Name", "Field Type"]

    # Add field information to the table
    for field in fields:
        table.add_row([field['AttributeName'], field['AttributeType']])

    # Print the formatted table
    print("Table Fields:")
    print(table)

    # Create another PrettyTable for general table information
    table_info = PrettyTable()
    table_info.field_names = ["Property", "Value"]

    # Add general table information to the table
    table_info.add_row(["Table Name", table_name])
    table_info.add_row(["Table ARN", table_arn])
    table_info.add_row(["Table Status", table_status])
    table_info.add_row(["Creation Date Time", creation_date_time.strftime('%Y-%m-%d %H:%M:%S %Z')])
    table_info.add_row(["Read Capacity Units", read_capacity_units])
    table_info.add_row(["Write Capacity Units", write_capacity_units])
    table_info.add_row(["Table Size (Bytes)", table_size_bytes])
    table_info.add_row(["Item Count", item_count])

    # Print the formatted table for general table information
    print("\nTable Description:")
    print(table_info)

except db.exceptions.ResourceNotFoundException:
    print(f"The table '{table_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
