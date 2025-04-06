from google.cloud import storage
import os
from dotenv import load_dotenv

load_dotenv()
BUCKET_NAME = os.environ.get('GCP_BUCKET_NAME')
if not BUCKET_NAME:
    raise ValueError("GCP_BUCKET_NAME environment variable is not set")

def download_files_from_gcp(source_folder, destination_folder):
    """
    Downloads files from a GCP bucket's folder to a local destination
    
    Args:
        source_folder (str): Folder path in the bucket (e.g., 'images/')
        destination_folder (str): Local folder path to save files
    """
    try:
        # Initialize the GCP storage client
        storage_client = storage.Client()
        
        # Get the bucket using bucket() method
        bucket = storage_client.bucket(BUCKET_NAME)
        
        # Create destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)
        
        # List all blobs in the specified folder
        blobs = bucket.list_blobs(prefix=source_folder)
        
        imagePaths = []

        # Download each file
        for blob in blobs:
            # Skip if it's a folder
            if blob.name.endswith('/'):
                continue
                
            # Get the filename from the blob path
            filename = os.path.basename(blob.name)
            destination_path = os.path.join(destination_folder, filename)
            imagePaths.append(destination_path)
            # Download the file
            blob.download_to_filename(destination_path)
            print(f"Downloaded: {filename}")
            
        print("All files downloaded successfully!")
        return imagePaths
    except Exception as e:
        print(f"Error downloading files: {str(e)}")

if __name__ == "__main__": 
    SOURCE_FOLDER = "images/"         # Folder in GCP bucket
    DESTINATION_FOLDER = "images"  # Local folder to save files
    
    # Execute the download
    download_files_from_gcp(SOURCE_FOLDER, DESTINATION_FOLDER)