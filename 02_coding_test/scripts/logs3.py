#!/usr/bin/env python3

import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAJWYFORX73DWVTFJQ' #Enter valid keys and bucket name
SECRET_KEY = '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' #Enter valid keys and bucket name
BUCKET_NAME = '02codingtest' #Enter valid keys and bucket name

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except Exception as e:
        logging.error(e)
        return False


uploaded = upload_to_aws('test.log', BUCKET_NAME, 'test.log')