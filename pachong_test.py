#!/usr/bin/python
import re
import urllib.request
import urllib

from collections import deque

queue=deque()
visited=set()

url='http://news.dbanote.net' #set begin web

queue.append(url)
cnt=0

while queue:
    url=queue.popleft() #queue head out
    visited |={url}

    print('already fetch '+str(cnt)+' fetching on<---'+url)
    cnt+=1
    urlop=urllib.request.urlopen(url)
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
