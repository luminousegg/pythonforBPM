#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017年05月31日

@author: wangzhen
'''
import urllib,urllib2,hashlib,json,request,cookielib,httplib,os,sys
import xlrd
from xlrd import *
from xlrd import cellname,open_workbook,sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")
#from _tkinter import create

class SetUpInfo():

    def __init__(self):
        self.userName = "18210911798"
        self.passWord = "a123456"
        pass




    def test_envi(self):
        domain = "https://www.ceshi112.com"
        assert domain == "https://www.ceshi112.com"


    def userType(self,type="a"):
        if type == 'a':
            return 1
        elif type == "b":
            return 2
        elif type == "c":
            return 3




    def getCookie(self):
        #userLoginInfoSheet = self.excelData.sheet_by_index(2)
        #userName = userLoginInfoSheet.cell(1,0).value
        #passWord = userLoginInfoSheet.cell(1,1).value
        userName = self.userName
        passWord = self.passWord
        try:
            cookieJarInMemory = cookielib.CookieJar();
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarInMemory));
            urllib2.install_opener(opener);

            #获取用户登录后的cookie
            loginUrl = self.TestEnvi()+"/FHH/EM0HXUL/Authorize/PersonalLogin";
            loginData = '{"PhoneNumber":"%s","InternationalAreaCode":"+86","Password":"%s","PersistenceHint":true,"CliendId":"undefined","ImgCode":""}' %(userName,passWord)
            response = urllib2.urlopen(loginUrl,loginData);
            enterpriseUserLoginUrl = self.TestEnvi()+"/FHH/EM0HXUL/Authorize/EnterpriseUserLogin"
            enterpriseUserLoginData = '{"EnterpriseId":"57265"}'
            #获取用户选择企业后的cookie
            response = urllib2.urlopen(enterpriseUserLoginUrl, enterpriseUserLoginData);
            #print cookieJarInMemory
            FSAuthXC_cookie = str(cookieJarInMemory).split("<")[2].split(" ")[1]
            #print FSAuthXC_cookie
            assert "FSAuthXC" in FSAuthXC_cookie
        except Exception:
            #print "get cookie failed!"
            return None

        return FSAuthXC_cookie
        print "FSAuthXC_cookie\n",FSAuthXC_cookie
        print "interface response:", response.read()





if __name__ == "__main__":
    p = SetUpInfo()
    print p.getCookie()