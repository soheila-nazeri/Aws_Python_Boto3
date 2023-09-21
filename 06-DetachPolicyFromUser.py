import boto3

def detach_user_policy(user_name, policy_arn):
    try:
        iam = boto3.client('iam')

        response = iam.detach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Policy '{policy_arn}' has been detached from user '{user_name}' successfully.")
        else:
            print(f"Failed to detach policy from user. Response: {response}")
    except Exception as e:
        print(f"Error detaching policy from user: {str(e)}")

# Specify the user name and policy ARN
user_name = 'soheila_nazeri'
policy_arn = 'arn:aws:iam::961827421039:policy/pyFullAccess_1'

# Detach the policy from the user
detach_user_policy(user_name, policy_arn)
