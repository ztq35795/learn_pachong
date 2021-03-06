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
    visited |={url}

    print('already fetch '+str(cnt)+' fetching on<---'+url)
    cnt+=1
    urlop=urllib.request.urlopen(url,timeout=1000)#超时跳过+爬下网页源码
    if 'html' not in urlop.getheader('Content-Type'):#判断打开的是不是网页，也可能是图片什么的
        continue

    try:
        data = urlop.read().decode('UTF-8')#用UTF-8读网页
    except:#不能则跳过
        continue
    linkre =re.compile('href=\"(.+?)\"')#创建一个正则表达式对象
    for x in linkre.findall(data):#从爬的网页读所有符合的网址
        if 'http' in x and x not in visited:
            queue.append(x)
            print('adding to the queue --->' + x)

    if 'html' not in urlop.getheader('Content-Type'):
        continue
