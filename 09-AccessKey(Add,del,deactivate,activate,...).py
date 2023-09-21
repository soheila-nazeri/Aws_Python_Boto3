import boto3


def create_access_key(username):
    try:
        iam = boto3.client('iam')
        response = iam.create_access_key(UserName=username)
        access_key = response['AccessKey']

        print(f"Access key created for user '{username}':")
        print(f"Access Key ID: {access_key['AccessKeyId']}")
        print(f"Secret Access Key: {access_key['SecretAccessKey']}")
    except Exception as e:
        print(f"Error creating access key: {str(e)}")


def get_existing_access_keys(username):
    try:
        iam = boto3.client('iam')
        response = iam.list_access_keys(UserName=username)
        access_keys = response['AccessKeyMetadata']

        if access_keys:
            print(f"Existing access keys for user '{username}':")
            for key in access_keys:
                print(f"Access Key ID: {key['AccessKeyId']} | Status: {key['Status']}")
        else:
            print(f"No existing access keys found for user '{username}'.")
    except Exception as e:
        print(f"Error getting existing access keys: {str(e)}")


def change_access_key_status(access_key_id, username, status):
    try:
        iam = boto3.client('iam')
        iam.update_access_key(AccessKeyId=access_key_id, Status=status, UserName=username)
        print(f"Access key with ID '{access_key_id}' for user '{username}' has been {status}.")
    except Exception as e:
        print(f"Error changing access key status: {str(e)}")


def delete_access_key(access_key_id, username):
    try:
        iam = boto3.client('iam')
        iam.delete_access_key(AccessKeyId=access_key_id, UserName=username)
        print(f"Access key with ID '{access_key_id}' for user '{username}' has been deleted.")
    except Exception as e:
        print(f"Error deleting access key: {str(e)}")


while True:
    print("\nMenu:")
    print("1. Create Access Key")
    print("2. Get Existing Access Keys")
    print("3. Change Access Key Status")
    print("4. Deactivate Access Key")
    print("5. Activate Access Key")
    print("6. Delete Access Key")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        username = input("Enter the username: ")
        create_access_key(username)
    elif choice == '2':
        username = input("Enter the username: ")
        get_existing_access_keys(username)
    elif choice == '3':
        access_key_id = input("Enter the Access Key ID: ")
        username = input("Enter the username: ")
        status = input("Enter the new status (Active/Inactive): ")
        change_access_key_status(access_key_id, username, status)
    elif choice == '4':
        access_key_id = input("Enter the Access Key ID: ")
        username = input("Enter the username: ")
        change_access_key_status(access_key_id, username, 'Inactive')
    elif choice == '5':
        access_key_id = input("Enter the Access Key ID: ")
        username = input("Enter the username: ")
        change_access_key_status(access_key_id, username, 'Active')
    elif choice == '6':
        access_key_id = input("Enter the Access Key ID: ")
        username = input("Enter the username: ")
        delete_access_key(access_key_id, username)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6/7).")
