from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from subprocess import run
from datetime import datetime
from airflow.operators.empty import EmptyOperator

PATCH_SCRIPT_PATH = ".../lakehouse/macros/patch_dbt_docs_logo.py"

def run_patch_script():
    run(["python3", PATCH_SCRIPT_PATH], check=True)

with DAG(
    dag_id="dbt_docs",
    description="DAG to process dbt docs generate and change Company logo",
    schedule_interval="0 18 * * *",  
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["dbt_docs"],
    max_active_runs=1,  
) as dag:
    
    start = EmptyOperator(task_id='init')
    
    generate_dbt_docs = BashOperator(
        task_id="generate_dbt_docs",
        bash_command="dbt docs generate",
    )

    patch_docs_logo = PythonOperator(
        task_id="patch_dbt_docs_logo",
        python_callable=run_patch_script,
    )

    finish = EmptyOperator(task_id='finish')
    
    generate_dbt_docs >> patch_docs_logo
