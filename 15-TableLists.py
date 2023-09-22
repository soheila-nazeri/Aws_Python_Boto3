import boto3
from prettytable import PrettyTable

# Initialize DynamoDB client
db = boto3.client('dynamodb')

try:
    # List tables
    response = db.list_tables()
    print(response)
    # Get table names
    table_names = response.get('TableNames', [])
    print(table_names)
    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["Table Names"]

    # Add table names to the PrettyTable
    for table_name in table_names:
        table.add_row([table_name])

    if not table_names:
        print("No tables found.")
    else:
        print("List of Tables:")
        print(table)

except Exception as e:
    print(f"An error occurred: {e}")
