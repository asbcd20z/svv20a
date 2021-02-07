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


