from airflow.sdk import dag,task
import os
from datetime import datetime,timedelta
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.Bronze_layer import BronzeLayer
from utils.Silver_layer import SilverLayer
from utils.Gold_layer import GoldLayer
@dag(schedule='@daily',
     is_paused_upon_creation=False)
def aws_project():
    @task(retries=3,retry_delay=timedelta(seconds=5))
    def extract_load_s3():
        urls = ["https://raw.githubusercontent.com/anshlambagit/ApacheAirflow/refs/heads/main/bookings.csv",
                "https://raw.githubusercontent.com/anshlambagit/ApacheAirflow/refs/heads/main/passengers.csv",
                "https://raw.githubusercontent.com/anshlambagit/ApacheAirflow/refs/heads/main/airports.csv"]
        obj = BronzeLayer()
        folder_name = datetime.now().strftime("%Y-%m-%d")
        for url in urls:
            fetch_data = obj.Fetch_Api(url)
            obj.put_data_s3hook("awsbucketmoni2026",f"Bronze/{folder_name}/{url.split('/')[-1]}",fetch_data)
        return folder_name
    @task(retries=3, retry_delay=timedelta(seconds=5))
    def transform_load_s3(ti):
        last_load_date = ti.xcom_pull(task_ids='extract_load_s3',key='return_value')
        obj = SilverLayer()
        job_run_id = obj.trigger_glue_job('silver_layer',last_load_date)
        return f"Glue Job is triggered. Job Id is :{job_run_id}"
    @task(retries=3, retry_delay=timedelta(seconds=5))
    def transform_load_parquet(ti):
        last_load_date = ti.xcom_pull(task_ids='extract_load_s3',key='return_value')
        obj = SilverLayer()
        job_run_id = obj.trigger_glue_job('silver_athena',last_load_date)
        return f"Glue Job is triggered. Job Id is :{job_run_id}"
    @task(retries=3, retry_delay=timedelta(seconds=5))
    def trigger_crawler_silver():
        obj = SilverLayer()
        crawl_res = obj.trigger_crawler('silver_crawler')
        return f"crawler respond : {crawl_res}"
    @task(retries=3, retry_delay=timedelta(seconds=5))
    def trigger_Gold_Layer():
        obj = GoldLayer()
        res = obj.trigger_databricks_job(1094092834923963)
        print(res)

    extract_load_s3() >> [transform_load_s3(),transform_load_parquet()] >> trigger_crawler_silver() >> trigger_Gold_Layer()
aws_project()

