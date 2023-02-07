import logging
from datetime import datetime, timedelta
from pathlib import Path
from utils import get_api_marvel
from utils import read_json_characters
from utils import read_json_comics

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

log = logging.getLogger(__name__)

files_path = "/" + "/".join(Path(__file__).parts[1:-1]) + "/files"

docs = """
teste markdown
"""

default_args = {
    "owner": "Diego",
    "schedule_interval": "@once",
    "start_date": datetime(2023, 2, 4, 6, 00, 00),
    "catchup": False,
    "retries": 2,
    "dagrun_timeout": timedelta(minutes=60),
}

dag = DAG(
    "Marvel",
    default_args=default_args,
    tags=[
        "Marvel",
    ],
    max_active_runs=1,
    #on_success_callback=cleanup_xcom,
    doc_md=docs,
)

with dag:

    start_flow = DummyOperator(task_id="start_flow")

    create_table_comics = PostgresOperator(
        task_id="create_table_comics",
        postgres_conn_id="postgres_default",
        sql="./files/sql/create_table_comics.sql",
        )

    create_table_characters = PostgresOperator(
        task_id="create_table_characters",
        postgres_conn_id="postgres_default",
        sql="./files/sql/create_table_characters.sql",
        )

    get_data = DummyOperator(task_id="get_data")

    get_data_comics = PythonOperator(
        task_id='get_data_comics', 
        python_callable=get_api_marvel, 
        op_kwargs={'endpoint': 'comics'},
        dag=dag)

    get_data_characters = PythonOperator(
        task_id='get_data_characters', 
        python_callable=get_api_marvel, 
        op_kwargs={'endpoint': 'characters'},
        dag=dag)

    transformations = DummyOperator(task_id="transformations")

    transform_comics = PythonOperator(
        task_id='transform_comics', 
        python_callable=read_json_comics, 
        dag=dag)

    transform_characters = PythonOperator(
        task_id='transform_characters', 
        python_callable=read_json_characters, 
        dag=dag)

    load_data_task = DummyOperator(task_id="load_data")

    insert_data_comics = PostgresOperator(
        task_id="insert_data_comics",
        postgres_conn_id="postgres_default",
        sql="./files/sql/insert_comic.sql",
        )

    insert_data_characters = PostgresOperator(
        task_id="insert_data_characters",
        postgres_conn_id="postgres_default",
        sql="./files/sql/insert_characters.sql",
        )
    results = DummyOperator(task_id="results")
    
    final_results = PostgresOperator(
        task_id="final_results",
        postgres_conn_id="postgres_default",
        sql="./files/sql/select_comic.sql",
        )

    end_flow_task = DummyOperator(task_id="end_flow")

    start_flow >> [create_table_comics,create_table_characters] >> get_data
    get_data >> [get_data_comics,get_data_characters] >> transformations
    transformations >>[transform_comics,transform_characters] >> load_data_task >> [insert_data_comics,insert_data_characters] >> results
    results >> final_results >> end_flow_task

if __name__ == "__main__":
    dag.cli()
