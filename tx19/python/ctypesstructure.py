#!/usr/bin/env python3
##-*- coding:utf-8 -*-

#python352.chm- 3.5.2 Documentation » The Python Standard Library » 16. Generic Operating System Services » 
# 16.16. ctypes — A foreign function library for Python
#ctypes --- Python 的外部函数库 # https://docs.python.org/zh-cn/3.7/library/ctypes.html
# Q: how to enum?-instead by c_int (eg: myEnum1=ctypes.c_int)? //(from enum import Enum; can't be well with ctypes?)
#        or class myEnum1(ctypes.c_int):pass;  然后甚至可以加__doc__描述可用的枚举值，或get/set值限制?
#
#[Python]ctypes+struct实现类c的结构化数据串行处理 https://www.cnblogs.com/code1992/p/11301586.html 
#  python调用C++ DLL 传参技巧  (cast)   https://www.cnblogs.com/TQCAI/p/8881530.html
#[Python]ctypes+struct实现类c的结构化数据串行处理 https://blog.csdn.net/machael_sonic/article/details/50266499 https://blog.csdn.net/mergerly/article/details/76858589
#


import sys; sys.path ;print(sys.path)
#import ctypesstructure as myt
#pyy -ic'import ctypesstructure as myt'
#pyy -i ctypesstructure.py
#bytes.hex()

import pdb
import ctypes
import ctypes as tt ## Structure Union Array
import pprint as pp ## pprint.pprint

import sys; sf=sys._getframe
sf=sys._getframe # sys._getframe().f_lineno, eval('sys._getframe().f_lineno')
print(sf().f_lineno)
def flno():return eval('sys._getframe().f_code.co_filename')+str(eval('sys._getframe().f_lineno'))
#logging-and-file-line-function
print("here is :",__file__,str(sys._getframe().f_lineno)) #https://www.cnblogs.com/ld1226/p/5639976.html
def get_cur_info():import sys; print('log:', sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno)
get_cur_info();
#sys._current_frames(), sys._getframe(), traceback.print_stack(), inspect.currentframe(),  inspect.stack()[0][1], inspect.trace(), inspect.getframeinfo()
#traceback.extract_stack(limit=2)[0] #python获取当前行号,函数名称,文件名https://blog.csdn.net/iteye_11349/article/details/82679062
#
#import inspect; # to getLine as __LINE__ in c
def lg():import inspect;return '--'+str(inspect.stack()[1][1:4])
print(lg())
#def lg():import sys;f=sys._getframe().f_back;return  ('---',f.f_code.co_filename, f.f_lineno, f.f_code.co_name)
#
import logging #python日志打印模块,输出时间/文件名/行号信息等https://blog.csdn.net/ternence_hsu/article/details/104572415/
#logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y:%H:%M:%S')
#logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d:%(funcName)s] %(message)s', datefmt='%x-%T%z', level=logging.INFO)
#logging.getLogger().setLevel(logging.DEBUG); logger = logging.getLogger(); logger.debug("This is a debug log")
#printf=logging.warn
import datetime; str(datetime.datetime.now())
##


#Python 在 ctypes 中为我们提供了类似C语言的数据类型# https://www.cnblogs.com/adylee/p/10299157.html  https://www.cnblogs.com/rainduck/archive/2011/09/02/2163230.html
#from ctypes import *;
class beer_recipe(ctypes.Structure):_fields_ = [("amt_barley", ctypes.c_int),("amt_water", ctypes.c_char),]
class  barley_amount(ctypes.Union):_fields_ = [("amt_barley", ctypes.c_int),("amt_water",  ctypes.c_char),]
arr=ctypes.c_bool *9; a=arr(); #a=(ctypes.c_bool*9)()
ctypes.sizeof(beer_recipe)
#ctypes.sizeof(beer_recipe),sizeof(barley_amount),sizeof(arr),sizeof(a)
print("hi..")

#class USEROBJECTFLAGS(ctypes.Structure):
#    _fields_ = [("fInherit", ctypes.wintypes.BOOL),


class mycc(ctypes.Structure):_fields_=[("b1",ctypes.c_char),("b2",ctypes.c_long)];pass
#class mycc(ctypes.BigEndianStructure):_fields_=[("b1",ctypes.c_char),("b2",ctypes.c_long)];pass
class myee(ctypes.Structure):_fields_=[("b1",ctypes.c_char),("cc2",mycc)];pass
ctypes.sizeof(mycc), ctypes.sizeof(myee), sys.getsizeof(mycc())#?

c=mycc(0x4b,3); c,c.__class__,'///',c._fields_[1],'///', c.b2,c.__class__.b2
print((c.b1,c.b2,"///",c.__sizeof__(),ctypes.sizeof(c), '//', c.b1,c.b2))
print(mycc,mycc.__name__, c.__class__, c.__class__.__name__)
#mycc._fields_[i], mycc.c1, '///', 'mycc'+'.'+mycc._fields_[i][0], eval('mycc'+'.'+mycc._fields_[i][0])
getattr(c,'b1')
[(e[0],e[1], getattr(c,e[0]),getattr(c.__class__,e[0])) for e in c._fields_]  ##tostring(name,value) #bitfield in ctypes @Python-cytes-str-#getattr#### https://zhuanlan.zhihu.com/p/20182674 
isinstance(c, ctypes.Structure), isinstance(c, ctypes.Union), isinstance(c, ctypes.Array), not isinstance(c, ctypes._SimpleCData), #isinstance(c, ctypes._CData)  ##with getattr() to @wrapper__str__
not isinstance(c, ctypes._SimpleCData), isinstance(c, ctypes._SimpleCData.__mro__[1]),  ctypes.c_int.__mro__[-2], #isinstance(c, ctypes._CData)
#import inspect; inspect.getmembers(c), inspect.isbuiltin(c)
#__str__, __repr__, eval(),exec()   #__str__和__repr__的异同https://segmentfault.com/a/1190000022266368
#c.b2=7;
#
c.__reduce__()[1][1][1]  #_unpickle
import binascii; [hex(e) for e in binascii.b2a_hex(bytes(c))];  binascii.b2a_hex(bytes(c)); str( binascii.b2a_hex(bytes(c)),'utf-8' ) ##bytes.hex(), hex_codec
bytes(c)          #??same to ctypes.string_at(ctypes.addressof(c), ctypes.sizeof(c))
['{:02x}'.format(e) for e in ctypes.string_at(ctypes.addressof(c), ctypes.sizeof(c))] ##bytes.hex()
from ctypes import *; print("===buf:", [i for i in ctypes.string_at(ctypes.addressof(c), ctypes.sizeof(c))] ) ##bytes.hex()
c.b2=7;               print("===buf:", [i for i in ctypes.string_at(ctypes.addressof(c), ctypes.sizeof(c))] )
c2=mycc.from_buffer_copy(string_at(addressof(c), sizeof(c))); print('==', c2, c2.b2)
#c_long.from_buffer_copy((string_at(addressof(c), sizeof(c))), mycc.b2.ofs) #??
#
#POINTER(type), addressof(c),byref(c),pointer(c),
#print [ hex(ord(i)) for i in string_at(addressof(c), sizeof(c))]
#print [(hex(ord(i)),ord(i)) for i in string_at(addressof(c), sizeof(c))]
##

class mydata(ctypes.Structure):
    #_pack_   = 4;#min(pack,self)
    _fields_ = [("b1", ctypes.c_bool), # 1byte for bool accortding to new g++:
                ("b2", ctypes.c_byte),
                ("c3", ctypes.c_char),
                ("l4", ctypes.c_short),
                ("myc",mycc),
                ('kKB', ctypes.c_uint32, 24)
                ]

x=mydata()
x.__sizeof__(), ctypes.sizeof(x)
type(mydata)
type(x)
type(x.b1)
#help(x)
#help(x.b1)
dir(mydata),vars(mydata),  dir(x),vars(x)
print('==', repr(vars(mydata)), '\n',  mydata._fields_)
print('===')
#
print((mydata.b1, mydata.b2, mydata.c3, mydata.l4,  mydata.myc,  mydata.kKB))  ###it shows byte-topology, different from instance
#print(mydata._fields_)
x.b1, x.b2, x.c3, x.l4,  x.myc,  x.kKB
#x.b1.value
y=ctypes.c_int(88);y.value

mydata._fields_[0],mydata._fields_[0][0]
for i in mydata._fields_: print(i)
[i for i in mydata._fields_] ##for class/instance,_fields_ is same. and is not attached to member as __dict__
[i for i in x._fields_]
[i[0] for i in x._fields_]
#[x.__dict__[i[0]] for i in x._fields_]


###
#  class mycc(ctypes.Structure):_fields_=[("b1",ctypes.c_char),("b2",ctypes.c_long)];pass
#class msgBase(ctyes.Structure): _fields_ = [("c1", ctypes.c_char), ("i2", ctypes.c_int), ("c3", ctypes,)]
print('==',sys._getframe().f_lineno)
msgBase=mycc
class msgAA(msgBase): _fields_=[("_f3",ctypes.c_char)]
class msgBB(msgBase): _fields_=[("_f4",ctypes.c_longlong)]
ma=msgAA();
mb=msgBB();
ctypes.sizeof(ma),ctypes.sizeof(msgBB)
print('==', msgBB._fields_, '\n', vars(msgBB), '\n', msgBB._f4, '\n', msgBB._f4.__class__, '--is a data-descriptor (auto?)') #help(msgBB._f4)
##
print('==', sf().f_lineno, lg())
i=ctypes.c_int(2);
i.tt=22; (i.value,i.__dict__); # all _CData is inherited from object class, also c_int,so it's a general instance of object
class myEE(ctypes.c_int): pass  #eg,for Enum
e=myEE(3)
e.tt=33; (e.value,e.__dict__, vars(e))


if 0:
    print("goto interaction--welcome...")
    #import pdb;pdb.set_trace()
    import code
    interp = code.InteractiveConsole(globals())
    interp.interact("") #but some up/down/left/right-move-key-bug with history
    print("goto end-here??")


