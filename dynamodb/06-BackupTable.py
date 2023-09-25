import boto3
from prettytable import PrettyTable

# Initialize DynamoDB client
db = boto3.client('dynamodb')

def create_backup():
    try:
        table_name = input("Enter the name of the table to create a backup for: ")
        backup_name = input("Enter a name for the backup: ")

        # Create the backup
        response = db.create_backup(
            TableName=table_name,
            BackupName=backup_name
        )

        # Print the response
        print("\nBackup Creation Response:")
        display_response(response)

    except Exception as e:
        print(f"An error occurred: {e}")

def delete_backup():
    try:
        backup_arn = input("Enter the ARN of the backup to delete: ")

        # Delete the backup
        response = db.delete_backup(BackupArn=backup_arn)

        # Print the response
        print("\nBackup Deletion Response:")
        display_response(response)

    except Exception as e:
        print(f"An error occurred: {e}")

def display_response(response):
    # Create a PrettyTable for the response
    table = PrettyTable()
    table.field_names = ["Property", "Value"]

    # Add response properties to the PrettyTable
    for key, value in response.items():
        table.add_row([key, value])

    # Print the formatted table
    print(table)

while True:
    print("\nMenu:")
    print("1. Create Backup")
    print("2. Delete Backup")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_backup()
    elif choice == '2':
        delete_backup()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
