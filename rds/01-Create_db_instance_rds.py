import boto3
from pprint import pprint

# Initialize the RDS client
rds_client = boto3.client('rds')

try:
    # Attempt to create the RDS instance
    response = rds_client.create_db_instance(
        DBName="rdsSoheila",  # Name of the RDS database
        DBInstanceIdentifier="rdssoheilainstance",  # Identifier for the RDS instance
        AllocatedStorage=20,  # Allocated storage in GB
        DBInstanceClass='db.t2.micro',  # Instance class (e.g., db.t2.micro)
        Engine='MySQL',  # Database engine (e.g., MySQL)
        MasterUsername='sima',  # Master username
        MasterUserPassword='sima_12345',  # Master password
        Port=3306,  # Port for database access
        EngineVersion='8.0.28',  # Database engine version (e.g., MySQL 8.0.27)
        PubliclyAccessible=True,  # Allow public access (can be True or False)
        StorageType='gp2'  # Storage type (e.g., gp2)
    )

    # Print the response from the AWS service
    pprint(response)

except Exception as e:
    # Handle exceptions gracefully and print an error message
    print(f"An error occurred: {e}")
