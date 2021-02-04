import json
import requests
import unittest
from common.localconfig_utils import local_config
from common.log_utils import logger

class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts=local_config.URL
        self.session=requests.session()
    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        logger.info('[case03]创建用户标签接口')
        params = {
            'grant_type': 'client_credential',
            'appid': 'wx15938bc8b042cee0',
            'secret': 'f01c3e1836d6b40fb24db5dbc0142253'
        }
        get_access_token_response = self.session.get(url=self.hosts + '/cgi-bin/token',
                             params=params
                             )
        token_id=get_access_token_response.json()['access_token']

        get_params = {
            'access_token': token_id
        }
        post_params ='{"tag":{"name":"newman28"}}'
        headers = {
            'content_type': 'application/json'
        }

        create_tag_response = requests.post(url=self.hosts + '/cgi-bin/tags/create',
                              params=get_params,
                              data=post_params,
                              headers=headers
                              )

        # print(create_tag_response.json())

        actual_result=create_tag_response.json()["tag"]["name"]
        self.assertEqual(actual_result,'newman28')
        # print(actual_result.json())

if __name__=="__main__":
    unittest.main()
