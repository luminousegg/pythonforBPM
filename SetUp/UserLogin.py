#!/usr/bin/python
#coding:utf8
import request
import cookielib,urllib,urllib2,os,httplib

class UserLogin():
    def __init__(self):
        self.request = request.Httpcommon()

    def getEnterpriseList(self):
        url = 'https://www.fxiaoke.com/FHH/EM0HXUL/Authorize/PersonalLogin'
        data = '{"PhoneNumber":"13520133129","InternationalAreaCode":"+86","Password":"glow3182","PersistenceHint":true,"ClientId":"undefined","ImgCode":""}'
        print self.request.request("POST",url,data)

    def saveCookie(self):
        filename = 'cookie.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = urllib.urlencode({
            "PhoneNumber": "13520133129",
            "InternationalAreaCode": "+86",
            "Password": "a123456",
            "PersistenceHint": 'true',
            "CliendId": "undefined",
            "ImgCode": ""

        })
        # 登录教务系统的URL
        loginUrl = 'https://www.sina.com/'
        # 模拟登录，并把cookie保存到变量
        result = opener.open(loginUrl)
        print result.read()
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        # 利用cookie请求访问另一个网址，此网址是成绩查询网址
        gradeUrl = 'https://www.ceshi112.com/FHH/EM1HBPM/ProcessDefinition/GetDefinitionList'
        data = urllib.urlencode(
            {"enabled": 0, "pageSize": 20, "pageNumber": 1}
        )
        # 请求访问成绩查询网址
        result = opener.open(gradeUrl,data)
        print result.read()


    def pythonAutoHandleCookie(self):
        """
            Demo how to auto handle cookie in Python
                cookies in memory
                cookies in file:
                    save cookie to file
                        LWP     format
                        Mozilla format
                    load cookie from file
        """

        print "1. Demo how to auto handle cookie (in memory)";
        cookieJarInMemory = cookielib.CookieJar();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarInMemory));
        urllib2.install_opener(opener);
        print "after init, cookieJarInMemory=", cookieJarInMemory;  # after init, cookieJarInMemory= <cookielib.CookieJar[]>
        # !!! following urllib2 will auto handle cookies

        #demoUrl = "http://www.baidu.com/";
        demoUrl = "https://www.ceshi112.com/FHH/EM0HXUL/Authorize/PersonalLogin";
        postdata = '{"PhoneNumber":"13520133129","InternationalAreaCode":"+86","Password":"a123456","PersistenceHint":true,"CliendId":"undefined","ImgCode":""}'


        response = urllib2.urlopen(demoUrl,postdata);
        # here, we already got response cookies

        print "after urllib2.urlopen, cookieJarInMemory=", cookieJarInMemory;
        print response.read
        # after urllib2.urlopen, cookieJarInMemory= <cookielib.CookieJar[<Cookie PREF=ID=1e5d4d8621e61210:FF=0:NW=1:TM=1358235182:LM=1358235182:S=B-ONJ1lsQj5ARTEO for .google.com/>, <Cookie NID=67=lIY7YlPSrtQy4pHX_u8SrMAoG8-LXp8blElxXXfahe2ES3TVHzpaT3aejzaltwXetiE7TO7HrVwQCCe69tTh5K7Y5WyP8bvSZF20Myn1dcG7C780DNEeiT_QB0NeB4cR for .google.com.hk/>, <Cookie PREF=ID=4501e3b1f4a952b6:U=535aadd0e6b1070b:FF=2:LD=zh-CN:NW=1:TM=1358235182:LM=1358235182:S=Az7ZVYebAECtSKXd for .google.com.hk/>]>
        print "%"*100
        demoUrl2 = "https://www.ceshi112.com/FHH/EM0HXUL/Authorize/EnterpriseUserLogin"
        postdata2 = '{"EnterpriseId":"54931"}'

        response = urllib2.urlopen(demoUrl2, postdata2);
        # here, we already got response cookies

        print "after urllib2.urlopen, cookieJarInMemory=", cookieJarInMemory;
        print response.read

        print "2. Demo how to auto handle cookie in file, LWP format";
        cookieFilenameLWP = "localCookiesLWP.txt";
        cookieJarFileLWP = cookielib.LWPCookieJar(cookieFilenameLWP);
        # will create (and save to) new cookie file
        cookieJarFileLWP.save();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarFileLWP));
        urllib2.install_opener(opener);
        # !!! following urllib2 will auto handle cookies
        demoUrl = "http://www.baidu.com/";
        response = urllib2.urlopen(demoUrl);
        # update cookies, save cookies into file
        cookieJarFileLWP.save();
        # for demo, print cookies in file
        print "LWP cookies:";
        print open(cookieFilenameLWP).read(os.path.getsize(cookieFilenameLWP));
        # #LWP-Cookies-2.0
        # Set-Cookie3: PREF="ID=34c1415b570a93ae:FF=0:NW=1:TM=1358236121:LM=1358236121:S=gEVVojW4x37ht5n-"; path="/"; domain=".google.com"; path_spec; domain_dot; expires="2015-01-15 07:48:41Z"; version=0
        # Set-Cookie3: NID="67=JI_uEwUm5GDrQ_vCwAp2z_YGU7MdLm5CLMa4CNLF7RQuTDMzrrk1EjRddGcnpoFbht81LaV9spxZQQInf0mPS6lDrvcRqBBL5NOTmy8SwOzA6HWC3iTIo4-o3fO1Udkv"; path="/"; domain=".google.com.hk"; path_spec; domain_dot; expires="2013-07-17 07:48:41Z"; HttpOnly=None; version=0
        # Set-Cookie3: PREF="ID=8f7e4efca89bdb1b:U=f85a4afa4db021aa:FF=2:LD=zh-CN:NW=1:TM=1358236121:LM=1358236121:S=2WR59hDWutdnUJtF"; path="/"; domain=".google.com.hk"; path_spec; domain_dot; expires="2015-01-15 07:48:41Z"; version=0

        print "3. Demo how to auto handle cookie in file, Mozilla Format";
        cookieFilenameMozilla = "localCookiesMozilla.txt";
        cookieJarFileMozilla = cookielib.MozillaCookieJar(cookieFilenameMozilla);
        # will create (and save to) new cookie file
        cookieJarFileMozilla.save();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarFileMozilla));
        urllib2.install_opener(opener);
        # !!! following urllib2 will auto handle cookies
        demoUrl = "http://www.baidu.com/";
        response = urllib2.urlopen(demoUrl);
        # update cookies, save cookies into file
        cookieJarFileMozilla.save();
        # for demo, print cookies in file
        print "Mozilla cookies:";
        print open(cookieFilenameMozilla).read(os.path.getsize(cookieFilenameMozilla));
        # # Netscape HTTP Cookie File
        # # http://www.netscape.com/newsref/std/cookie_spec.html
        # # This is a generated file!  Do not edit.

        # .google.com   TRUE    /   FALSE   1421308121  PREF    ID=0e05040dd979207c:FF=0:NW=1:TM=1358236121:LM=1358236121:S=jcFid2XgXMIhPUPl
        # .google.com.hk    TRUE    /   FALSE   1374047321  NID 67=klMI_Z5ZPWDjUYrWSUHIE_kYI77_ziJaL0kWRoUGThagME86LKY7H-MNa2wAMI_GklIwYcD8t82qPinxzLd4GLDbmWT0OVLCXhRj0wQDC57dTNAsTs4lhVR7Yjvj2tfn
        # .google.com.hk    TRUE    /   FALSE   1421308121  PREF    ID=028f8b736db06a9a:U=6ba6d080847c8de6:FF=2:LD=zh-CN:NW=1:TM=1358236121:LM=1358236121:S=_1BcC5v3G0ZojVz8

        print "4. read cookies from file";
        parseAndSavedCookieFile = "parsedAndSavedCookies.txt"
        parsedCookieJarFile = cookielib.MozillaCookieJar(parseAndSavedCookieFile);
        # parsedCookieJarFile = cookielib.MozillaCookieJar(cookieFilenameMozilla);
        print parsedCookieJarFile;  # <_MozillaCookieJar.MozillaCookieJar[]>
        parsedCookieJarFile.load(cookieFilenameMozilla);
        print parsedCookieJarFile;  # <_MozillaCookieJar.MozillaCookieJar[<Cookie PREF=ID=5add236cafeb990c:FF=0:NW=1:TM=1358236707:LM=1358236707:S=9lhhp0W0zTCj8FVn for .google.com/>, <Cookie NID=67=Kx0fU67poTRN-ECBA_2zqr9KIUSP5a6DcGUefbD5R0ILsRAYSa109mAYIEF69LS40-UPrECtu756mH2nlz8mVneCVzANWfY7eFkmvQkeFVPGh9D58QYAeiFrUMed_OZB for .google.com.hk/>, <Cookie PREF=ID=442b8f2173d4249e:U=d01eca1334179f67:FF=2:LD=zh-CN:NW=1:TM=1358236707:LM=1358236707:S=_WQ1abARwIb5Crdj for .google.com.hk/>]>

    def postRequest(self):
        httpClient = None
        try:
            params = urllib.urlencode({"PhoneNumber":"13520133129","InternationalAreaCode":"+86","Password":"a123456","PersistenceHint":True,"CliendId":"undefined","ImgCode":""})
            headers = {"Content-type": "application/x-www-form-urlencoded"
                , "Accept": "text/plain"}
            demoUrl = "https://www.fxiaoke.com/FHH/EM0HXUL/Authorize/PersonalLogin";
            print 1
            httpClient = httplib.HTTPConnection("https://www.ceshi112.com/FHH/EM0HXUL/Authorize/PersonalLogin","")
            a = httpClient.request("POST", params, headers)
            print a
            response = httpClient.getresponse()


            print response
            print response.status
            print response.reason
            print response.read()
            print response.getheaders()  # 获取头信息
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()



if __name__ =="__main__":
    p = UserLogin()
    print p.getEnterpriseList()
