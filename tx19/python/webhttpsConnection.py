#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

class AA: pass
print("hi..")

##
# environment variable https_proxy=135.251.33.16:8080 not work here? unlike to urlopen()
import http.client
#conn = http.client.HTTPSConnection("www.baidu.com")
conn = http.client.HTTPSConnection("gitlabe2.ext.net.nokia.com")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason, r'\n', r1.read())

