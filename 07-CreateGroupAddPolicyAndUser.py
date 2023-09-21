import boto3

def create_group(group_name):
    iam = boto3.client('iam')

    try:
        # Create the IAM group
        response = iam.create_group(
            GroupName=group_name
        )

        print(f"Group '{group_name}' has been created successfully.")
        return True
    except Exception as e:
        print(f"Error creating group: {str(e)}")
        return False

def add_user_to_group(user_name, group_name):
    iam = boto3.client('iam')

    try:
        # Add the user to the group
        response = iam.add_user_to_group(
            GroupName=group_name,
            UserName=user_name
        )

        print(f"User '{user_name}' has been added to group '{group_name}' successfully.")
        return True
    except Exception as e:
        print(f"Error adding user to group: {str(e)}")
        return False

def attach_policy_to_group(policy_arn, group_name):
    iam = boto3.client('iam')

    try:
        # Attach the policy to the group
        response = iam.attach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )

        print(f"Policy '{policy_arn}' has been attached to group '{group_name}' successfully.")
        return True
    except Exception as e:
        print(f"Error attaching policy to group: {str(e)}")
        return False

# Define group name, user name, and policy ARN
group_name = 'S3Admins'
user_name = 'soheila_nazeri'  # Replace with the actual username
policy_arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'

# Create the group (if it doesn't already exist)
if create_group(group_name):
    # Add the user to the group
    if add_user_to_group(user_name, group_name):
        # Attach the policy to the group
        attach_policy_to_group(policy_arn, group_name)
