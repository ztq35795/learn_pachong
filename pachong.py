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

URL='http://ftp.lib.hust.edu.cn/search*chx/X?SEARCH='+TRANS_KEY_WORD#set begin web

queue.append(URL)
cnt=1

while queue:
    URL=queue.popleft()#queue head out

    URL_OPEN=urllib.request.urlopen(URL,timeout=1000)#超时跳过+爬下网页源码
    print("正在爬取第",cnt,"页的信息...")
    try:
        data = URL_OPEN.read().decode('UTF-8')#用UTF-8读网页
    except:#不能则跳过
        continue
    linkre =re.compile(r'<span class="briefcitTitle">\n<a href=.*?">(.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?)\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.DOTALL).findall(data)

    for x in linkre:
        print(x)

    try:
        NEST_FETCH=re.compile('<a href="(/search\*chx\?/X.*?/browse)">后一页<',re.DOTALL).search(data)
        NEST_URL="http://ftp.lib.hust.edu.cn"+re.findall('"(.*?)"',NEST_FETCH.group())[0]
        queue.append(NEST_URL)
#        print(NEST_URL)
        cnt+=1
    except:
        print("信息全部爬取完毕")

