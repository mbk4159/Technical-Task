import boto3
import sys

def read_s3_object(bucket_name, object_key):

    try:
        s3_client = boto3.client('s3')

        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)

        data = response['Body'].read().decode('utf-8')

        return data

    except Exception as e:
        print(f"Error reading object {object_key} from bucket {bucket_name}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    bucket_name = "task-database"
    object_key = "database.txt"

    content = read_s3_object(bucket_name, object_key)
    print(content)
