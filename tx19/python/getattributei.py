#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

class AA: pass
print("hi..")

'''
Python的__getattribute__二三事 https://www.cnblogs.com/telecomshy/p/10605679.html
'''

##
#1.object类有__getattribute__属性，因此所有的类默认就有__getattribute__属性（所有类都继承自object），object的__getattribute__起什么用呢？它做的就是查找自定义类的属性，如果属性存在则返回属性的值，如果不存在则抛出AttributeError。
#还是看代码：
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
#当在命令行输入b.spam(，甚至括号还没有输入完整的时候，就已经触发了__getattribute__。可见，当实例在查找任何属性的时候（注意是实例，这是另一个知识点，后面再详谈），都会触发__getattribute__方法。
#基于此特性，可以方便的使用类装饰器为其所有属性（不管是有的还是没有的）扩充功能，例如，加一个log记录功能，代码如下：
def log_attr(cls):
	cls_getattribute = cls.__getattribute__
	def new_getattribute(self, name):
		print('catch name')
		return cls_getattribute(self, name)
	cls.__getattribute__ = new_getattribute
	return cls

@log_attr
class C:
	def __init__(self, x):
		self.x = x
	def spam(self):
		print('spam')

c = C(42)
c.x, c.spam
c.spam()


##
#2.只有在实例的命名空间查找属性的时候，才会触发__getattribute__，在类的命名空间中查找，是不会触发__getattribute__的。
#还是第一个例子：
B.spam
b=B()
#b.spam()
B.spam(b)

#可见，当类直接调用spam方法的时候，不会触发__getattribute__，而且当以B.spam(b)形式调用的时候，巧妙的绕过了__getattribute__。


##
#接下来，是一个重要的知识点，即特殊的方法，如__len__，__str__等等操作符重载方法，当隐式调用的时候，在python3中会直接在类的命名空间中查找，因此是不会触发__getattribute__的！！如下：
class CC:
	def __len__(self):
		return 42
	def __getattribute__(self, name):
		print(r'catch {name}'); #print(f'catch {name}')
		return super().__getattribute__(name)
c2 = CC()
len(c2)

#but，当直接显示调用的时候，python不会将其当作啥特殊方法，仍然会从实例的命名空间查找，此时，就会触发__getattribute__：
c2.__len__()


###
#最大的影响就是，在委托类型的代码中，操作符重载的方法代码得重新写，如下：
#...如, len()隐式调用的时候,因为没有触发__getattribute__，故而没有foward到被代理对象的__len__
class A3:
	def __len__(self):
		return 42
	def attr1(self):
		print('attr1')
class B3:
	def __init__(self):
		self.a = A3()
	def __getattribute__(self, name):
		if name == 'a':
			return super().__getattribute__(name)
		else:
			return getattr(self.a, name)
b=B3()
b.attr1()
len(b)
#可见，attr1正确的被代理，但是len方法没有被代理，因为隐式调用的时候，直接在B类的命名空间查找__len__方法，根本就没有触发__getattribute__。如果显示调用，就可以被代理了。
b.__len__()

#最后，还有一个坑需要注意，如上例B类的__getattribute__方法中，判断一下a是否B自身的实例属性的代码不可少，是则调用"父类的" __getattribute__方法返回正确的self.a，否则在getattr(self.a, name)中，self.a会不断的触发__getattribute__，从而会陷入无限循环。
#对了，最后还有一小点，有一个比较特殊的操作符重载方法，即dir，因为它会从实例的命名空间开始查找__dict__和__class__特殊方法，因此也会触发__getattribute__。

