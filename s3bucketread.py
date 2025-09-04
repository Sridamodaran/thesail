import boto3
#listing s3 bucket using boto3
def list_s3_buckets():
    """Lists all S3 buckets."""
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    # Call list_buckets() and get the response
    response = s3_client.list_buckets()
    
    # Print the names of the buckets
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

if __name__ == "__main__":
    list_s3_buckets()
