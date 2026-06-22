import boto3
import pandas as pd
import requests
from io import StringIO
import os
from dotenv import load_dotenv
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
load_dotenv() #for loading env variables from.env file

class BronzeLayer:
    def __init__(self):
        pass
    def Fetch_Api(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            df = pd.read_csv(StringIO(data))
            csv_buffer = StringIO()
            df.to_csv(csv_buffer,index=False)
            return csv_buffer.getvalue()
        else:
            return f"Failed to Fetch Api Successfully. {response.status_code}"
    def Write_data_s3(self,bucket,object_key,data):
        aws_access_key = os.environ.get("aws_access_key_id")
        aws_secret_key = os.environ.get("aws_secret_access_key")

        s3_client = boto3.client(
            's3',
            region_name='ap-south-2',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        s3_client.put_object(
            Bucket=bucket,
            Key=object_key,
            Body=data
        )
        return f"Data upload to {bucket} with object key {object_key}"
    def put_data_s3hook(self,bucket,object_key,data):
        s3_hook = S3Hook(aws_conn_id="aws_s3_conn")
        s3_hook.load_string(
            string_data=data,
            bucket_name=bucket,
            key=object_key,
            replace=True
        )
         

        
