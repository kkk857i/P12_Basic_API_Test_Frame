import unittest
import json
from common import HTMLTestReportCN
from common.localconfig_utils import local_config

def get_all_cases_suite():
    discover=unittest.defaultTestLoader.discover(
        start_dir='./testcases',
        pattern='*_cases01.py',
        top_level_dir='./testcases'
    )

    all_cases_suite=unittest.TestSuite()
    all_cases_suite.addTest(discover)
    return all_cases_suite

report_dir=HTMLTestReportCN.ReportDirectory(local_config.REPORT_PATH +'/')
report_dir.create_dir('API_TEST_')
# dir_path=HTMLTestReportCN.GlobalMsg.get_value('dir_path')
report_path=HTMLTestReportCN.GlobalMsg.get_value('report_path')
fp=open(report_path,'wb')

# print(report_path)
# print(report_path.text)
# if report_path is None:'continue'


runner=HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                       tester="testk",
                                       title="testk_API_TEST",
                                       description='study~~'
                                       )


runner.run(get_all_cases_suite())
fp.close()