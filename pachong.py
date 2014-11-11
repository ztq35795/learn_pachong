#!/usr/bin/python
import re
import urllib.request
import urllib
import urllib.parse
from collections import deque

print("请输入关键词")
KEY_WORD=input()
TRANS_KEY_WORD=urllib.parse.quote(KEY_WORD)


queue=deque()#用了专门存放URL的类
visited=set()#set结构：无序无重复元素

url='http://ftp.lib.hust.edu.cn/search*chx/X?SEARCH='+TRANS_KEY_WORD#set begin web

queue.append(url)
cnt=0

while queue:
    url=queue.popleft()#queue head out

    urlop=urllib.request.urlopen(url,timeout=1000)#超时跳过+爬下网页源码
    try:
        data = urlop.read().decode('UTF-8')#用UTF-8读网页
    except:#不能则跳过
        continue

#    linkre =re.compile(r'<span class="briefcitTitle">\n<a href=.*?">(.*?) / (.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?)\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.DOTALL).findall(data)
#    print(linkre)

    NEST_URL=re.compile(r'<a href="(.*)+?">后一页',re.DOTALL).findall(data)
    print(NEST_URL)
