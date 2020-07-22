#!/usr/bin/env python3
##-*- coding:utf-8 -*-
import sys; sys.path ;print(sys.path)
#import ctypesstructure as myt
#pyy -ic'import ctypesstructure as myt'
#pyy -i ctypesstructure.py

import pdb
import ctypes
import ctypes as tt ## Structure Union Array
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
ctypes.sizeof(mycc), ctypes.sizeof(myee)

c=mycc(0x42,3); c,c.__class__,'///',c._fields_[1],'///', c.b2,c.__class__.b2
print((c.b1,c.b2,"///",c.__sizeof__(),ctypes.sizeof(c), '//', c.b1,c.b2))
#mycc._fields_[i], mycc.c1, '///', 'mycc'+'.'+mycc._fields_[i][0], eval('mycc'+'.'+mycc._fields_[i][0])
getattr(c,'c1')
[(e[0],e[1], getattr(c,e[0]),getattr(c.__class__,e[0])) for e in c._fields_]  ##tostring(name,value) #bitfield in ctypes @Python-cytes-str-#getattr#### https://zhuanlan.zhihu.com/p/20182674 
isinstance(c, ctypes.Structure), isinstance(c, ctypes.Union), isinstance(c, ctypes.Array)
#c.b2=7;
from ctypes import *; print("===buf:", [i for i in ctypes.string_at(ctypes.addressof(c), ctypes.sizeof(c))] )
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
    _fields_ = [("b1", ctypes.c_bool),
                ("b2", ctypes.c_byte),
                ("c3", ctypes.c_char),
                ("l4", ctypes.c_short),
                ("myc",mycc),
                ('kKB', ctypes.c_uint32, 24)
                ]

x=mydata()
x.__sizeof__()
type(mydata)
type(x)
type(x.b1)
#help(x)
#help(x.b1)
#
print((mydata.b1, mydata.b2, mydata.c3, mydata.l4,  mydata.kKB))  ###it shows byte-topology, different from instance
x.b1, x.b2, x.c3, x.l4,  x.kKB
#x.b1.value
y=ctypes.c_int(88);y.value

mydata._fields_[0],mydata._fields_[0][0]
for i in mydata._fields_: print(i)
[i for i in mydata._fields_] ##for class/instance,_fields_ is same. and is not attached to member as __dict__
[i for i in x._fields_]
[i[0] for i in x._fields_]
#[x.__dict__[i[0]] for i in x._fields_]


if 0:
    print("goto interaction--welcome...")
    #import pdb;pdb.set_trace()
    import code
    interp = code.InteractiveConsole(globals())
    interp.interact("") #but some up/down/left/right-move-key-bug with history
    print("goto end-here??")


