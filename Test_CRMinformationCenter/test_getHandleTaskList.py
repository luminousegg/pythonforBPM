#!/usr/bin/python
#coding:utf8



from SetUp import setUpInfo,request
import json,unittest,os,sys
sys.path.append("..")

class Test_getHandleTaskList(unittest.TestCase):

    def setUp(self):
        self.domain = setUpInfo.SetUpInfo().TestEnvi()
        self.request = request.Httpcommon()

    def test_GetHandleTaskListCompleted(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessTask/GetHandleTaskList"
        data = '{"isCompleted":true,"pageSize":20,"pageNumber":1}'

        try:
            response = self.request.request("POST", url, data)
            json_response = json.loads(response)
            self.assertEqual(json_response["Result"]["StatusCode"],0,msg=response)
        except Exception,e:
            return e

    def test_GetHandleTaskListUncompleted(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessTask/GetHandleTaskList"
        data = '{"isCompleted":false,"pageSize":20,"pageNumber":1}'

        try:
            response = self.request.request("POST", url, data)
            json_response = json.loads(response)
            self.assertEqual(json_response["Result"]["StatusCode"],0,msg=response)
        except Exception,e:
            return e

if __name__=="__main__":

    unittest.main()