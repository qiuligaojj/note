import unittest
import requests
from common.read_yml import ReadYaml
import time
from common.logs_create import info_log,error_log,warning_log


class DataUploadClear(unittest.TestCase):
    env_config = ReadYaml().env_yaml()
    host = env_config["host"]


    def upload_note(self,userid,sid1,num,group):
        """上传/更新便签信息主体以及上传/更新便签内容"""
        info_log("上传/更新便签信息主体以及上传/更新便签内容")
        pathinfo = "/v3/notesvr/set/noteinfo"
        pathcontent = "/v3/notesvr/set/notecontent"
        urlinfo = self.host + pathinfo
        urlcontent = self.host + pathcontent
        headers = {"Cookie": "wps_sid={}".format(sid1), "X-user-key": "{}".format(userid)}
        noteId1=[]
        for i in range(num):
            noteId = str(int(time.time()))
            noteId1.append(noteId)
            bodyinfo = {"noteId": noteId, "star": 1, "groupId": "{}".format(group)}
            response1 = requests.post(url=urlinfo, headers=headers, json=bodyinfo)
            infoVersion = response1.json()["infoVersion"]
            self.assertEqual(200, response1.status_code)

            bodycontent = {"noteId": noteId, "title": "abc", "summary": "abc", "body": "abc",
                    "localContentVersion": infoVersion,
                    "BodyType": 0}
            response2 = requests.post(url=urlcontent, headers=headers, json=bodycontent)
            self.assertEqual(200, response2.status_code)
            time.sleep(1)
        return noteId1

    def upload_calendar_note(self,userid,sid1,num,group):
        """上传/更新日历便签信息主体以及上传/更新日历便签内容"""
        info_log("上传/更新便签信息主体以及上传/更新便签内容")
        pathinfo = "/v3/notesvr/set/noteinfo"
        pathcontent = "/v3/notesvr/set/notecontent"
        urlinfo = self.host + pathinfo
        urlcontent = self.host + pathcontent
        headers = {"Cookie": "wps_sid={}".format(sid1), "X-user-key": "{}".format(userid)}
        noteId1=[]
        for i in range(num):
            noteId = str(int(time.time()))
            noteId1.append(noteId)
            bodyinfo = {"noteId": noteId, "star": 1, "remindTime":1,"remindType":0,"groupId": "{}".format(group)}
            response1 = requests.post(url=urlinfo, headers=headers, json=bodyinfo)
            infoVersion = response1.json()["infoVersion"]
            self.assertEqual(200, response1.status_code)

            bodycontent = {"noteId": noteId, "title": "abc", "summary": "abc", "body": "abc",
                    "localContentVersion": infoVersion,
                    "BodyType": 0}
            response2 = requests.post(url=urlcontent, headers=headers, json=bodycontent)
            self.assertEqual(200, response2.status_code)
            time.sleep(1)
        return noteId1

    def note_delete(self, noteId1,num,sid1,userid):
        """删除便签  软删除"""
        info_log("删除便签")
        path = "/v3/notesvr/delete"
        url = self.host + path
        headers = {"Cookie": "wps_sid={}".format(sid1), "X-user-key": "{}".format(userid)}
        for i in range(num):
            body = {"noteId": noteId1[i-1]}
            response = requests.post(url=url, headers=headers, json=body)
            self.assertEqual(200, response.status_code)

    def group_add(self,sid1,userid):
        """新增分组"""
        info_log("新增分组")
        headers = {"Cookie": "wps_sid={}".format(sid1), "X-user-key": "{}".format(userid)}
        path = "/v3/notesvr/set/notegroup"
        url = self.host + path
        groupId = "group{}".format(int(time.time()))
        body = {"groupId": groupId, "groupName": "pipi", "order": 0}
        response = requests.post(url=url, headers=headers, json=body)
        self.assertEqual(200, response.status_code)
        return groupId

    def group_delete(self,sid1,userid):
        """删除分组"""
        headers = {"Cookie": "wps_sid={}".format(sid1), "X-user-key": "{}".format(userid)}
        path = "/v3/notesvr/delete/notegroup"
        url = self.host + path
        body = {"groupId": "group999"}
        response = requests.post(url=url, headers=headers, json=body)
        self.assertEqual(200, response.status_code)

