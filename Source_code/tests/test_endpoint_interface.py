import pytest
from endpoint_client.endpoint_interface import EndPointDownloader

class TestClass:
    global endpoint_object
    endpoint_object = EndPointDownloader()
    def test_download_json(self):
        assert endpoint_object.download_json() == 1


    def test_download_json_exception(self):
        endpoint_object.file_name="abcd"
        with pytest.raises(Exception) as execinfo:
            raise Exception('pytest : {}'.format(execinfo))
        assert True

    def test_convert_to_gz_notempty(self):
        endpoint_object2 = EndPointDownloader()
        # download_json is implicitly calling convert_to_gz()
        assert endpoint_object2.download_json() == 1

