# -*- coding:utf-8 -*-


import urllib2
import hashlib
import time
import urllib
import json
import cookielib
import setUpInfo
#from SetUpInfo import SetUpInfo


class Httpcommon():


    def __init__(self):
        self.cookie = setUpInfo.SetUpInfo().getCookie()


    def request(self, method, url, data):
        try:
            rq = urllib2.Request(url)
            #rq.add_header("Token", self.token)
            #rq.add_header("Device-Searal", "59")
            #rq.add_header("Device-Name", ':7-433d06bb')
            rq.add_header("accept", 'application/json')
            rq.add_header("Cookie",self.cookie)
            rq.add_header("Content-Type", "application/json;charset=utf-8")
            rq.get_method = lambda: method
            content = urllib2.urlopen(rq, data).read()
            return content
        except Exception, e:
            return e.read()



    def request_delete(self, url, data):
        rq = urllib2.Request(url, data=data)
        #        rq.add_header("Token",self.token)
        rq.add_header("Cookie", self.Cookie)
        rq.add_header("Accept", "application/javascript, application/json")
        rq.add_header("Accept-Encoding", "gzip,deflate,sdch")
        rq.add_header("Accept-Language", "zh-CN,zh;q=0.8")
        rq.add_header("Connection", "keep-alive")
        rq.add_header("Content-Length", "2")
        rq.add_header("Content-Type", "application/json;charset=utf-8")
        rq.get_method = lambda: 'DELETE'  # or 'DELETE or PUT or ...
        responseinfo = urllib2.urlopen(rq).read()
        return responseinfo

    def request_put(self, url, data):
        rq = urllib2.Request(url, data=data)
        rq.add_header("Cookie", self.Cookie)
        rq.add_header("Accept", "application/javascript, application/json")
        rq.add_header('Accept-Encoding', 'gzip,deflate,sdch')
        rq.add_header("Content-Type", "application/json;charset=utf-8")
        rq.get_method = lambda: 'put'  # or 'DELETE or PUT or ...
        responseinfo = urllib2.urlopen(rq.data).read()
        #        responseinfo = urllib2.urlopen(rq).read()
        return responseinfo

    def post(self, url, data):  # http post+referer请求方式
        import urllib
        rq = urllib2.Request(url)
        # rq.add_header("Token","2a8a2e33-b775-456e-a050-0ef8d6c420a9")
        # rq.add_header("Device-Searal","7")
        # rq.add_header("Device-Name","7-433d06bb");
        # rq.add_header("Device-Type","Android")
        # rq.add_header('cookie',self.Cookie)
        # rq.add_header("Content-Type","application/json")
        content = urllib2.urlopen(rq, data=urllib.urlencode(data)).read()
        return content

    def get(self, url):
        start_time = time.time()
        rq = urllib2.Request(url)
        rq.add_header("Token", "da350393-157b-4abd-ab8f-04fe538d24be")
        rq.add_header("Device-Searal", "7")
        rq.add_header("Device-Name", "7-433d06bb");
        rq.add_header("Device-Type", "Android")
        rq.add_header("Content-Type", "application/json")
        content = urllib2.urlopen(rq)
        cont = content.read()
        return cont
        timer = time.time() - start_time
        return timer

    def get_data(self, url, param):
        rq = urllib2.Request(url)
        rq.add_header('cookie', self.Cookie)
        content = urllib2.urlopen(rq, data=param)
        cont = content.read()
        return cont

    def put(self, url, param):
        rq = urllib2.Request(url, data=param)
        rq.add_header("Cookie", self.Cookie)
        rq.add_header("Device-Searal", "7")
        rq.add_header("Device-Name", "7-433d06bb");
        rq.add_header("Device-Type", "Android")
        rq.add_header("Content-Type", "application/json")
        rq.get_method = lambda: 'PUT'
        content = urllib2.urlopen(rq)
        http_recode = content.code
        cont = content.read()
        return cont, http_recode

    def multipart(self, url, files):
        try:
            register_openers()
            datagen, headers = multipart_encode({"Filedata": open(files, "rb")})

            rq = urllib2.Request(url, datagen, headers)
            rq.add_header("Token", self.token)
            rq.add_header("Device-Searal", "121212")
            rq.add_header("Device-Name", "11212")
            rq.add_header("Device-Type", "Android")
            rq.add_header("Content-Type", "multipart/form-data")
            rq.add_header("Content-Transfer-Encoding", "binary")
            rq.add_header("Content-Type", "application/octet-stream")
            requestInfo = urllib2.urlopen(rq)
            print  requestInfo.read()
        except Exception, e:
            print e.read()

    def chanjet_request_urlencode(self, method, url, data):

        try:
            rq = urllib2.Request(url)
            # rq.add_header("Token",self.token)
            # rq.add_header("Device-Searal", "121212")
            # rq.add_header("Device-Name", "11212")
            # rq.add_header("Device-Type", "Android")
            rq.add_header("Content-Type", "application/x-www-form-urlencoded")
            rq.get_method = lambda: method
            content = urllib2.urlopen(rq, data=urllib.urlencode(data)).read()
            return content
        except Exception, e:
            return e.read()

    def chanjet_request(self, method, url, data):
        try:
            rq = urllib2.Request(url)
            # rq.add_header("Token",self.token)
            # rq.add_header("Device-Searal", "121212")
            # rq.add_header("Device-Name", "11212")
            # rq.add_header("Device-Type", "Android")
            rq.add_header("Content-Type", "application/x-www-form-urlencoded")
            rq.get_method = lambda: method
            content = urllib2.urlopen(rq, data).read()
            return content
        except Exception, e:
            return e.read()



    def logincia(self, var="access_token"):
        url = "http://cia.csp.chanapp.com/internal_api/client_authentication_with_userInfo"
        param = 'client_id=accounting&client_secret=uoi6dd&auth_username=%s&password=%s' % (
        self.username, self.password)
        rq = urllib2.Request(url)
        # content = urllib2.urlopen(rq, data=param).read().split(',')[0].split(':')[1].replace('"','')
        content = urllib2.urlopen(rq, data=param).read()
        if "access_token" not in json.loads(content).keys():
            print "用户名密码错误"
        else:
            return json.loads(content)[var]


if __name__ == "__main__":
    test = Httpcommon()
