from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define default args for the DAG
default_args = {
    'owner': 'wael',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'mlops_pipeline',
    default_args=default_args,
    description='An example MLOps pipeline',
    schedule_interval=timedelta(days=1),  # Run every day
)

# Define tasks (functions to execute)
def data_ingestion():
    print("Ingesting data...")

def data_validation():
    print("transformation data...")

def data_transformation():
    print("Validating data...")

def model_training():
    print("Training model...")

def model_evaluation():
    print("Evaluating model...")

# Create the tasks for each component of the pipeline
t1 = PythonOperator(task_id='data_ingestion', python_callable=data_ingestion, dag=dag)
t2 = PythonOperator(task_id='data_transformation', python_callable=data_validation, dag=dag)
t3 = PythonOperator(task_id='data_Validation', python_callable=data_transformation, dag=dag)
t4 = PythonOperator(task_id='model_training', python_callable=model_training, dag=dag)
t5 = PythonOperator(task_id='model_evaluation', python_callable=model_evaluation, dag=dag)

# Set task dependencies (order of execution)
t1 >> t2 >> t3 >> t4 >> t5
