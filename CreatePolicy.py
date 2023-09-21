import boto3
import json

def create_policy(policy_name, policy_document):
    iam = boto3.client('iam')

    try:
        # Create the policy
        response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )

        print(f"Policy '{policy_name}' has been created successfully.")
        return response['Policy']['Arn']
    except Exception as e:
        print(f"Error creating policy: {str(e)}")
        return None

def attach_policy_to_user(user_name, policy_arn):
    iam = boto3.client('iam')

    try:
        # Attach the policy to the user
        response = iam.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )

        print(f"Policy '{policy_arn}' has been attached to user '{user_name}' successfully.")
    except Exception as e:
        print(f"Error attaching policy to user: {str(e)}")

# Define your policy document
user_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}

# Define the policy name and user name
policy_name = 'pyFullAccess_1'
user_name = 'samira_nazeri_1'  # Replace 'your_username' with the actual username

# Create the policy and get its ARN
policy_arn = create_policy(policy_name, user_policy)

# Attach the policy to the specified user
if policy_arn:
    attach_policy_to_user(user_name, policy_arn)
