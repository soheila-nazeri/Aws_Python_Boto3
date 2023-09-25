import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Specify the desired bucket name
bucket_name = "soheila-s3-123"

# Set ACL settings
acl_settings = {
    'ACL': 'private',  # You can change this to your desired settings
}

# Create a new bucket with the given settings
try:
    response = s3_client.create_bucket(
        Bucket=bucket_name,
        **acl_settings,
    )
    print("Bucket created successfully.")
except Exception as e:
    print(f"Error creating bucket: {str(e)}")
