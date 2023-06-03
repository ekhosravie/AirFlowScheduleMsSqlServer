from airflow import DAG
from airflow.operators.mssql_operator import MsSqlOperator
from datetime import datetime

dag = DAG(
    'sql_server_dag',
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily'
)

# Create a task to run a SQL Server script
sql_server_task = MsSqlOperator(
    task_id='sql_server_task',
    mssql_conn_id='mssql_default',
    sql='path/to/sql/script.sql',
    dag=dag
)

# Run the task
sql_server_task