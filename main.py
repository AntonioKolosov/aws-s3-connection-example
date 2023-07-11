"""
After registration on AWS:
    Step one: create acces key from 
    https://us-east-1.console.aws.amazon.com/iamv2/home#/security_credentials

    Step two: create .env file for acces key and region

    Step three: you should download console from https://github.com/aws/aws-cli

    Step four: Connect it.

    Usefull commands: 
        aws s3 ls (list of created buckets)
        aws sts get-caller-identity (information about account)
"""


import os

import boto3
import pandas as pd


def main():
    """"""
    directory = "./metadata"

    # Create session with my DB
    session = boto3.Session(profile_name="bot-farm")
    dev_s3_client = session.client("s3")
    # Get avaible buckets list
    dev_s3_client.list_buckets()
    # Get metadata from bot-farm-storage
    s = dev_s3_client.list_objects(Bucket="bot-farm-storage")
    # Convert metadata to json file
    df = pd.DataFrame(s['Contents'])
    file_path = os.path.join(directory, "metadata.json")
    df.to_json(file_path, indent=4)


if __name__ == "__main__":
    main()
