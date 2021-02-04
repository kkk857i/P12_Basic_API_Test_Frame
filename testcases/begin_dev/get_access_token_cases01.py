import requests
import unittest
import json
from common.localconfig_utils import local_config
from common.log_utils import logger
from common.common_api import *

class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session=requests.session()
    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        """[case01]正常测试access_token值测试"""
        logger.info('[case01]正常测试access_token值测试')

        actual_result = get_access_token_api(self.session,
                                             'client_credential',
                                             'wx15938bc8b042cee0',
                                             'f01c3e1836d6b40fb24db5dbc0142253'
                                     )
        self.assertEqual(actual_result.json()['expires_in'], 7200)

    def test_appid_error(self):
        self._testMethodDoc='[case02]appid错误时测试'
        logger.info('[case02]appid错误时测试')
        actual_result = get_access_token_api(self.session,
                                             'client_credential',
                                             'wx15938bc8b042cee',
                                             'f01c3e1836d6b40fb24db5dbc0142253'
                                             )
        # print(actual_result.text)
        self.assertEqual(actual_result.json()['errcode'],40013)


if __name__ == "__main__":
    unittest.main()



