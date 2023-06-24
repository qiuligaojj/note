import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import case_logs
from common.logs_create import info_log,error_log,warning_log
from common.data_upload_clear import DataUploadClear

class NoteSvrDeleteLevel1(unittest.TestCase):
    """删除便签 软删除"""

    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    path = "/v3/notesvr/delete"
    url = host + path
    sid1=env_config["sid1"]
    userid = env_config["userid"]


    @case_logs
    def testCase01_major(self):
        """主流程"""
        DataUploadClear().test_body_upload()
        info_log("新增便签成功")
        info_log("删除用户jj的便签内容 软删除")
        body = {"noteId":"002"}
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        expected_body = {"responseTime":int}
        ResCheck().res_check(expected_body,response.json())
        self.assertEqual(200,response.status_code)






