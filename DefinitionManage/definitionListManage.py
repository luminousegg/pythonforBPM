#!/usr/bin/python
#coding:utf8
from SetUp import request
from SetUp import setUpInfo
import json

'''
测试说明
1、在业务流程中随机找一条业务流程，启用状态改为停用，停用改为启用
2、调用场景筛选接口，已停用、已启用中包含步骤一中停用和启用的流程。全部场景中包含停用和启用状态的流程
3、删除流程（未停用的给出提示信息，已停用的可成功删除）
'''
class DefinitionListManage():
    def __init__(self):
        self.request = request.Httpcommon()
        self.domain = setUpInfo.SetUpInfo().TestEnvi()

#返回流程管理中的流程信息，返回数组形式，格式{name:[],id:[],status:[]}
    def getDefinitionListAll(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList"
        data = '{enabled: 0, pageSize: 20, pageNumber: 1}'
        result = self.request.request("POST",url,data=data)
        result_dict= json.loads(result)
        definitionDict={"name":[],"id":[],"enabled":[]}
        #print   result
        #标记是否可以获取到对应状态的流程id
        for i in range(len(result_dict["Value"]["outlines"])):
            definitionDict["name"].append(result_dict["Value"]["outlines"][i]["name"])
            definitionDict["id"].append(result_dict["Value"]["outlines"][i]["id"])
            definitionDict["enabled"].append(result_dict["Value"]["outlines"][i]["enabled"])

        return definitionDict



#公共方法，根据id查询流程状态并返回,enable 1 启用 2 停用 0 全部
    def getDefinitionStatus(self,id=None,enable=0):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList"
        data = '{enabled: %s, pageSize: 20, pageNumber: 1}' % enable
        result = json.loads(self.request.request("POST", url, data=data))
        definitionDic = {"id":"","name":"","enabled":""}
        #判断查询结果是否为空
        nu = len(result["Value"]["outlines"])
        if nu == 0:
            return None
        #返回按id查询流程的状态
        for i in range(nu):
            if result["Value"]["outlines"][i]["id"] == id:
                definitionDic["enabled"]= result["Value"]["outlines"][i]["enabled"]
                return definitionDic
        #返回第一个停用或启用的流程信息
        definitionDic["enabled"] = result["Value"]["outlines"][0]["enabled"]
        definitionDic["id"] = result["Value"]["outlines"][0]["id"]
        definitionDic["name"] = result["Value"]["outlines"][0]["name"]
        return definitionDic


#停用一个启用中的流程
    def disableDefinition(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessDefinition/UpdateDefinitionStatus"
        id = str(self.getDefinitionStatus(enable=1)["id"])
        name = str(self.getDefinitionStatus(enable=1)["name"])
        if id == "None":
            return "无启用状态的流程"
        data = '{"ids":"%s","enabled":false}' % id
        result= self.request.request("POST",url,data=data)
        definitionStatus = self.getDefinitionStatus(id=id,enable=2)
        if definitionStatus["enabled"] is False:
            print "流程名称:",name, "停用成功"
        else:
            print "流程名称:",name,"停用失败，接口返回",result

#启用一个停止中的流程
    def enableDefinition(self,id = None):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/UpdateDefinitionStatus"
        id = str(self.getDefinitionStatus(enable=2)["id"])
        name = str(self.getDefinitionStatus(enable=2)["name"])
        if id == "None":
            return "无停用状态的流程"
        data = '{"ids":"%s","enabled":true}' % id
        result = self.request.request("POST", url, data=data)
        definitionStatus = self.getDefinitionStatus(id=id, enable=1)
        if definitionStatus["enabled"] is True:
            print "流程名称:", name, "启用成功"
        else:
            print "流程名称:", name, "启用失败，接口返回", result

#删除一个停用的流程
    def delDisenableDefinition(self):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/DeleteDefinition"
        id = str(self.getDefinitionStatus(enable=2)["id"])
        if id == "None":
            return "无停用状态的路程"
        data = '{"id":"%s"}' % str(id)
        result = self.request.request("POST", url, data=data)
        if self.getDefinitionStatus(id, enable=1) is None:
            print "删除成功"
        else:
            print "删除失败，接口返回", result


#删除一个启用状态的流程（不可删除，给出提示信息）
    def delEnableDefinition(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessDefinition/DeleteDefinition"
        id = str(self.getDefinitionStatus(enable=1)["id"])
        if id == "None":
            return "无启用状态的流程"
        data = '{"id":"%s"}' % id
        result= json.loads(self.request.request("POST",url,data=data))
        if result["Result"]["FailureMessage"]=="删除失败,请确认该流程是否已经停用":
            print "执行成功"
        else:
            print "执行失败，接口返回",result


#获取已经存在的流程名称作为关键字搜索
    def definitionKeywordSearch(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList"
        keyword = str(self.getDefinitionStatus(enable=0)["name"])
        data = '{"enabled":0,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"keyWord":"%s"}' % keyword
        result = self.request.request("POST",url,data=data)
        if len(json.loads(result)["Value"]['outlines']) == 1:
            print "搜索成功，关键字：",keyword
        else:
            print "搜索失败,接口返回：",result


#搜索关键字不存在的流程
    def definitionKeywordSearchNone(self):
        url = self.domain + "/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList"
        data = '{"enabled":0,"pageSize":20,"pageNumber":1,"QueryInfo":{"Conditions":[]},"keyWord":"!@#$%"}'
        result = self.request.request("POST", url, data=data)
        if len(json.loads(result)["Value"]['outlines']) == 0:
            print "搜索成功，关键字：!@#$%"
        else:
            print "搜索失败,接口返回：", result


if __name__=="__main__":
    p = DefinitionListManage()
    print p.getDefinitionListAll()
    #print p.disableDefinition()
