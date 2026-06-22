from databricks.sdk import WorkspaceClient
import os
from dotenv import load_dotenv

load_dotenv()

class GoldLayer:
    def __init__(self):
        pass
    def trigger_databricks_job(self,job_id:int):
        databricks_pat = os.environ.get("Databricks_PAT")
        databricks_host = os.environ.get("Databricks_HOST")

        db_client = WorkspaceClient(
            host= databricks_host,
            token=databricks_pat
        )
        run = db_client.jobs.run_now(
            job_id=job_id
        )
        return f"Databricks job is triggered! Job Run is {run.run_id}"

obj = GoldLayer()
obj.trigger_databricks_job(1094092834923963)
