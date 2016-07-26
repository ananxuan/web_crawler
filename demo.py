import urllib2,urllib

#version1 create request
response = urllib2.urlopen("http://www.baidu.com")#urlopen(url,data,timeout)
print(response.read())

#version2
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print(response.read())

#post and get data transfer
#version post
values = {"username":"1016903103@qq.com","password":"XXXX"}#define a dictionary,argv are username and password
data = urllib.urlencode(values)#encode with urlencode
url = "https://passport.csdn.net/account.login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Ruquest(url, data)#give the argv to request
response = urllib2.urlopen(request)#execute it you can login,create a server to test it 
print(response.read())

#version get
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" +data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print(response.read())

#set header
url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0(compatibal; MSTE 5.5;Windows NT)'#some server will identify if it is webbrowser request by proxy
values = {'username':'cqc','password':'XXXX'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)#identify if it is a request from webrowser
response = urllib2.urlopen(request)
page = response.read()

#set proxy 
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8000'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
  opener = urllib2.build_opener(proxy_handler)
else:
  opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#set timeout
reponse = urllib2.urlopen('http://www.baidu.com',timeout=10)
response = urllib2.urlopen('http://www.baidu.com',data, 10)

#use put and delete method of http
request = urllib2.Request(url,data = data)
request.get_method = lambda: 'PUT' #or 'DELETE'
response = urllib2.urlopen(request)

#handle the exception
request = urllib2.Request('http://www.xxxxx.com')
try:
  urllib2.urlopen(request)
except urllib2.URLError, e:
  print(e.reason)
