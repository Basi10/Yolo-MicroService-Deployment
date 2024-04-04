import os
import boto3

class S3ModelStorage:
    def __init__(self):
        """
        Initializes the S3ModelStorage object with AWS credentials and region.

        Args:
            region_name (str): The AWS region name.
            aws_access_key_id (str): The AWS access key ID.
            aws_secret_access_key (str): The AWS secret access key.
        """
        self.s3 = boto3.resource(
            service_name='s3',
            region_name= os.environ.get('AWS_DEFAULT_REGION'),
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )

    def upload_model(self, bucket_name, local_file_path, s3_key):
        """
        Uploads a model file to the specified S3 bucket.

        Args:
            bucket_name (str): The name of the S3 bucket.
            local_file_path (str): The local path of the model file to upload.
            s3_key (str): The S3 key to use for the uploaded file.
        """
        try:
            self.s3.Bucket(bucket_name).upload_file(Filename=local_file_path, Key=s3_key)
            print("Model uploaded successfully.")
        except Exception as e:
            print(f"Error uploading model: {str(e)}")


    def retrieve_model_to_disk(self, bucket_name, s3_key, local_file_path):
        """
        Retrieves a model file from the specified S3 bucket and saves it to the local disk.

        Args:
            bucket_name (str): The name of the S3 bucket.
            s3_key (str): The S3 key of the model file to retrieve.
            local_file_path (str): The local path where the retrieved model file will be saved.
        """
        try:
            self.s3.Bucket(bucket_name).download_file(Key=s3_key, Filename=local_file_path)
            print("Model retrieved to disk.")
        except Exception as e:
            print(f"Error retrieving model to disk: {str(e)}")




   
