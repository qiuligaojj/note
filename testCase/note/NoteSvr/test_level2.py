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

    def test1_userid_not_int(self):
        """userid非int类型"""
        userid = "256665263"
        path = "/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes".format(userid, self.startindex, self.rows)
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        expected_body = {"responseTime": int, "webNotes": list}
        ResCheck().res_check(expected_body, response.json())
        self.assertEqual(400, response.status_code)

    def test1_webNotes_none(self):
        """无返回数据时，webNotes返回为空"""
        noteId1 = []
        headers = {"Cookie": f"wps_sid={self.sid1}"}
        path = "/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes".format(self.userid, self.startindex, self.rows)
        url = self.host + path
        responsedele = requests.get(url=url, headers=headers)
        num = len(responsedele.json()["webNotes"])
        for i in range(num):
            noteIdres = responsedele.json()["webNotes"][i - 1]["noteId"]
            noteId1.append(noteIdres)
        DataUploadClear().note_delete(noteId1=noteId1, num=num, sid1=self.sid1, userid=self.userid)
        responsequery = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(200, responsequery.status_code)

    def test2_len_rows(self):
        """测试返回数据条数是否正常"""
        groupId = DataUploadClear().group_add(sid1=self.sid1, userid=self.userid)
        num = 15
        noteId1 = DataUploadClear().upload_note(self.userid, self.sid1, num,group=groupId)
        info_log("新增便签主体和内容")
        info_log("获取用户jj的首页便签")
        path = "/v3/notesvr/user/{}/home/startindex/{}/rows/{}/notes".format(self.userid, self.startindex, self.rows)
        url = self.host + path
        response = RequestsDemo().Get(url=url, sid1=self.sid1)
        self.assertEqual(self.rows, len(response.json()["webNotes"]))
        DataUploadClear().note_delete(noteId1=noteId1, num=num, sid1=self.sid1, userid=self.userid)
