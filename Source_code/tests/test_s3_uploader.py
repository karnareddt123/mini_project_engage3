import pytest
from abstract_client.s3_uploader import AmazonS3Uploader
import settings

class TestS3UPloader():
    def test_check_bucket(self):
        aws_conf_setting = settings.aws_settinigs
        s3_object = AmazonS3Uploader(**aws_conf_setting)
        assert  s3_object.check_bucket(settings.aws_settinigs.get('BUCKET_NAME')) == 1

    def test_upload(self):
        aws_conf_setting = settings.aws_settinigs
        s3_object = AmazonS3Uploader(**aws_conf_setting)
        val2 = s3_object.upload()
        assert 'amazonaws.com' in val2