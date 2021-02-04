import requests
import unittest
import json
from common.localconfig_utils import local_config
from common.log_utils import logger

class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session=requests.session()
    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        """[case01]正常测试access_token值测试"""
        logger.info('[case01]正常测试access_token值测试')
        params = {

            'grant_type': 'client_credential',
            'appid': 'wx15938bc8b042cee0',
            'secret': 'f01c3e1836d6b40fb24db5dbc0142253'
        }
        actual_result = self.session.get(url=self.hosts + '/cgi-bin/token',
                                     params=params
                                     )
        self.assertEqual(actual_result.json()['expires_in'], 7200)

    def test_appid_error(self):
        self._testMethodDoc='[case02]appid错误时测试'
        logger.info('[case02]appid错误时测试')
        params = {
            'grant_type': 'client_credential',
            'appid': 'wx15938bc8b042cee',
            'secret': 'f01c3e1836d6b40fb24db5dbc0142253'
        }
        actual_result = self.session.get(url=self.hosts + '/cgi-bin/token',
                                     params=params
                                     )
        # print(actual_result.text)
        self.assertEqual(actual_result.json()['errcode'],40013)


if __name__ == "__main__":
    unittest.main()



