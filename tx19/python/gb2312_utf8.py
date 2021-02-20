#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

def lg():import inspect;return '--'+str(inspect.stack()[1][1:4])
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

###
'''
# iconv 
用python批量处理gbk/gb2312格式文件转utf-8  https://blog.csdn.net/sun_tao1/article/details/79746184
python gb2312 转 utf-8  https://blog.csdn.net/weixin_33709219/article/details/91854984  https://my.oschina.net/sskill/blog/655472
# bytes.decode(encoding='gb2312') <-> str.encode(encoding='utf-8')
'''
# coding: utf-8
import chardet
 
f = open('d:/test.txt')
content = f.read()
 
ucontent = content.decode('gb2312').encode('utf-8-sig')
with open('d:/t.txt','w') as f2:
    f2.write(ucontent)

