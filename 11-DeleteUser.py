import boto3
from botocore.exceptions import ClientError

def delete_myuser(username):
    try:
        iam = boto3.client('iam')
        response = iam.delete_user(UserName=username)
        print(f"User '{username}' has been deleted successfully.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            print(f"User '{username}' not found. No action taken.")
        else:
            print(f"Error deleting user '{username}': {e}")

# Specify the username you want to delete
username = 'samira_nazeri_1'

# Delete the user
delete_myuser(username)
