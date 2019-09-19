#!/usr/bin/python
#coding:utf8
import unittest
from SetUp import setUpInfo,request
'''
获取待处理任务中和CRM通知中的任务详情
'''
class Test_getDetial(unittest.TestCase):
    def setUp(self):
        self.domain = setUpInfo.SetUpInfo().test_envi()
        self.request = request.Httpcommon

#待处理业务流程
    def test_getUncompletedTask(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessTask/GetUncompletedTasksByObject"
        data = {"apiName":"AccountObj","objectId":"664eb2e3198846ee9561b7b41b679cb2"}
        pass

    def test_getAvailableWorkflows(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessDefinition/GetAvailableWorkflows"
        data = '{"entryType":"AccountObj","objectId":"664eb2e3198846ee9561b7b41b679cb2"}'
        pass

    def test_getTask(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessTask/GetTask"
        data = '{"taskId":"594b34b6319d1927a49ec4bb"}'

#已处理业务流程
    def test_getEntireWorkflowInstance(self):
        url = self.domain+"/FHH/EM1HBPM/ProcessInstance/GetEntireWorkflowInstance"
        data = '{"instanceId":"594a4661688629293bf70ec9"}'

    def test_getTasksByInstanceIds(self):
        url = self.domain+'/FHH/EM1HBPM/ProcessTask/GetTasksByInstanceIds'
        data = '{"workflowInstanceId":"594a4661688629293bf70ec9","activityInstanceIds":[3]}'




