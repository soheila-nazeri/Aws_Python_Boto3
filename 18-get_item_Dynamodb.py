import boto3
import botocore  # Import botocore for exception handling

# Initialize DynamoDB resource
db = boto3.resource('dynamodb')

# Define the table name
table_name = 'Account'

# Define the key to retrieve
key_to_retrieve = {
    'id': "1"
}


# Get the item from the table
table = db.Table(table_name)
response = table.get_item(Key=key_to_retrieve)

# Check if the item exists
if 'Item' in response:
    item = response['Item']
    print("Item Retrieved:")
    print(item)
else:
    print(f"Item with id '{key_to_retrieve['id']}' does not exist in the table.")
