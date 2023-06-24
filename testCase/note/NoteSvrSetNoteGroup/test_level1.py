import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import case_logs
from common.logs_create import info_log,error_log,warning_log
from common.data_upload_clear import DataUploadClear

class NoteSvrSetNoteGroupLevel1(unittest.TestCase):
    """新增分组"""

    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    path = "/v3/notesvr/set/notegroup"
    url = host + path
    sid1=env_config["sid1"]
    userid = env_config["userid"]


    @case_logs
    def testCase01_major(self):
        """主流程"""
        info_log("用户jj下新增一个分组")
        body = {"groupId":"group001","groupName":"jj","order":0}
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        expected_body = {"responseTime":int,"updateTime":int}
        ResCheck().res_check(expected_body,response.json())
        self.assertEqual(200,response.status_code)
        DataUploadClear().test_note_delete()
        info_log("删除分组成功")






