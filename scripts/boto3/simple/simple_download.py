#!/usr/bin/env python3
import boto3
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: simple_download.py <UltiHash URL> [file [file ...]]")
        print("\nSimple single-threaded script to outline download from UltiHash service")
        print("using boto3 library.")
        sys.exit(1)

    # connection to UltiHash S3 service
    uh_url = sys.argv[1]
    uh_service = boto3.client('s3', endpoint_url=uh_url,
        aws_access_key_id='', aws_secret_access_key='')

    # all data will be queried from this bucket
    source_bucket_name = "bucket"

    # download each file from command line and store it in the current working directory
    for id in range(2, len(sys.argv)):
        file = sys.argv[id]

        response = uh_service.get_object(Bucket=source_bucket_name, Key=os.path.basename(file))
        with open(file, 'wb') as f:
            f.write(response['Body'].read())

            print(f"downloaded {file}")
