import boto3


def create_user(username):
    iam=boto3.client("iam")
    response=iam.create_user(UserName=username)
    print(response)

create_user("samira_nazeri")