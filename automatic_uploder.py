"""
This script upload files to backet from dirs
"""


import os
from dotenv import load_dotenv
import boto3


load_dotenv()

aws_access_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

client = boto3.client("s3",
                      aws_access_key_id=aws_access_id,
                      aws_secret_access_key=aws_secret_key)


# Not the best way to define your path
path = "../new-topics/new-bot/datatopics/simple"


for file in os.listdir(path):
    if ".txt" in file:
        file_path = os.path.join(path, file)
        upload_file_bucket = "bot-farm-storage"
        upload_file_key = "text/" + str(file)
        client.upload_file(file_path,
                           upload_file_bucket,
                           upload_file_key)
