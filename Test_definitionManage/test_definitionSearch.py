#!/usr/bin/python
#coding:utf8
import unittest,sys,os
sys.path.append("..")
from SetUp import request,setUpInfo
from publicMethod import PublicMethod
import json

class TestCase_definitionSearch(unittest.TestCase):
    def setUp(self):
        self.request = request.Httpcommon()
        self.domain = setUpInfo.SetUpInfo().TestEnvi()
        self.publicMethod = PublicMethod()
        if self.publicMethod.getDefinitionId() == None:
            self.definitionId =self.publicMethod.creatDefinitionInfo()
        else:
            self.definitionId = self.publicMethod.getDefinitionId()





#获取已经存在的流程名称作为关键字搜索
    def test_definitionKeywordSearch(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList"
        keyword = self.publicMethod.creatDefinitionInfo()["name"]
        data = '{"enabled":0,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"keyWord":"%s"}' % keyword
        data = str(data)
        response = self.request.request("POST",url,data=data)
        json_response = json.loads(response)
        self.assertEqual(json_response["Result"]["StatusCode"],0,msg=response)
        self.assertEqual(len(json_response["Value"]["outlines"]),1,msg=response)



#搜索关键字不存在的流程
    def test_definitionKeywordSearch2(self):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList"
        keyword = "关键字!@#$%"
        data = '{"enabled":0,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"keyWord":"%s"}' % keyword
        data = str(data)
        response = self.request.request("POST", url, data=data)
        json_response = json.loads(response)
        self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)
        self.assertEqual(len(json_response["Value"]["outlines"]), 0, msg=response)




if __name__=="__main__":
    unittest.main()