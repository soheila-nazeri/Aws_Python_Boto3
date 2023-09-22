import boto3
from prettytable import PrettyTable

# Initialize DynamoDB client
db = boto3.client('dynamodb')

# Define the table name and new provisioning settings
table_name = 'Account'
new_provisioned_throughput = {
    'ReadCapacityUnits': 1,
    'WriteCapacityUnits': 1
}

try:
    # Update the table
    response = db.update_table(
        TableName=table_name,
        BillingMode='PROVISIONED',
        ProvisionedThroughput=new_provisioned_throughput
    )

    # Create a PrettyTable for the response
    table = PrettyTable()
    table.field_names = ["Property", "Value"]

    # Add response properties to the PrettyTable
    for key, value in response.items():
        table.add_row([key, value])

    print("Table Update Response:")
    print(table)

except Exception as e:
    print(f"An error occurred: {e}")
