#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

class AA: pass
print("hi..")

class A:
	def __getattribute__(self, name):
		print('==in A')
		return super().__getattribute__(name)

class B(A):
	def __init__(self): self.bx=1
	def spam(self):
		print('spam')

b=B()
'to',b.spam,B.spam
'call',b.spam(),B.spam
b.bx
#b.by

##
# environment variable https_proxy=135.251.33.16:8080 not work here? unlike to urlopen()
import http.client
#conn = http.client.HTTPSConnection("www.baidu.com")
conn = http.client.HTTPSConnection("gitlabe2.ext.net.nokia.com")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason, '\n', r1.read())

