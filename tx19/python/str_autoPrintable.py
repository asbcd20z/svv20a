#!/usr/bin/env python3
##-*- coding:utf-8 -*-

#python – 如何正确实现__str__和__repr__   https://www.icode9.com/content-1-359907.html
#__str__, __repr__, eval() , callable() #__str__和__repr__的异同https://segmentfault.com/a/1190000022266368
import sys;

##===1
print('//',sys._getframe().f_lineno)
class MyClass(object):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return 'MyClass({})'.format(self.a)

    def __repr__(self):
        return 'MyClass({!r})'.format(self.a)

##
'''
>>> myobject = MyClass(np.array([1, 2]))
>>> str(myobject)
'MyClass([1 2])'
>>> repr(myobject)
'MyClass(array([1, 2]))'
'''


##==2
print('//',sys._getframe().f_lineno)
def stringify(obj, attrs, strfunc):
    values = []
    # get each attribute's value and convert it to a string
    for attr in attrs:
        value = getattr(obj, attr)
        values.append(strfunc(value))

    # get the class name
    clsname = type(obj).__name__

    # put everything together
    args = ', '.join(values)
    return '{}({})'.format(clsname, args)

print( stringify(MyClass('foo'), ['a'], repr) )
# output: MyClass('foo')


##===3
print('//',sys._getframe().f_lineno)
class Printable:
    def __str__(self):
        return self.__stringify(str)

    def __repr__(self):
        return self.__stringify(repr)

    def __stringify(self, strfunc):
        values = []
        for attr in self._attributes:
            value = getattr(self, attr)
            values.append(strfunc(value))

        clsname = type(self).__name__
        args = ', '.join(values)
        return '{}({})'.format(clsname, args)

class MyClass(Printable):
    _attributes = ['a']

    def __init__(self, a):
        self.a = a

print(MyClass('aaa')) #==


##===4
print('//',sys._getframe().f_lineno)
import inspect

class AutoPrintable:
    def __str__(self):
        return self.__stringify(str)

    def __repr__(self):
        return self.__stringify(repr)

    def __stringify(self, strfunc):
        sig= inspect.signature(self.__init__)
        values= []
        print('--', sig, sig.parameters) #==
        for attr in sig.parameters:
            print('--',attr)
            value= getattr(self, attr)
            values.append(strfunc(value))

        clsname= type(self).__name__
        args= ', '.join(values)
        return '{}({})'.format(clsname, args)

class MyClass(AutoPrintable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

print( str(MyClass('foo', 'bar')) ) # output: MyClass(foo, bar)
print( repr(MyClass('foo', 'bar')) ) # output: MyClass('foo', 'bar')

##
x=MyClass('foo', 'bar')
sig=inspect.signature(x.__init__)
sig, sig.parameters,  '///', str(sig), [e for e in sig.parameters]
str(sig), str(sig.parameters),         [e for e in sig.parameters]
