from datetime import datetime

from airflow import DAG
from airflow.decorators import task

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:

    # Tasks are represented as operators
    @task()
    def hello():
        print("hello")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello() >> airflow()
