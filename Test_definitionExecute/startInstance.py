#!/usr/bin/python
#coding:utf8
from SetUp import request,setUpInfo
import json,sys
sys.path.append("..")
from DefinitionManage import definitionCreate
reload(sys)
sys.setdefaultencoding('utf-8')
class StartInstance():
    def __init__(self):
        self.request = request.Httpcommon()
        self.domain = setUpInfo.SetUpInfo().TestEnvi()
#        self.definitionId = definitionCreate.DefinitionCreate()
#查询客户是否存在
    def searchCustomer(self,customerName=None):
        # 获取我负责的FilterMainId
        url_GetUserTable = self.domain + "/FHH/EM1HEBL/UserTable/GetUserTable"
        data_GetUserTable = '{"TableName":"customer","IsLoadManagement":true}'
        result_GetUserTable = self.request.request("POST", url_GetUserTable, data=data_GetUserTable)
        fiterMainId = json.loads(result_GetUserTable)["Value"]["FilterMains"][0]["FilterMainID"]
        # 获取我负责的客户下所有客户信息
        url_GetCustomerList = self.domain + '/FHH/EM1HCRM/Customer/GetCustomerList'
        data_GetCustomerList = '{"QueryInfo":{"FilterMainID":"%s"},"pageSize":20,"pageNumber":1}' % fiterMainId
        #print "data_GetCustomerList",data_GetCustomerList
        result_GetCustomerList = self.request.request("POST", url_GetCustomerList, data=data_GetCustomerList)
        result_GetCustomerList_dict = json.loads(result_GetCustomerList)
        #print result_GetCustomerList
        #print "23",len(result_GetCustomerList_dict["Value"]["CustomerList"])
        for i in range(len(result_GetCustomerList_dict["Value"]["CustomerList"])):

            if str(customerName) == str(result_GetCustomerList_dict["Value"]["CustomerList"][i]["Name"]):

                return result_GetCustomerList_dict["Value"]["CustomerList"][i]["CustomerID"]
            else:
                return None



#查询自动化使用的客户是否存在，如果没有，新建一个客户，发起用于发起流程
    def addCustomer(self):

        data_addCustomer = json.loads(open('addCustomer.json').read())
        for i in range(len(data_addCustomer["UDFieldDatas"])):
            if data_addCustomer["UDFieldDatas"][i]["FieldName"] == "Name":
                name = data_addCustomer["UDFieldDatas"][i]["FieldValue"]["Value"]
                break
        id = self.searchCustomer(customerName=name)

        if id == None:

            url_addCustomer = self.domain+"/FHH/EM1HCRM/Customer/AddCustomer"
            data_addCustomer = str(open('addCustomer.json').read())
            #print "url",url_addCustomer
            result_addCustomer = self.request.request("POST",url_addCustomer,data= data_addCustomer)
            print result_addCustomer
            return json.loads(result_addCustomer)["Value"]["CustomerID"]

        else:
            return id




#发起流程（所用参数。对象ID和流程ID）,发起成功后返回instanceID
    def startInstance(self):
        url_startInstance = self.domain+"/FHH/EM1HBPM/ProcessInstance/StartInstance"
        definitionData =definitionCreate.DefinitionCreate().createDefinition()
        definitionId = definitionData["id"]
        objectId= self.addCustomer()
        instanceName = definitionData["instanceName"]

        print "definitionId",definitionId,"objectId",objectId,"instanceName",instanceName
        print self.getUncompletedTasksByObject(objectId=objectId,instanceName=instanceName)
        #先判断一下此流程是否是发起状态,是 终止，否 发起
        if self.getUncompletedTasksByObject(objectId=objectId,instanceName=instanceName) is True:
            print "checkstatus",self.cancelInstance(definitionId=definitionId)


        data_startInstance = '{"id":"%s","objectId":"%s"}' %(definitionId,objectId)
        result = self.request.request("POST",url_startInstance,data=data_startInstance)
        print result
        if self.getUncompletedTasksByObject(objectId=objectId, instanceName=instanceName) is True:
            print "流程发起成功"

            result_dict = json.loads(result)
            print result_dict["Value"]["result"]
            #返回instanceID
            return result_dict["Value"]["result"]

#获取对象下未完成的任务并返回搜搜流程ID
    def getUncompletedTasksByObject(self,objectId=None,instanceName= None):
        apiName = "AccountObj"
        if objectId == None:
            return None
        url_getUncompletedTaskByObject= self.domain+'/FHH/EM1HBPM/ProcessTask/GetUncompletedTasksByObject'
        data_getUncompetedTaskByObject='{"apiName":"AccountObj","objectId":"%s"}' %objectId
        uncompletedInstanceNameList = []
        result =json.loads(self.request.request("POST",url_getUncompletedTaskByObject,data=data_getUncompetedTaskByObject))
        for i in range(len(result["Value"]["taskOutlines"])):
            uncompletedInstanceNameList.append(result["Value"]["taskOutlines"][i]["processName"])
        if instanceName in uncompletedInstanceNameList:
            return True
        else:
            return False



#终止一个进行中的流程
    def cancelInstance(self,definitionId=None):
        url = self.domain+"/FHH/EM1HBPM/ProcessInstance/CancelInstance"

        data = '{"id":"%s"}' % definitionId
        response = self.request.request("POST",url,data=data)
        print response
        response_dict = json.loads(response)
        if response_dict["Result"]["StatusCode"] == 0:
            return True
        else:
            return False





if __name__ == "__main__":
    p = StartInstance()
    print p.cancelInstance(definitionId="257840427435687936")