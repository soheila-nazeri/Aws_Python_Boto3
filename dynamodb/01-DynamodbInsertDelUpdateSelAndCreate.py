import boto3
import csv
import time

# Initialize DynamoDB resource
db = boto3.resource('dynamodb')
table_name = 'account'


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
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'  # String type for id
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()

    return table


def insert_data(table, data):
    try:
        table.put_item(Item=data)
        print("Item added successfully!")
    except Exception as e:
        print(f"An error occurred while adding the item: {e}")


def delete_data(table, account_id):
    try:
        table.delete_item(
            Key={'id': account_id}
        )
        print(f"Item with id {account_id} deleted successfully!")
    except Exception as e:
        print(f"An error occurred while deleting the item: {e}")


def update_data(table, account_id, update_expression, expression_attribute_values):
    try:
        table.update_item(
            Key={'id': account_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        print(f"Item with id {account_id} updated successfully!")
    except Exception as e:
        print(f"An error occurred while updating the item: {e}")


def select_data(table, condition_expression, expression_attribute_values):
    try:
        response = table.scan(
            FilterExpression=condition_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        return response['Items']
    except Exception as e:
        print(f"An error occurred while querying the table: {e}")
        return []


def export_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
        print(f"Data exported to {filename} successfully!")
    except Exception as e:
        print(f"An error occurred while exporting to CSV: {e}")


def main():
    while True:
        print("\nMenu:")
        print("1. Create Table (if not exists)")
        print("2. Insert Data")
        print("3. Delete Data")
        print("4. Update Data")
        print("5. Query Data")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_table_if_not_exists(db, table_name)
        elif choice == '2':
            account_id = input("Enter Account ID: ")
            code = input("Enter Code: ")
            title = input("Enter Title: ")
            user_id = input("Enter User ID: ")
            create_date_time = input("Enter Create Date Time: ")
            data = {
                'id': account_id,
                'code': code,
                'title': title,
                'user_id': user_id,
                'create_date_time': create_date_time
            }
            insert_data(db.Table(table_name), data)
        elif choice == '3':
            account_id = input("Enter Account ID to delete: ")
            delete_data(db.Table(table_name), account_id)
        elif choice == '4':
            account_id = input("Enter Account ID to update: ")
            update_expression = input("Enter Update Expression: ")
            expression_attribute_values = {}
            update_data(db.Table(table_name), account_id, update_expression, expression_attribute_values)
        elif choice == '5':
            condition_expression = input("Enter Condition Expression: ")
            expression_attribute_values = {}
            result = select_data(db.Table(table_name), condition_expression, expression_attribute_values)
            print("Query results:")
            for item in result:
                print(item)
        elif choice == '6':
            filename = input("Enter CSV filename to export data: ")
            data_to_export = select_data(db.Table(table_name), "status = :s", {":s": "active"})
            export_to_csv(data_to_export, filename)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


"""
Sample Input for Creating a User Account (Insert Data):

Account ID: 12345
Code: ABC123
Title: Example User
Status: Active
User ID: 67890
Create Date Time: 2023-09-25T14:30:00Z
You can use the above input to insert a new user account record into your DynamoDB table.

Sample Input for Updating a User Account (Update Data):

Account ID to Update: 12345
Update Expression: set status = :s
Expression Attribute Values: {:s: "Inactive"}

You can use the above input to update the status of the user account with Account ID 12345 to "Inactive."
"""