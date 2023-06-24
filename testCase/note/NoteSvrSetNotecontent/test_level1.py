import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import case_logs
from common.logs_create import info_log,error_log,warning_log

class NoteSvrSetNotecontentLevel1(unittest.TestCase):
    """上传/更新便签内容"""

    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    path = "/v3/notesvr/set/notecontent"
    url = host + path
    sid1=env_config["sid1"]
    userid = env_config["userid"]


    @case_logs
    def testCase01_uploadNoteContent(self):
        """主流程"""
        info_log("上传用户jj的便签内容")
        body = {"noteId":"001","title":"abc","summary":"abc","body":"abc", "localContentVersion":8,"BodyType":0}
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        expected_body = {"responseTime":int,"contentVersion":int,"contentUpdateTime":int}
        ResCheck().res_check(expected_body,response.json())
        self.assertEqual(200,response.status_code)



