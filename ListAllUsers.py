import boto3
from tabulate import tabulate

def all_users():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')
    user_data = []

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            arn = user['Arn']
            createdate = user['CreateDate']
            user_data.append([username, arn, createdate])

    table_headers = ['Username', 'ARN', 'CreateDate']
    print(tabulate(user_data, headers=table_headers, tablefmt='pretty'))

all_users()
