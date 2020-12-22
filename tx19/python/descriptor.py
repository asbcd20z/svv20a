#!/usr/bin/env python3
##-*- coding:utf-8 -*-

#Python » 3.5.2 Documentation » The Python Language Reference » 
#3. Data model/3.3.2. Customizing attribute access
# __getattr__() ..., __getattribute__()
#python描述符理解 www.cnblogs.com/wancy86/p/descriptor.html
#python核心编程v2-13.16.3  特殊方法__getattribute__()
#
#Python的__getattribute__二三事 https://www.cnblogs.com/telecomshy/p/10605679.html
#Python描述符深入理解        #   https://www.cnblogs.com/telecomshy/p/10168853.html
#
#深入理解 Python 描述符  (why#)  https://www.cnblogs.com/wongbingming/p/13555963.html
'''
2. 描述符的访问规则#
描述符分两种：
数据描述符：实现了__get__ 和 __set__ 两种方法的描述符
非数据描述符：只实现了__get__ 一种方法的描述符
你一定会问，他们有什么区别呢？网上的讲解，我看过几个，很多都把一个简单的东西讲得复杂了。
--
其实就一句话，数据描述器和非数据描述器的区别在于：它们相对于实例的字典的优先级不同。
如果实例字典中有与描述符同名的属性，如果描述符是数据描述符，优先使用数据描述符，如果是非数据描述符，优先使用字典中的属性。
'''
#
#深入理解Python描述符 https://blog.csdn.net/woshijidutu/article/details/77893318?utm_source=blogxgwz6
# 《流畅的Python》  根据描述符中是否定义了__set__方法可以把描述符分为覆盖型和非覆盖型，有__set__方法就是覆盖型描述符, 
# 覆盖型描述符还可以分为两类，有__get__方法的覆盖型和没有__get__方法的覆盖型。
#
#Python学习——面向对象高级之描述符  https://blog.csdn.net/zhaoyun_zzz/article/details/82179481
#python关于描述符__set__ ,__get__ , __delete__  https://blog.csdn.net/Mr_Slower/article/details/83590823
#Python语言学习讲解十六：python之描述符__set__和__get__ 等解释  https://blog.csdn.net/Windgs_YF/article/details/53409482
#
##
#深入理解python super     https://coordinate.blog.csdn.net/article/details/79531891
#baidu,Guido van Rossum super()
#Python学习资料  Super https://www.cnblogs.com/macula7/archive/2009/08/17/1960737.html
#简介Python之super的用法及原理 https://blog.csdn.net/nirendao/article/details/48863215
#[Things to Know About Python Super] by Michele Simionato  https://www.artima.com/weblogs/viewpost.jsp?thread=236275
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
	ss=Mydesc()
	def __getattribute__(self, name):print('geta-owner'); return super().__getattribute__(name)
	#def __getattr__(self, name): pass
g=G()


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

