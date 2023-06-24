import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import log_class_methods
from common.logs_create import info_log, error_log, warning_log
from common.data_upload_clear import DataUploadClear
import time


@log_class_methods
class NoteSvrSetNoteInfoLevel1(unittest.TestCase):
    """获取首页便签"""
    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    startindex = 0
    rows = 10
    sid1 = env_config["sid1"]
    userid = env_config["userid"]

    def test01_notes(self):
        """主流程"""
        groupId = DataUploadClear().group_add(sid1=self.sid1, userid=self.userid)
        num = 2
        info_log("新增便签主体和内容")
        noteIdnote = DataUploadClear().upload_note(self.userid, self.sid1, num, group=groupId)
        info_log("获取用户jj的首页便签")
        path = "/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes".format(self.userid, self.startindex, self.rows)
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        expected_body = {"responseTime": int, "webNotes": list}
        expected_body_son = {"noteId": str, "createTime": int, "star": int, "remindTime": int, "remindType": int,
                             "infoVersion": int, "infoUpdateTime": int, "groupId": str, "title": str, "summary": str,
                             "thumbnail": type(None), "contentVersion": int, "contentUpdateTime": int}
        ResCheck().res_check(expected_body, response.json())
        ResCheck().res_check(expected_body_son, response.json()["webNotes"][0])
        DataUploadClear().note_delete(noteId1=noteIdnote, num=num, sid1=self.sid1, userid=self.userid)

    def test02_notes_userid_miss(self):
        """userid不填校验"""
        info_log("校验userid不填写时能否获取首页便签")
        path = f"/v3/notesvr/user/home/startindex/{self.startindex}/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(404, response.status_code)

    def test03_notes_startindex_miss(self):
        """startindex不填校验"""
        info_log("校验startindex不填写时能否获取首页便签")
        path = f"/v3/notesvr/user/{self.userid}/home/startindex/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(404, response.status_code)

    def test04_notes_rows_miss(self):
        """rows不填校验"""
        info_log("校验rows不填写时能否获取首页便签")
        path = f"/v3/notesvr/user/{self.userid}/home/startindex/{self.startindex}/rows/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(404, response.status_code)

    def test05_notes_other_userid(self):
        """校验越权"""
        self.userid = 256665262
        info_log("校验用户jj能否使用其他用户的userid获取其的首页便签")
        path = f"/v3/notesvr/user/{self.userid}/home/startindex/{self.startindex}/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(412, response.status_code)
        self.assertEqual(-1011, response.json()["errorCode"])

    def test06_notes_other_userid(self):
        """校验越权"""
        sid1 = "V02SQdY3jnKrwl8qWzBhOUMN1ATHM7w00a306139000f4c06af"
        info_log("校验用户jj能否使用其他用户的userid获取其的首页便签")
        path = f"/v3/notesvr/user/{self.userid}/home/startindex/{self.startindex}/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=sid1)
        self.assertEqual(401, response.status_code)
        self.assertEqual(-2010, response.json()["errorCode"])

    def test07_notes_userid_none(self):
        """userid为空校验"""
        info_log("校验userid为空时能否获取首页便签")
        self.userid = ""
        path = f"/v3/notesvr/user/{self.userid}/home/startindex/{self.startindex}/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(404, response.status_code)

    def test08_notes_userid_none(self):
        """startindex为空校验"""
        info_log("校验startindex为空时能否获取首页便签")
        self.startindex = ""
        path = f"/v3/notesvr/user/{self.userid}/home/startindex/{self.startindex}/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(404, response.status_code)

    def test09_notes_userid_none(self):
        """rows为空校验"""
        info_log("校验rows为空时能否获取首页便签")
        self.rows = ""
        path = f"/v3/notesvr/user/{self.userid}/home/startindex/{self.startindex}/rows/{self.rows}/notes"
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(404, response.status_code)

    def test10_notes_headers_none(self):
        """headers值为空校验"""
        headers = {"Cookie": ""}
        path = "/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes".format(self.userid, self.startindex, self.rows)
        url = self.host + path
        response = requests.get(url=url, headers=headers, timeout=3)
        self.assertEqual(401, response.status_code)
        self.assertEqual(-2009, response.json()["errorCode"])

    def test10_notes_headers_miss(self):
        """headers不填写校验"""
        headers = {}
        path = "/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes".format(self.userid, self.startindex, self.rows)
        url = self.host + path
        response = requests.get(url=url, headers=headers, timeout=3)
        self.assertEqual(401, response.status_code)
        self.assertEqual(-2009, response.json()["errorCode"])
