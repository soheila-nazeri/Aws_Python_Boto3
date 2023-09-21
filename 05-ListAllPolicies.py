import boto3

def list_customer_policies():
    iam = boto3.client('iam')

    try:
        paginator = iam.get_paginator('list_policies')

        for response in paginator.paginate(Scope="Local"):
            for policy in response['Policies']:
                policy_name = policy['PolicyName']
                policy_arn = policy['Arn']

                print(f"Policy Name: {policy_name} | Arn: {policy_arn}")

    except Exception as e:
        print(f"Error listing policies: {str(e)}")

list_customer_policies()
