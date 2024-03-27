# Overview

Concurrent UltiHash download script. Download data recursively to UltiHash
cluster using boto3 library to access the S3 API.

# Requirements

- Python 3
- boto3 library installed

# Installation
Create a virtual environment to hold the Python libraries:

```
$> python3 -m venv venv
$> . venv/bin/activate
```

Install all requirements:

```
$> pip install --requirement requirements.txt
```

# Usage
To download a bucket from an UH cluster running locally:

```
$> ./uh_download.py $BUCKET_NAME
```

Download a folder from a given S3 instance

```
$> ./uh_download.py --url http://uh.my-domain.net $BUCKET_NAME
```

Override the default target directory:

```
$> ./uh_upload.py --path MY_DIRECTORY $BUCKET_NAME
```
