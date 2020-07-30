#!/usr/bin/env python
#test_so.py
from ctypes import cdll
import os

#f= CDLL(os.getcwd() + '/libfunc.so')
p = os.getcwd() + '/libfunc.so'
f = cdll.LoadLibrary(p)
print p,':', f.func(99)

##
import ctypes
from ctypes import *
class mycc(Structure):pass
#mycc._pack_ =4;
mycc._fields_=[('c1',c_char),('i2',c_int),('s3',c_short*22),('i4',c_int)]  ##('s3',c_short*20)
c=mycc('B',3, i4=0x12345678);c.s3[21]=0xabcd
print 'sizeof:',sizeof(mycc),sizeof(c)
print f.fcc(c)
#POINTER(type), addressof(c),byref(c),pointer(c),
print [ hex(ord(i)) for i in string_at(addressof(c), sizeof(c))]
print [(hex(ord(i)),ord(i)) for i in string_at(addressof(c), sizeof(c))]

##
c2=mycc.from_buffer_copy(string_at(addressof(c), sizeof(c))); print '==',c2,c2.i2
c3=mycc.from_address(addressof(c)); print '==',c3,c3.i2
c.i2=33; print '==',c,c.i2
pass;    print '==',c3,c3.i2
#
cbuf=ctypes.create_string_buffer(string_at(addressof(c), sizeof(c)))
str(list(cbuf)); cbuf[4]='A'; cbuf[4]
c4=mycc.from_buffer(cbuf); print '==',c4,c4.i2
#import binascii; binascii.b2a_hex(c); binascii.b2a_hex(cbuf)  #Aborted (core dumped) to stackdump when finished, why?


##
#import pdb;pdb.set_trace()

#POINTER(type), addressof(c),byref(c),pointer(c),
#[ord(i) for i in string_at(addressof(c), sizeof(c))]
print '-end'