#!/usr/bin/env python3
##-*- coding:utf-8 -*-
import sys; sys.path ;print(sys.path)
#import ctypesstructure as myt
#pyy -ic'import ctypesstructure as myt'
#pyy -i ctypesstructure.py
#pytest -sv test_.py  --setup-show
##algorithm
'''
Python测试框架之pytest详解 https://blog.csdn.net/lovedingd/article/details/98952868
Pytest - 使用介绍 https://www.jianshu.com/p/a754e3d47671
Pytest 使用简介 https://www.cnblogs.com/shenh/p/11572657.html
https://wiki.python.org/moin/PythonTestingToolsTaxonomy
https://docs.pytest.org/en/stable  https://docs.pytest.org/en/stable/reference.html#fixtures
https://docs.pytest.org/en/latest/contents.html#toc
https://docs.pytest.org/en/latest/example/simple.html#how-to-change-command-line-options-defaults
https://pypi.org/project/pytest/
https://learning-pytest.readthedocs.io/zh/latest/    Pytest 使用手册##
https://learning-pytest.readthedocs.io/zh/latest/doc/fixture/scope.html
Pytest学习之use fixtures(pytest.fixture/pytest.fixture(autouse=True)/pytest.mark.usefixtures的区别-以及返回值) https://www.cnblogs.com/nuonuozhou/p/10429846.html
https://docs.pytest.org/en/latest/mark.html
https://docs.pytest.org/en/latest/example/markers.html#mark-examples
'''
##
import pdb

import pytest

#def pytest_configure(config): config.addinivalue_line( "mymark", "my-mark")
@pytest.mark.mymark
def test_hi_test(): print("hi")
def test_Hi():
	print('hi..')
def test_Hi2():
	print('hi2..')
	assert(0==1)
##
@pytest.fixture
def afix(): return "afix-"
def test_Hi3(afix):	print('hi3..',afix)
@pytest.mark.usefixtures("afix")  #call by no arg from return result to be used, also can "pytest.fixture(autouse=True)"
def test_Hi3b(): print('hi3b..',afix)
##
@pytest.fixture(params=[('redis', '6379'),('elasticsearch', '9200')])
def afix_param(request): return request.param;
def test_Hi4(afix_param): print('hi4..',afix_param)
##
#pytest.mark.parametrize(argnames, argvalues)
#@pytest.mark.parametrize("arg1",[0,1])
@pytest.mark.parametrize("arg1",range(2))
@pytest.mark.parametrize("para1, para2",[('a','b'),('c','d')])
def test_Hi5(arg1, para1, para2):
	print('hi5..',(arg1, para1, para2))


######
@pytest.fixture(scope='function') #by default
def func_scope(): pass
@pytest.fixture(scope='module')
def mod_scope(): pass
@pytest.fixture(scope='session')
def sess_scope(): pass
@pytest.fixture(scope='class')
def class_scope(): pass
def test_multi_scope(sess_scope, mod_scope, func_scope): pass #pytest --setup-show
class Test_my2():
	def test_1(self, sess_scope, mod_scope, func_scope,  class_scope): pass
	def test_2(self, sess_scope, mod_scope, func_scope,  class_scope): pass

##===
#
def pmn(pre,l):
	#print(pre,l)
	if not len(l): print("--",pre);return
	#if 3==len(pre): print("--",pre);return
	for i in l:
		l2=[e for e in l if e!=i];
		#pmn(list(pre),l2);
		pre2=list(pre)
		pre2.append(i)
		#print('+',pre2)
		l2=[e for e in l if e!=i];
		pmn(pre2, l2)
def test_pmn():
	'''p(m/n)'''
	l=[1,2,3];
	pre=[]
	pmn(pre,l)
##
def smn(pre,l):
	#print(pre,l)
	if not len(l): print("--",pre);return
	#for i in l:
	if len(l):
		i=l[0]
		l2=[e for e in l if e!=i];
		smn(list(pre),l2);
		pre2=list(pre)
		pre2.append(i)
		#print('+',pre2)
		l2=[e for e in l if e!=i];
		smn(pre2, l2)
def test_smn():
	'''full-sub-sets'''
	l=[1,2,3];
	pre=[]
	smn(pre,l)


##===
#if __name__=="__main__": print("main.hi");pytest.main("-s  test_abc.py")
if __name__=="__main__": test_pmn()
