#!/usr/bin/python
# coding:utf8
import unittest, sys, os

sys.path.append("..")
from SetUp import request
from SetUp import setUpInfo
from publicMethod import PublicMethod
import json


class TestCase_definitionDel(unittest.TestCase):
    def setUp(self):
        self.request = request.Httpcommon()
        self.domain = setUpInfo.SetUpInfo().TestEnvi()
        self.publicMethod = PublicMethod()




    # 删除一个停用的流程
    def test_delDisenableDefinition(self, id=None):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/DeleteDefinition"
        if self.publicMethod.getDefinitionId() == None:
            self.definitionId = self.publicMethod.createDefinition()
        else:
            self.definitionId = self.publicMethod.getDefinitionId()
        self.publicMethod.disableDefinition(id=self.definitionId)

        data = '{"id":"%s"}' % str(self.definitionId)
        result = self.request.request("POST", url, data=data)


# 删除一个启用状态的流程（不可删除，给出提示信息）

    def test_delEnableDefinition(self, id=None):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/DeleteDefinition"
        if self.publicMethod.getDefinitionId() == None:
            self.definitionId = self.publicMethod.createDefinition()
        else:
            self.definitionId = self.publicMethod.getDefinitionId()

        data = '{"id":"%s"}' % id
        response = self.request.request("POST", url, data=data)
        json_response = json.loads(response)
        self.assertEqual(json_response["Result"]["StatusCode"], 6, msg=response)


if __name__ == "__main__":
    unittest.main()
