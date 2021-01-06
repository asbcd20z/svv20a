#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

class AA: pass

class A:
	x1=1
	def __init__(self):print('==in A init');self.x2=2; ## not work,for x2 is excluded by bad __setattr__
	## all these __getattribute__,__getattr__,__setattr__ are about instance likely?, not class
	## and 通常应该是补充增强其函数的功能(最后调用原object的函数)，而非去掉
	def __getattribute__(self, name):
		print('==in A __getattribute__',name)
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print('==in A __getattr__',name)
		#return self.__dict__[name]
	def __setattr__(self, name, val):
		print('==in A __setattr__',name)
		if name!='x2' :self.__dict__[name]=val  ## exclude x2

class B(A):
	def __init__(self): self.bx=1; #super().__init__()
	def spam(self):
		print('spam')

class CC:pass

a=A()
print("--")
A.x1  ## A.x1 not use __getattribute__, which "Called unconditionally to implement attribute accesses for instances of the class"
a.x1
a.x2  ## not work,for x2 is excluded by bad __setattr__
a.x3=3
print("--")
print([a.x3, getattr(a,'x3')])
print("---")
b=B()
'to',b.spam,B.spam
'call',b.spam(),B.spam
b.bx
#b.by
print("---")
c=CC()
#setattr(c,'x',1)
print(['c.x-default', getattr(c,'x',99)])



