import boto3
import time
import os
from dotenv import load_dotenv

load_dotenv()

class SilverLayer:
    def __init__(self):
        pass
    def trigger_glue_job(self,job_name,job_parameter):
        aws_access_key = os.environ.get("aws_access_key_id")
        aws_secret_key = os.environ.get("aws_secret_access_key")

        glue_client = boto3.client(
            'glue',
            region_name='ap-south-2',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        response = glue_client.start_job_run(
            JobName = job_name,
            Arguments = {
                '--load_date' : job_parameter
            }
        )
        job_run_id = response['JobRunId']
        while True:
            status = glue_client.get_job_run(
                JobName = job_name,
                RunId = job_run_id
            )['JobRun']['JobRunState']
            print(f"Current Status : {status}")
            if status in ['SUCCEEDED']:
                break
            elif status in ['FAILED','STOPPED']:
                raise Exception(f"Glue Job Failed with status : {status}")
            time.sleep(30)
        return job_run_id
    def trigger_crawler(self,crawler_name):
        aws_access_key = os.environ.get("aws_access_key_id")
        aws_secret_key = os.environ.get("aws_secret_access_key")

        glue_client = boto3.client(
            'glue',
            region_name='ap-south-2',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        response = glue_client.start_crawler(
            Name=crawler_name
        )
        while True:
            status = glue_client.get_crawler(
                Name = crawler_name
            )['Crawler']['State']
            print(f"Current Status : {status}")
            if status in ['READY']:
                break
            elif status in ['FAILED','STOPPED']:
                raise Exception(f"Glue Job Failed with status : {status}")
            time.sleep(30)
        return response
        