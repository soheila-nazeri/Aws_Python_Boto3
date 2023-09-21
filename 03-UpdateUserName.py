import boto3


def update_username(old_username, new_username):
    iam = boto3.client("iam")

    try:
        # First, retrieve the information of the old username
        user_info = iam.get_user(UserName=old_username)

        # Then, update the username using the update_user method
        response = iam.update_user(
            UserName=old_username,
            NewUserName=new_username
        )

        print(f"Username {old_username} has been changed to {new_username}.")
    except Exception as e:
        print(f"Error: {str(e)}")


update_username("samira_nazeri", "samira_nazeri_1")
