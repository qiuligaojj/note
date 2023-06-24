import requests
import time
from  common.logs_create import info_log,warning_log,error_log

class RequestsDemo():
    def Get(self,url,sid1):
        headers = {"Cookie":f"wps_sid={sid1}"}
        response = requests.get(url = url,headers =headers,timeout = 3)
        info_log(f"url : {url}")
        info_log(f"headers :{headers}")
        info_log(f"response : {response.text}")
        info_log(f"code : {response.status_code}")
        return response


    def Post(self,url,sid1,userid,body):
        headers = {"cookie":"wps_sid={}".format(sid1),"X-user-key":"{}".format(userid)}
        response = requests.post(url=url,headers=headers,json=body)
        info_log(f"url : {url}")
        info_log(f"headers :{headers}")
        info_log(f"request body:{body}")
        info_log(f"response body: {response.text}")
        info_log(f"code : {response.status_code}")
        return response



























