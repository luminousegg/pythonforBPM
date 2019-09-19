#!/usr/bin/python
#coding:utf8
import unittest,sys,os
sys.path.append("..")
from SetUp import request,setUpInfo
from publicMethod import PublicMethod
import json

class TestCase_definitionManger(unittest.TestCase):
    def setUp(self):
        self.request = request.Httpcommon()
        self.domain = setUpInfo.SetUpInfo().TestEnvi()
        self.publicMethod = PublicMethod()
        if self.publicMethod.getDefinitionId() == None:
            self.definitionId =self.publicMethod.creatDefinitionInfo()
        else:
            self.definitionId = self.publicMethod.getDefinitionId()





# TestCase 2  停用流程接口，停用一个启用中的流程

    def test_disableDefinition(self):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/UpdateDefinitionStatus"
        id = self.definitionId
        data = '{"ids":"%s","enabled":false}' % id
        response = self.request.request("POST", url, data=data)
        json_response = json.loads(response)
        self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)
        definitionStatus = self.publicMethod.getDefinitionStatus(id=id, enable=2)
        self.assertEqual(definitionStatus["enabled"],False,msg=definitionStatus)


# TestCase 3  启用流程接口，启用一个停用中的流程

    def test_enableDefinition(self,id=None):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/UpdateDefinitionStatus"
        id = self.definitionId
        data = '{"ids":"%s","enabled":true}' % id
        response = self.request.request("POST", url, data=data)
        json_response = json.loads(response)
        self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)
        definitionStatus = self.publicMethod.getDefinitionStatus(id=id, enable=1)
        self.assertEqual(definitionStatus["enabled"], True, msg=definitionStatus)




if __name__=="__main__":
    unittest.main()
