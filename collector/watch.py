import _thread, time
from scripts.watch.main import watch_for_changes

a_list = []
WATCH_DIRECTORY = "hotdir"
def input_thread(a_list):
    input()
    a_list.append(True)

def main():
  _thread.start_new_thread(input_thread, (a_list,))
  print(f"Watching '{WATCH_DIRECTORY}/' for new files.\n\nUpload files into this directory while this script is running to convert them.\nPress enter or crtl+c to exit script.")
  while not a_list:
    watch_for_changes(WATCH_DIRECTORY)
    time.sleep(1)
  
  print("Stopping watching of hot directory.")
  exit(1)

if __name__ == "__main__":
  main()

  """
  Yes, it is indeed possible to design the "hot dir" on cloud storage and implement the functionality in a serverless manner instead of running nonstop. This can be achieved by using cloud storage services and serverless computing platforms. Here's a high-level overview of how you could adapt the script for such a setup:

1. **Choose a Cloud Storage Service:**
   - Select a cloud storage service such as Amazon S3, Google Cloud Storage, or Microsoft Azure Blob Storage to store the files.

2. **Upload Files to Cloud Storage:**
   - Instead of a local directory (`hotdir`), users would upload files directly to the designated cloud storage bucket.

3. **Trigger Serverless Function on File Upload:**
   - Set up a serverless function (e.g., AWS Lambda, Google Cloud Functions, or Azure Functions) to be triggered whenever a new file is uploaded to the cloud storage bucket.

4. **Modify Script for Serverless:**
   - Adapt the script to run as a serverless function. The file-watching loop can be replaced by the serverless function that gets triggered on file upload.

5. **Remove Threading:**
   - Since serverless functions are designed to scale automatically, threading may not be necessary. Serverless functions are typically stateless and handle one invocation at a time.

6. **Handle File Processing:**
   - Integrate the file processing logic into the serverless function. Upon trigger, the function can process the uploaded file and perform any required transformations.

7. **Output Results to Cloud Storage:**
   - Store the results (vectorized files) back in the cloud storage bucket or another designated location.

8. **Serverless Invocation Limits:**
   - Be aware of the invocation limits and execution duration constraints of the chosen serverless platform. Serverless functions are designed to be event-driven and stateless, so ensure that your script fits within these constraints.

Here's a very simplified example using AWS Lambda and S3:

```python
import json
import boto3

def lambda_handler(event, context):
    # Retrieve information about the uploaded file
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Process the file (replace this with your processing logic)
    process_file(bucket, key)

def process_file(bucket, key):
    # Implement your file processing logic here
    # ...

    # Save results back to cloud storage (e.g., S3)
    save_results_to_s3(bucket, key, processed_data)

def save_results_to_s3(bucket, key, data):
    s3 = boto3.client('s3')

    # Specify the bucket and key for storing results
    result_bucket = 'your-result-bucket'
    result_key = f'results/{key}'  # You can customize the destination key

    # Upload processed data to the result bucket
    s3.put_object(Body=json.dumps(data), Bucket=result_bucket, Key=result_key)
```

This is a basic example, and you'll need to customize it based on your specific requirements and the cloud platform you choose. Additionally, consider security measures such as access controls and encryption when working with cloud storage and serverless functions.
  """