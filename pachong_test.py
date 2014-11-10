#!/usr/bin/python
import re
import urllib.request
import urllib
import http.cookiejar
#head: dict of header
def makeMyOpener(head = {
    'Connection':'Keep-Alive',
    'Accept':'test/html,application/xhtml+xml,*/*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3'
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko' }):

    cj=http.cookiejar.Cookiejar()
    opener=urllib.request.build_opener(urllib,request.HTTPCookieProsessor(cj))
    header=[]
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders=header
    return opener

from collections import deque

queue=deque()
visited=set()   #set结构：无序无重复元素

url='http://news.dbanote.net' #set begin web

queue.append(url)
cnt=0

while queue:
    url=queue.popleft() #queue head out
    visited |={url}

    print('already fetch '+str(cnt)+' fetching on<---'+url)
    cnt+=1
    urlop=urllib.request.urlopen(url,timeout=2)#超时跳过+爬网页
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    try:
        data = urlop.read().decode('UTF-8')
    except:
        continue
    linkre =re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('adding to the queue --->' + x)

    if 'html' not in urlop.getheader('Content-Type'):
        continue
