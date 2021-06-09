
Contents:
========

1. What program does

2. source code directory structure

3. Hardware and software

4. How to run program

5. How to run unit test using docker



1. What program does:
   ==================

Program is to parse data from an endpoint, write them to a file and upload it to a S3 bucket.
Details are given below:

1. Fetch JSON data from this endpoint: https://jsonplaceholder.typicode.com/photos

2. Process json data with following logic:
    add "new_photo_id" field, which will be a composite of 2 fields: "albumId" and "id", it's up to you to determine format
    add "new_url" field, which will only contain path, params, query and fragment, extracted from "url" field
        example: url of https://test.org/photos/1.jpg?size=100 => /photos/1.jpg?size=100
    add "timestamp" field, which will contain ISO8601 formatted timestamp of when each entry was processed
3. Write data into TSV file in following columns: "photo_id, title, url, timestamp"
    where "photo_id" is "new_photo_id", "title" is "title", "url" is "new_url", "timestamp" is "timestamp"

    filename format: "photos_YYYY-MM-DD_uuid4"
        example: "photos_2021-05-04_16fd2706-8baf-433b-82eb-8c7fada847da.tsv.gz"
4. Gzip the TSV
5. Upload it to S3 bucket (have configurable credentials) 
6. print the name of the file that was uploaded and its S3 uri


2. Source code directory structure:
   ===============================
source folder containing following folder and files.
source-
	-abstract_client  
	-endpoint_client  
        -tests
aws_main.py
settings.py
requirements.txt
Dockerfile
readme.txt
api_to_aws_.log   



3. Hardware and software:
   =====================

The host operating system used is Ubuntu 18.04, RAM should be 4G.B.
List of the software and library required to installed is mentioned in the requirements.txt.

4. How to run program:
   ===================

from command prompt type below command:
>python aws_main.py

User can use, Pycharm as well.

5. How to run unit test using docker:
   ==================================

Copy the source code from the github: https://github.com/Amit-Singh-N/STRORE_IN_AWS_S3
or clone the repository using below command:

>git clone https://github.com/Amit-Singh-N/STRORE_IN_AWS_S3.git
>cd STRORE_IN_AWS_S3/source

Now build the docker image named "newimage" using below command, this usually take few min. of time.
>sudo docker build -t "newimage:Dockerfile"

Now run the image by running the below command:
>sudo docker run -e AWS_ACCESS_KEY_ID=AKIAY6P2JYSB27K4EN2Y -e AWS_SECRET_ACCESS_KEY=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 newimage:Dockerfile



prerequisite : 
1. docker is installed on the host and docker is running.
2. user should have sudo permission.
3. ubuntu 18.04


