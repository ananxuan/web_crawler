# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
#百度贴吧爬虫类
class BDTB:
  #初始化，传入基地址，是否只看楼主参数
  #URLADDR:http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1
  def __init__(self,baseURL, seeLZ):
    self.baseURL=baseURL
    self.seeLZ= '?see_lz=' +str(seeLZ)
    
    #传入页码，获取该页帖子的代码
    def getpage(self,pageNum):
      try:
        url = self.baseURL +self.seeLZ + '&pn=' + str(pageNum)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        print response.read()
        return response
      except urllib2.URLError, e:
        if hasattr(e, "reason"):
          print u"failed,reson",e.reason
          return None
          
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getpage(1)
#提取相关信息
#帖子标题
#htmldata:<h1 class="core_title_txt  " title="纯原创我心中的NBA2014-2015赛季现役50大" style="width: 396px">
#纯原创我心中的NBA2014-2015赛季现役50大</h1>
#get title
def getTitle(self):
  page= self.getPage(1)
  pattern = re.compile('<h1 class="core_title_text.*?>(.*?)</h1>',re.S)
  result = re.search(pattern, page)
  if result:
    return result.group(1).strip()
  else:
    return None
    
#帖子页数
def getPageNum(self):
  page = self.getPage(1)
  pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
  result=re.search(pattern,page)
  if result:
  return result.group(1).strip()
  else:
    return None
#获取正文data
def getContent(self,page):
  pattern = re.compile('<div id = "post_content_.*?>(.*?)</div>',re.S)
  items = re.findall(pattern, page)
  for item in items:
    print item
    
#处理页面
class Tool:
  removeImg = re.compile('<img.*?>| {7}|')#去除img标签，7位长空格
  removeAddr = re.compile('<a.*?>|</a>')#去除超链接标签
  removeLine = re.compile('tr>|<div>|</div>|</p>')#去除超链接标签
  repalceTD = re.compile('<td>')#将表格制表td替换为\t
  replacePara = re.compile('<p.*?>')#段落开头换位\n将空两格
  repalceBR = re.compile('<br><br>|<br>')#将换行符替换为\n
  removeExtraTag = re.compile('<.*?>')#删除其余标签
  def replace(self,x):
    x = re.sub(self.removeImg, "",x)
    x = re.sub(self.removeAddr, "",x)
    x = re.sub(self.removeLine, "",x)
    x = re.sub(self.removeTD, "",x)
    x = re.sub(self.removePara, "",x)
    x = re.sub(self.removeBR, "",x)
    x = re.sub(self.removeExtraTag, "",x)
    return x.strip() #去除多余内容
  
