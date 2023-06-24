import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import log_class_methods
from common.logs_create import case_logs
from common.logs_create import info_log, error_log, warning_log
from common.data_upload_clear import DataUploadClear
import time


@log_class_methods
class NoteSvrSetNoteInfoLevel1(unittest.TestCase):
    """上传/更新便签信息主体"""
    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    path = "/v3/notesvr/set/noteinfo"
    url = host + path
    sid1 = env_config["sid1"]
    userid = env_config["userid"]

    def test01_upload_note_info(self):
        """主流程"""
        num = 2
        info_log("上传用户jj的便签主体")
        for i in range(num):
            noteId = str(int(time.time()))
            body = {"noteId": f"{noteId}", "star": 1, "remindTime": 1, "remindType": 1, "groupId": "001"}
            response = RequestsDemo().Post(self.url, self.sid1, self.userid, body)
            time.sleep(1)
        expected_body = {"responseTime": int, "infoVersion": int, "infoUpdateTime": int}
        ResCheck().res_check(expected_body, response.json())
        self.assertEqual(200, response.status_code)

    def test02_note_info_noteid_miss(self):
        """不传noteId"""
        info_log("上传用户jj的便签，不传noteId")
        body = {"noteId": "001", "star": 1, "remindTime": 1, "remindType": 1, "groupId": "001"}
        body.pop("noteId")
        response = RequestsDemo().Post(self.url, self.sid1, self.userid, body)
        self.assertEqual(-7, response.json()["errorCode"])
        self.assertEqual(500,response.status_code)

    def test03_note_info_noteid_none(self):
        """noteId传空字符串"""
        info_log("上传用户jj的便签，传空的noteId")
        body = {"noteId": "001", "star": 1, "remindTime": 1, "remindType": 1, "groupId": "001"}
        body["noteId"] = ""
        response = RequestsDemo().Post(self.url, self.sid1, self.userid, body)
        self.assertEqual(-7, response.json()["errorCode"])
        self.assertEqual(500, response.status_code)


    def test04_note_info_redeat(self):
        """验证数据重复请求"""
        info_log("重复请求接口成功")
        body = {"noteId": "001", "star": 1, "remindTime": 1, "remindType": 1, "groupId": "001"}
        response = RequestsDemo().Post(self.url, self.sid1, self.userid, body)
        print(response.status_code)
        self.assertEqual(200,response.status_code)

    def test05_note_info_headers_miss(self):
        """验证无请求头"""
        info_log("不填写请求头发送接口请求")
        body = {"noteId": "001", "star": 1, "remindTime": 1, "remindType": 1, "groupId": "001"}
        response = requests.post(url=self.url, json=body)
        self.assertEqual(-2009, response.json()["errorCode"])
        self.assertEqual(401, response.status_code)
        info_log(f"url : {self.url}")
        info_log(f"request body:{body}")
        info_log(f"response body: {response.text}")
        info_log(f"code : {response.status_code}")





