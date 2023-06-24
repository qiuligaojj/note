import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import case_logs
from common.logs_create import info_log,error_log,warning_log

class NoteSvrIserInvalidStartindexRowsNotesLevel1(unittest.TestCase):
    """查看回收站下便签列表"""

    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    sid1=env_config["sid1"]
    userid = env_config["userid"]
    startindex = 0
    rows = 10


    @case_logs
    def testCase01_major(self):
        """主流程"""
        info_log("查看用户jj回收站下的便签列表")
        path = f"/v3/notesvr/user/{self.userid}/invalid/startindex/{self.startindex}/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url,self.sid1)
        expected_body = {"responseTime":int,"webNotes":list}
        expected_body_son = {"noteId":str,"createTime":int,"star":int,"remindTime":int,"remindType":int,"infoVersion":int,"infoUpdateTime":int,"groupId":str,"title":str,"summary":str,"thumbnail":str,"contentVersion":int,"contentUpdateTime":int}
        ResCheck().res_check(expected_body,response.json())
        ResCheck().res_check(expected_body_son,response.json()["webNotes"][0])
        self.assertEqual(200,response.status_code)









