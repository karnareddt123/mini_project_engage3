import logging
from io import BytesIO
import sys
import settings
from endpoint_client.abstract_endpoint import AbstractEndpoint
import requests
import datetime
import csv
import gzip
import shutil


logger = logging.getLogger(__name__)


class EndPointDownloader(AbstractEndpoint):

    def __init__(self, **kwargs):
        self.json_endpoint = settings.JSON_ENDPOINT
        self.file_name = settings.FILE_NAME
        try:
            if not self.json_endpoint:
                raise Exception('endpoint Not Found')
        except Exception as exc:
            raise exc
        requested_file = requests.get(self.json_endpoint)
        self.json_list_records = requested_file.json()

    def download_json(self, *args, **kwargs):
        """
        Download a json from the endpoint
        :return: 1 success
        """
        try:
            with open(self.file_name, 'wt') as out_file:
                for json_record in self.json_list_records:
                    json_record['new_photo_id'] = str(json_record['albumId']) + str(json_record['id'])
                    # print(json_record)
                    json_record['new_uri'] = json_record['url'].split(".com", 1)[-1]
                    # print(json_record['url'].split(".com", 1)[-1])
                    json_record['timestamp'] = datetime.datetime.now().isoformat()
                    # print(json_record)
                    value_photo_id = int(str(json_record['albumId']) + str(json_record['id']))
                    # print("photo_id ", value_photo_id)
                    logger.info("photo_id : {}, title : {} , uri : {}, timestamp : {}".format(int(value_photo_id),json_record['title'],json_record['url'].split(".com", 1)[-1],datetime.datetime.now().isoformat()))
                    tsv_writer = csv.writer(out_file, delimiter='\t')
                    tsv_writer.writerow(['photo_id', int(value_photo_id)])
                    tsv_writer.writerow(['title', json_record['title']])
                    tsv_writer.writerow(['url', json_record['url'].split(".com", 1)[-1]])
                    tsv_writer.writerow(['timestamp', datetime.datetime.now().isoformat()])
                    self.convert_to_gz()
            return 1
        except Exception as exc:
            logger.error("Exception at download_json : {} ".format(exc))
            sys.exit(exc)


    def convert_to_gz(self):
        """
        convert file to the gz
        :return: 1 success
        """
        if self.file_name is None:
            return -1
        try:
            with open(self.file_name, 'rb') as f_in:
                #logger.info("open a file ...")
                with gzip.open(self.file_name + '.gz', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            return 1
        except Exception as exc:
            logger.error("Exception occurred at convert_to_gz : {}".format(exc))

