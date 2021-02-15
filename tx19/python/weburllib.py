#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

class AA: pass
print("hi..")

#
#https_response
#Python » 3.5.2 Documentation » Python HOWTOs » HOWTO Fetch Internet Resources Using The urllib Package
#Python » 3.5.2 Documentation » The Python Standard Library » 21. Internet Protocols and Support » 21.5. urllib — URL handling modules
#Python » 3.5.2 Documentation » The Python Standard Library » 21. Internet Protocols and Support » 21.11. http — HTTP modules
#Python » 3.5.2 Documentation » The Python Standard Library » 19. Internet Data Handling » 19.2. json — JSON encoder and decoder
#ProxyHandler处理器（代理设置） https://blog.csdn.net/weixin_42152274/article/details/88526545
# Python网络爬虫之ProxyHandler处理器（IP代理设置）https://blog.csdn.net/z564359805/article/details/88691875
#python3下urllib.request库高级应用之ProxyHandler处理器_代理设置  https://www.cnblogs.com/tinghai8/p/9051513.html
#Request.set_proxy()
#关于python requests包新版本设置代理的问题  https://www.cnblogs.com/piperck/p/5045487.html
#
#
#https_proxy=135.251.33.16:8080  pyy -c "import urllib.request as r; f=r.urlopen('https://github.com'); print(f.getcode(),f.geturl())"
#https_proxy=135.251.33.16:8080  pyy -i weburllib.py  #for http://www.baidu.com
import urllib.request
import os
#req = urllib.request.Request(url='http://www.baidu.com')
req = urllib.request.Request(url='https://www.baidu.com');
#req.set_proxy("135.251.33.16:8080","https") # error,why?
#print(os.environ['https_proxy'], os.environ)
print(os.getenv('https_proxy'), os.environ)
#
#os.putenv('https_proxy', '135.251.33.16:8080')  # affect subprocesses only
if (not os.getenv('https_proxy')): os.environ['https_proxy'] = '135.251.33.16:8080' # change environ varable here, or in shell command
print(os.getenv('https_proxy'))
with urllib.request.urlopen(req) as f: print(f.getcode(),f.geturl(),f.info(),f.read(666).decode('utf-8'))
#import urllib,ssl


#with urllib.request.urlopen('http://www.baidu.com') as response: html = response.read(399); print(html.decode('utf-8'))
#with urllib.request.urlopen('http://www.sina.com.cn') as rf: print('\n',rf.getcode(),rf.geturl(),'\n',rf.info());html = rf.read(99); print(html)


