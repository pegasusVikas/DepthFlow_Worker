from google.cloud import run_v2
from google.cloud.run_v2 import Job
from dotenv import load_dotenv
import os

load_dotenv()

 # Get configuration from environment variables
PROJECT_ID = os.environ.get('GCP_PROJECT_ID')
LOCATION = os.environ.get('GCP_LOCATION', 'us-central1')
JOB_NAME = os.environ.get('GCP_JOB_NAME')

if not all([PROJECT_ID, JOB_NAME]):
    raise ValueError("Missing required environment variables")

def trigger_cloud_run_job(project_id: str=PROJECT_ID, location: str=LOCATION, job_name: str=JOB_NAME):
    """
    Triggers a Cloud Run job execution
    
    Args:
        project_id (str): GCP project ID
        location (str): Region where job is deployed (e.g., 'us-central1')
        job_name (str): Name of the Cloud Run job
    
    Returns:
        str: Execution name if successful, None if failed
    """
    try:
        # Initialize the Cloud Run jobs client
        client = run_v2.JobsClient()

        # Create the job execution request
        request = run_v2.RunJobRequest(
            name=f"projects/{project_id}/locations/{location}/jobs/{job_name}"
        )

        # Execute the job
        operation = client.run_job(request=request)
        
        print(f"Job triggered: {operation.metadata}")
        return operation.metadata.uid

    except Exception as e:
        print(f"Error triggering job: {str(e)}")
        raise e

if __name__ == "__main__":
   

    # Trigger the job
    execution_name = trigger_cloud_run_job()