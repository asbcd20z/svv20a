#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

class AA: pass

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
# 数据描述符
class DataDes:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        print("访问数据描述符里的 __set__")
        self._score = value

    def __get__(self, instance, owner):
        print("访问数据描述符里的 __get__")
        return self._score

# 非数据描述符
class NoDataDes:
    def __init__(self, default=0):
        self._score = default

    def __get__(self, instance, owner):
        print("访问非数据描述符里的 __get__")
        return self._score


class Student:
    math = DataDes(0)
    chinese = NoDataDes(0)

    def __init__(self, name, math, chinese):
        self.name = name
        print("init--1")
        self.math = math
        print("init--2")
        self.chinese = chinese
        
    def __getattribute__(self, item):
        print("调用 __getattribute__")
        return super(Student, self).__getattribute__(item)
     
    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {},>".format(
                self.name, self.math, self.chinese)



s = Student('小明', 76,  68)
s2= Student('小明', 76,  88)
s,s2

