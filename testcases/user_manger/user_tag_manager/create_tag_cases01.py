import json
import requests
import unittest
from common.localconfig_utils import local_config
from common.log_utils import logger
from common.common_api import *

class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts=local_config.URL
        self.session=requests.session()
    def tearDown(self) -> None:
        pass

    def test_add_tag(self): #1提供测试数据，2测试步骤操作，3断言判定
        logger.info('[case03]创建用户标签接口')
        token_id = get_access_token_value(self.session)
        # print(token_id)
        post_params ='{   "tag" : {     "name" : "上海仁"   } }'

        create_tag_response = create_user_tag_api(self.session,token_id,post_params)

        print(create_tag_response.json())

        actual_result=create_tag_response.json()["tag"]["name"]
        self.assertEqual(actual_result,'上海仁')
        print(actual_result.json())

if __name__=="__main__":
    unittest.main()
