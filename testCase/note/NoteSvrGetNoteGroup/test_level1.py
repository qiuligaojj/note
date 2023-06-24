import unittest
import requests
import json
from common.resCheck import ResCheck
from common.read_yml import ReadYaml
from business_common.requests_demo import RequestsDemo
from common.logs_create import case_logs
from common.logs_create import info_log,error_log,warning_log
from common.data_upload_clear import DataUploadClear

class NoteSvrGetNoteGroupLevel1(unittest.TestCase):
    """获取分组列表"""
    env_config = ReadYaml().env_yaml()
    host = env_config["host"]
    path = "/v3/notesvr/get/notegroup"
    url = host + path
    sid1=env_config["sid1"]
    userid = env_config["userid"]

    @case_logs
    def testCase01_major(self):
        """主流程"""
        DataUploadClear().test_group_add()
        info_log("新增分组成功")
        info_log("获取用户jj的分组列表")
        body = {"excludeInvalid":"true"}
        response = RequestsDemo().Post(self.url,self.sid1,self.userid,body)
        expected_body = {"requestTime":int,"noteGroups":list}
        ResCheck().res_check(expected_body,response.json())
        expected_body_son={"userId":str,"groupId":str,"groupName":str,"order":int,"valid":int,"updateTime":int}
        ResCheck().res_check(expected_body_son,response.json()["noteGroups"][0])
        self.assertEqual(200,response.status_code)
        DataUploadClear().test_group_delete()
        info_log("删除分组成功")





