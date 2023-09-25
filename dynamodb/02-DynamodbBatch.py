import boto3

# Initialize DynamoDB resource
db = boto3.resource('dynamodb')

# Define the table name
table_name = 'employee'

# Function to create a table if it doesn't exist
def create_table_if_not_exists(db, table_name):
    try:
        # Check if the table exists
        table = db.Table(table_name)
        table.table_status
    except db.meta.client.exceptions.ResourceNotFoundException:
        # Table does not exist, so create it
        table = db.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'emp_id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'emp_id',
                    'AttributeType': 'S'  # String type for emp_id
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
    return table

# Create the table if it doesn't exist
table = create_table_if_not_exists(db, table_name)

# Use batch_writer to insert data into the table
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'emp_id': '1',
            'name': 'soheila_nazeri',
            'age': '38'
        }
    )

    batch.put_item(
        Item={
            'emp_id': '2',
            'name': 'sima_naderi',
            'age': '32'
        }
    )

    batch.put_item(
        Item={
            'emp_id': '7',
            'name': 'samira_nazeri',
            'age': '37'
        }
    )
