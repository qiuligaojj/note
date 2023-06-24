import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import case_logs
from common.logs_create import info_log,error_log,warning_log
from common.data_upload_clear import DataUploadClear

class NoteSvrWebGetNotesRemindLevel1(unittest.TestCase):
    """查看日历下的便签"""
    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    path = "/v3/notesvr/web/getnotes/remind"
    url = host + path
    sid1=env_config["sid1"]
    userid = env_config["userid"]


    @case_logs
    def testCase01_major(self):
        """主流程"""
        groupId = DataUploadClear().group_add(sid1 = self.sid1,userid=self.userid)
        num = 2
        noteIdnote = DataUploadClear().upload_calendar_note(self.userid, self.sid1, num,group = groupId)
        info_log("查看用户jj的日历下的便签")
        body = {"remindStartTime":1685589770,"remindEndTime":1687231370,"startIndex":0,"rows":10}
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        expected_body = {"responseTime":int,"webNotes":list}
        expected_body_son = {"noteId":str,"createTime":int,"star":int,"remindTime":int,"remindType":int,"infoVersion":int,"infoUpdateTime":int,"groupId":str,"title":str,"summary":str,"thumbnail":type(None),"contentVersion":int,"contentUpdateTime":int}
        ResCheck().res_check(expected_body,response.json())
        ResCheck().res_check(expected_body_son,response.json()["webNotes"][0])
        self.assertEqual(200,response.status_code)
        DataUploadClear().note_delete(noteId1=noteIdnote,num = num,sid1=self.sid1,userid=self.userid,rows=self.rows)






