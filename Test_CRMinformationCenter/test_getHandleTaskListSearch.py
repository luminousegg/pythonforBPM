#!/usr/bin/python
#coding:utf8



from SetUp import setUpInfo,request
import json,unittest,os,sys
sys.path.append("..")

class Test_getHandleTaskListSearch(unittest.TestCase):

    def setUp(self):
        self.domain = setUpInfo.SetUpInfo().TestEnvi()
        self.request = request.Httpcommon()
        self.url = self.domain+'/FHH/EM1HBPM/ProcessTask/GetHandleTaskList'

    def test_handleTaskListCompletedPass(self):
        #已完成业务流程下，搜索结果不为空
        keyword = "搜索关键字"
        data = '{"isCompleted":true,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"taskName":"%s"}' % keyword
        try:
            response = self.request.request("POST",url=self.url,data=data)
            json_response = json.loads(response)
            self.assertEqual(json_response["Result"]["StatusCode"],0,msg=response)
            self.assertTrue(json_response["Value"]["dataList"] != 0,msg=None)
        except Exception,e:
            return e

    def test_handleTaskListCompletedFaile(self):
        # 已完成业务流程下，搜索结果为空
        keyword = "搜索关键字"
        data = '{"isCompleted":true,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"taskName":"%s"}' % keyword
        try:
            response = self.request.request("POST", url=self.url, data=data)
            json_response = json.loads(response)
            self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)
            self.assertTrue(json_response["Value"]["dataList"] == 0, msg=None)
        except Exception, e:
            return e

    def test_handleTaskListUncompletedPass(self):
        ##未完成业务流程下，搜索结果不为空
        keyword = "搜索关键字"
        data = '{"isCompleted":false,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"taskName":"%s"}' % keyword
        try:
            response = self.request.request("POST", url=self.url, data=data)
            json_response = json.loads(response)
            self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)
            self.assertTrue(json_response["Value"]["dataList"] != 0, msg=None)
        except Exception, e:
            return e

    def test_handleTaskListUncompletedFaile(self):
        #未完成业务流程下，搜索结果为空
        keyword = "搜索关键字"
        data = '{"isCompleted":false,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"taskName":"%s"}' % keyword
        try:
            response = self.request.request("POST", url=self.url, data=data)
            json_response = json.loads(response)
            self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)
            self.assertTrue(json_response["Value"]["dataList"] == 0, msg=None)
        except Exception, e:
            return e

if __name__=="__main__":

    unittest.main()