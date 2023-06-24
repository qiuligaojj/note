import unittest
import requests
from common.read_yml import ReadYaml
from common.logs_create import log_class_methods
from business_common.requests_demo import RequestsDemo
from common.logs_create import info_log,error_log,warning_log

@log_class_methods
class NoteSvrSetNoteInfoLevel2(unittest.TestCase):
    """上传/更新便签信息主体"""
    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    path = "/v3/notesvr/set/noteinfo"
    url = host + path
    sid1=env_config["sid1"]
    userid = env_config["userid"]

    def testcase01_upload_note_info(self):
        """noteId传空字符串"""
        info_log("上传用户jj的便签，不传noteId")
        body = {"noteId":"001","star":1,"remindTime":1,"remindType":1, "groupId":"001"}
        body["noteId"] = ""
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        self.assertEqual(-7, response.json()["errorCode"])
        self.assertEqual(500, response.status_code)

    def testCase02_upload_note_info_starMiss(self):
        """不传star的场景"""
        info_log("上传用户jj的便签，不传noteId")
        body = {"noteId":"001","star":1,"remindTime":1,"remindType":1, "groupId":"001"}
        body.pop("star")
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        self.assertEqual(200,response.status_code)

    def testCase03_upload_note_info_remind_time_miss(self):
        """不传remindTime的场景"""
        info_log("上传用户jj的便签，不传noteId")
        body = {"noteId":"001","star":1,"remindTime":1,"remindType":1, "groupId":"001"}
        body.pop("remindTime")
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        self.assertEqual(200,response.status_code)

    def testCase02_upload_note_info_remind_type_miss(self):
        """不传remindType的场景"""
        info_log("上传用户jj的便签，不传noteId")
        body = {"noteId":"001","star":1,"remindTime":1,"remindType":1, "groupId":"001"}
        body.pop("remindType")
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        self.assertEqual(200,response.status_code)