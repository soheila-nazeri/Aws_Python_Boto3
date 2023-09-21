import boto3

def detach_policy_from_group(policy_arn, group_name):
    iam = boto3.client('iam')

    try:
        # Detach the policy from the group
        response = iam.detach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )

        print(f"Policy '{policy_arn}' has been detached from group '{group_name}' successfully.")
        return True
    except Exception as e:
        print(f"Error detaching policy from group: {str(e)}")
        return False

def remove_user_from_group(user_name, group_name):
    iam = boto3.client('iam')

    try:
        # Remove the user from the group
        response = iam.remove_user_from_group(
            GroupName=group_name,
            UserName=user_name
        )

        print(f"User '{user_name}' has been removed from group '{group_name}' successfully.")
        return True
    except Exception as e:
        print(f"Error removing user from group: {str(e)}")
        return False

# Define group name, user name, and policy ARN
group_name = 'S3Admins'
user_name = 'soheila_nazeri'  # Replace with the actual username
policy_arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'

# Detach the policy from the group (if it's attached)
detach_policy_from_group(policy_arn, group_name)

# Remove the user from the group (if the user is in the group)
remove_user_from_group(user_name, group_name)
