from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 4, 10),
}

PERMS = "export GOOGLE_APPLICATION_CREDENTIALS=/opt/airflow/dags/keys/airflow-dbt.json"

with DAG(
    'nhanes_dbt_dag',
    default_args=default_args,
    schedule_interval=None,  # or '@daily', etc.
    catchup=False,
) as dag:

    run_stg_health_data = BashOperator(
        task_id='run_stg_health_data',
        bash_command=f'{PERMS} && cd /opt/airflow/dags/dbt/nhanes_project && dbt run --select stg_health_data',
    )

    run_int_biomarkers_enriched = BashOperator(
        task_id='run_int_biomarkers_enriched',
        bash_command=f'{PERMS} && cd /opt/airflow/dags/dbt/nhanes_project && dbt run --select int_biomarkers_enriched',
    )

    run_fct_longevity_summary = BashOperator(
        task_id='run_fct_longevity_summary',
        bash_command=f'{PERMS} && cd /opt/airflow/dags/dbt/nhanes_project && dbt run --select fct_longevity_summary',
    )

    run_stg_health_data >> run_int_biomarkers_enriched >> run_fct_longevity_summary