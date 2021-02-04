#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i


class AA: pass
print("hi..")
def lg():import inspect;return '--'+str(inspect.stack()[1][1:4])
print(lg())


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
'''
#Python » 3.5.2 Documentation » Python HOWTOs » Descriptor HowTo Guide
If an object defines both __get__() and __set__(), it is considered a data descriptor. 
Descriptors that only define __get__() are called non-data descriptors (they are typically used for methods but other uses are possible).
--
Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance’s dictionary. If an instance’s dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence. If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.
#
descriptor 
Any object which defines the methods __get__(), __set__(), or __delete__(). When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using a.b to get, set or delete an attribute looks up the object named b in the class dictionary for a, but if b is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python because they are the basis for many features including functions, methods, properties, class methods, static methods, and reference to super classes.
For more information about descriptors’ methods, see Implementing Descriptors.
#
##
#python关于描述符__set__ ,__get__ , __delete__  https://blog.csdn.net/Mr_Slower/article/details/83590823
#Python » 3.5.2 Documentation » The Python Language Reference » 3. Data model
#3.3.2.1. Implementing Descriptors
The following methods only apply when an instance of the class containing the method (a so-called descriptor class) appears in an owner class (the descriptor must be in either the owner’s class dictionary or in the class dictionary for one of its parents). In the examples below, “the attribute” refers to the attribute whose name is the key of the property in the owner class’ __dict__.
The following methods only apply, when an instance [of the class containing the method (a so-called descriptor class)] appears in an owner class (the descriptor must be in either the [owner’s class dictionary] or in the class dictionary for one of its parents). In the examples below, “the attribute” refers to the attribute whose name is the key of the property in the owner class’ __dict__.
下列方法只有在包含这些方法的类的实例出现在"所有者"类中(所有者的属性字典或者其父类的属性字典中)时才适用.
#
1)object.__ get__(self, instance, owner)
Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). owner is always the owner class, while instance is the instance that the attribute was accessed through, or None when the attribute is accessed through the owner. This method should return the (computed) attribute value or raise an AttributeError exception.
当需要访问所有者类的属性或所有者类的实例的属性时被调用.其中参数owner就是所有者类, instance是要访问属性的实例,当所以者类访问属性时,该参数为None. 该方法应该返回属性值或抛出错误
#
2)object.__ set__(self, instance, value)
Called to set the attribute on an instance instance of the owner class to a new value, value.
调用以将所有者类的实例instance设置为一个新值value.
#
3)object.__ delete__(self, instance)
Called to delete the attribute on an instance instance of the owner class.
调用以删除所有者类的实例的属性
#
4)object.__ set_name__(self, owner, name)
Called at the time the owning class owner is created. The descriptor has been assigned to name.
当所有者类被创建时调用,描述符被赋值给name
'''

###
'''
1)描述符本质就是一个新式类, 在这个类中, 至少实现了 __ set__, __ get__,
__ delete__ 三种方法中的一种, 也被称为描述符协议.
__ get__ : 调用相关属性时触发;
__ set__ : 修改相关属性时触发;
__ delete__ : 删除相关属性时触发;
2)至少同时具有前两种方法的描述符称为数据描述符,
不具有__ set__ 方法的称为非数据描述符.
3)属性调用优先级: 类属性>数据描述符>实例属性>非数据描述符
4)描述符必须定义为类属性,不可放到函数中.
示例:
'''
class Test:
    name = 'Testhahahaha'
    
       #self:描述符对象n, instance:实例t1, owner:t1所属的类Test1
    def __get__(self, instance, owner):  
        print('====>get')
        #print(self, instance, owner, sep='\n')
        return self

    def __set__(self, instance, value):    #value:值3
        print('====>set')
        #print(self.name, instance, value, sep='\n')
        instance.__dict__['n'] = value

    def __delete__(self, instance):
        print('====>delete')
        print(self, instance)

class Test1:
    n = Test()

    def __init__(self, name):
        self.name = name


print(lg())

#Test1.n = 'abc'   # 类属性的设置优先级高于描述符,不触发__set__  ///
Test1.n             # 类调用属性会触发__get__
print('=====>hahaha')
t1 = Test1('sabi')  # 不涉及属性n时不会触发描述符
t1.n = 3            # 触发__set__, 增加属性n,但类属性不变
print(t1.__dict__)
print(t1.n)         # 触发__get__
del t1.n            # 触发__delete__
print('=====分隔')
del Test1.n         # 类删除属性也不会触发__delete__
#my
print(lg(), t1.n, '\n')  # my-直接打印值3。 Test1.n已被删除so不再是描叙符,不触发__get__  

'''
#result
====>get
<__main__.Test object at 0x000001908F997470>
None
<class '__main__.Test1'>
=====>hahaha
====>set
{'name': 'sabi', 'n': 3}
====>get
<__main__.Test object at 0x000001908F997470>
<__main__.Test1 object at 0x000001908F997BA8>
<class '__main__.Test1'>
<__main__.Test object at 0x000001908F997470>
====>delete
<__main__.Test object at 0x000001908F997470> <__main__.Test1 object at 0x000001908F997BA8>
=====分隔
'''


'''
示例2: 非数据描述符,注意设置实例属性时描述符中也不能有delete方法,否则会报错
'''
class Test:
    name = 'Testhahahaha';
    print(lg()) # called here

    def __get__(self, instance, owner):
        print('====>get')
        #print(self, instance, owner, sep='\n')
        print((self, instance, owner))
        return self

    # def __delete__(self, instance):
    #     print('====>delete')
    #     print(self, instance)

class Test1:
    n = Test()

    def __init__(self, name):
        self.name = name

#my
print(lg())
t1=Test1('my')  
print('out:', t1.n)     # my-触发get, 它是non-data描叙符  
print('out:', Test1.n)  # my-类调用属性 触发get, 它是non-data描叙符  
#Test1.n=11             # my-不再是non-data描叙符
#
t1 = Test1('sabi')
t1.n = 'niubi'        #没有set, 所以不会触发
print(t1.__dict__)
print(t1.n)          #已经和描述符无关, 所以不会触发get  
del t1.n
print(t1.__dict__)

'''
#result
{'name': 'sabi', 'n': 'niubi'}
niubi
{'name': 'sabi'}
'''


'''
示例3: __ set_name__
'''
class Test:
    name = 'Testhahahaha'

    def __get__(self, instance, owner):
        print('====>get')
        print(self, instance, owner, sep='\n')
        return self

    def __set_name__(self, owner, name):
        #print('setname', owner, name, sep='\n')
        print(('setname', owner, name))  # my-仅仅从python3.6 开始支持  

print('\n', lg(), 'python3.6 supported newly')
class Test1:
    n = Test()

    def __init__(self, name):
        self.name = name

'''
#result
setname
<class '__main__.Test1'>
n
'''


###
'''
2.描述符的应用
1)示例4: 输入类型限制,描述输入参数的类型
2)示例5: 利用描述符自己定制property
'''

