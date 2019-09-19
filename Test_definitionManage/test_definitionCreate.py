#!/usr/bin/python
#coding:utf8



from SetUp import setUpInfo,request
from publicMethod import PublicMethod
#from test_definitionManage import TestCase_definitionManger
#from test_definitionDel import TestCase_definitionDel
import json,unittest,os,sys
sys.path.append("..")

class Test_DefinitionCreate(unittest.TestCase):

    def setUp(self):
        self.domain = setUpInfo.SetUpInfo().TestEnvi()
        self.request = request.Httpcommon()
        self.publicMethod= PublicMethod()
        #self.definitionDel = test_definitionDel.TestCase_definitionDel()

# TestCase 1，获取流程列表接口，返回流程管理中的流程信息，返回数组形式，格式{name:[],id:[],status:[]}
    def test_getDefinitionListAll(self):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList"
        data = '{enabled: 0, pageSize: 20, pageNumber: 1}'
        definitionDict = {"name": [], "id": [], "enabled": []}
        response = self.request.request("POST", url, data=data)
        json_response = json.loads(response)
        self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)

        try:
            for i in range(len(json_response["Value"]["outlines"])):
                definitionDict["name"].append(json_response["Value"]["outlines"][i]["name"])
                definitionDict["id"].append(json_response["Value"]["outlines"][i]["id"])
                definitionDict["enabled"].append(json_response["Value"]["outlines"][i]["enabled"])
            return definitionDict
        except Exception, e:

            return e


#在流程列表中查询流程是否存在，如果存在，停用并删除此流程。如果不存在，新建业务流程,返回流程数组[id:"",instanceName:""]
    def test_createDefinition(self):
        getDefinitionListAll = self.publicMethod.getDefinitionListAll()
        url = self.domain+"/FHH/EM1HBPM/ProcessDefinition/CreateDefinition"
        definitionName = self.publicMethod.creatDefinitionInfo()["name"]
        data = self.publicMethod.creatDefinitionInfo()["parameter"]
        #判断路程是否存在，如果存在，停用并删除
        if definitionName in self.publicMethod.getDefinitionListAll()["name"]:
            definitionId = self.publicMethod.getDefinitionId(name=definitionName)
            #停用页流程
            self.publicMethod.disableDefinition(id=definitionId)
            #删除业务流程
            self.publicMethod.delDisenableDefinition(id=definitionId)

        response =  self.request.request("POST",url,data=data)
        print response
        json_response=json.loads(response)
        #判断新建流程接口返回的statusCode
        self.assertEqual(json_response["Result"]["StatusCode"], 0, msg=response)
        #新建完成后，请求getDefinition接口，查询新建的流程是否存在
        self.assertTrue(definitionName in getDefinitionListAll["name"],msg=None)


if __name__=="__main__":

    unittest.main()