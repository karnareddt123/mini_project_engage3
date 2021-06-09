import logging.config
import signal
import sys
import settings as settings
from abstract_client.s3_uploader import AmazonS3Uploader
from endpoint_client.endpoint_interface import EndPointDownloader


# signal handler for Ctrl+C key press
def signal_handler(signal, frame):
    print('pressed Ctrl+C!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == '__main__':
    try:
        logging.config.dictConfig(settings.logging)
        logger = logging.getLogger(__name__)
        logger.info("Main program started...")
    except KeyError as exc:
        msg = 'failed to create '
        logger.error(msg)
        sys.exit('failed to create ' + exc.__str__())

    try:
        endpoint_object = EndPointDownloader()
    except Exception as exc:
        logger.error("Exception when calling EndPointDownloader : {} ".format(exc))

    try:
        endpoint_object.download_json()
    except Exception as exc:
        logger.error("Exception when calling download_json : {} ".format(exc))

    try:
        endpoint_object.convert_to_gz()
    except Exception as exc:
        logger.error("Exception when calling convert_to_gz : {} ".format(exc))

    try:
        logger.info("acquiring aws credentials...")
        aws_conf_setting = settings.aws_settinigs
    except (AttributeError, KeyError) as exc:
        msg = 'Incorrect settings '
        logger.error(msg)
        sys.exit(exc)

    aws_client = AmazonS3Uploader(**aws_conf_setting)
    file_name = aws_client.pre_send()
    logger.info("File name : {}".format(file_name))

    uri = aws_client.upload()
    logger.info("URI : {}".format(uri))
