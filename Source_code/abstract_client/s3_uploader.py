import botocore
import boto3
import logging
from io import BytesIO
import sys
import settings as settings
from abstract_client.aws_client import AbstractAwsS3

logger = logging.getLogger(__name__)


class AmazonS3Uploader(AbstractAwsS3):
    S3_SERVICE = 's3'

    def __init__(self, **kwargs):
        assert kwargs.get('SECRET_ACCESS_KEY'), 'aws secret access key missing'
        self.aws_secret_access_key = kwargs.get('SECRET_ACCESS_KEY')

        assert kwargs.get('ACCESS_KEY_ID'), 'aws_access_key_id is missing'
        self.aws_access_key_id = kwargs.get('ACCESS_KEY_ID')

        assert kwargs.get('BUCKET_NAME'), 'bucket name missing'
        self.bucket = kwargs.get('BUCKET_NAME')

        self.file_name = settings.FILE_NAME

        self.client = boto3.client(__class__.S3_SERVICE,
                                   aws_access_key_id=self.aws_access_key_id,
                                   aws_secret_access_key=self.aws_secret_access_key)
        try:
            if not self.check_bucket(self.bucket):
                raise Exception('Bucket Not Found')
        except Exception as exc:
            raise exc

    def check_bucket(self, bucket):
        """
        check the bucket
        :param bucket: bucket name
        :return: True
        """
        try:
            self.client.head_bucket(Bucket=bucket)
            return True
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 403:
                raise Exception("Private Bucket. Forbidden Access!")
            elif error_code == 404:
                raise Exception("Bucket Does Not Exist!")

    def pre_send(self):
        """
        open the file and upload as object
        :return: file name
        """
        object_name = self.file_name
        try:
            with open(self.file_name, "rb") as f:
                response = self.client.upload_fileobj(f, self.bucket, object_name)
            return object_name
        except Exception as exc:
            logger.error("exception when opening file : {}".format(exc))
            sys.exit(exc)

    def upload(self):
        """
        upload a file and return uri
        :return: uri
        """

        logger.info("uploading a file...")
        try:
            key = self.bucket
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(self.bucket)
            response = bucket.upload_file(self.file_name, key)
            location = boto3.client('s3').get_bucket_location(Bucket=self.bucket)['LocationConstraint']
            uri = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket, key)
            logger.info("uri : {}".format(uri))
            return uri
        except Exception as exc:
            logger.error("Exception when loading a file ..{}".format(exc))
            sys.exit(exc)

    def post_send(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass


