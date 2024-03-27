# Overview

UltiHash sample scripts. Upload and download of data to UltiHash cluster using
boto3 to access the UltiHash S3 API.


# Requirements

- Python 3
- boto3 library installed

# Installation

Create a virtual environment to hold the Python libraries:

```
$> python -m venv venv
$> . venv/bin/activate
```

Install all requirements:

```
$> pip install --requirement requirements.txt
```

# Script Usage

## Sample upload script

See `simple_upload.py` for how to upload a file to an UltiHash S3 bucket using
boto3 library. The script will upload any file given on the command line and
upload it sequentially to the bucket `bucket`. The bucket will be created.

Usage:
```
$> ./simple_upload.py http://localhost:8080 file
```

## Sample download script

See `simple_download.py` for how to download a file from an UltiHash S3 bucket
using boto3 library. The script will download files given on the command line
sequentially from the bucket `bucket`. The files must exist in the bucket.

Usage:
```
$> ./simple_upload.py http://localhost:8080 file
```

