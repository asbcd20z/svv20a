#!/usr/bin/env python3
##-*- coding:utf-8 -*-

#Python » 3.5.2 Documentation » The Python Language Reference » 
#3. Data model/3.3.2. Customizing attribute access
#python描述符理解 www.cnblogs.com/wancy86/p/descriptor.html
#python核心编程v2-13.16.3  特殊方法__getattribute__()
#
#Python的__getattribute__二三事 https://www.cnblogs.com/telecomshy/p/10605679.html
#Python描述符深入理解            https://www.cnblogs.com/telecomshy/p/10168853.html
#

import sys

class A():
	x=11
a=A()
[i for i in dir(A) if not i.startswith('__')]
def notbf(s):return not s.startswith('_');
notb=lambda s:'_'!=s[0]
#list(filter(notb, dir(A)) )
def xdir(cls):return [i for i in dir(cls) if not i.startswith('__')]

class Foo():
	def foo():print ('call foo');
	def foo2(self):print ('call foo2');
f=Foo()

class Mydesc():
	def __get__(self,owner,ocls):print('geta')
	def __set__(self,owner,value):print('seta')
	def __delete__(self,owner):print('dela')


class G():
	def __getattribute__(self, attr):print('geta')



##


'''
gl=1
class B():
	def foo(self):print('BB')
class B2():
	def foo(self):print('BB2')
class D(B,B2):
	def foo(self):
		#x=super();
		global gl;
		gl=super()
		super().foo();#super(D,self).foo();
		print('DD', super())
d=D()
d.foo()
'''


class T():
	x=1
	def __init__(self):
		self.y=2
		self.z=3
	def foo():pass
	foo.fx=4
t=T()
T.__dict__, t.__dict__, t.foo.__dict__, T.foo.__dict__