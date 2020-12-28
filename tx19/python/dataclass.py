#!/usr/bin/env python3
##-*- coding:utf-8 -*-

import sys; sys.path ;print(sys.path)
#import ctypesstructure as myt
#pyy -ic'import ctypesstructure as myt'
#pyy -i ctypesstructure.py
#bytes.hex()


'''memo
Documentation » Python 标准库 » Python运行时服务 »
 dataclasses --- 数据类  https://docs.python.org/zh-cn/3.9/library/dataclasses.html
#https://docs.python.org/3.9/  [HTML Help (.chm) files are made available in the "Files" section on the Python download page.]
#https://docs.python.org/zh-cn/3.9/download.html
#https://www.python.org/downloads/release/python-391/
__annotations__  
annotation  https://docs.python.org/3.9/glossary.html#term-annotation
See variable annotation, function annotation, PEP 484 and PEP 526,  
PEP 526 -- Syntax for Variable Annotations  https://www.python.org/dev/peps/pep-0526/
PEP 484 -- Type Hints                       https://www.python.org/dev/peps/pep-0484/
PEP 557 -- Data Classes                     https://www.python.org/dev/peps/pep-0557/
mixin??
python monkey_patch //Pyhon基础：Monkey Patch（猴子补丁）https://blog.csdn.net/fly910905/article/details/77152110
#
理解Python数据类（上）  https://www.sohu.com/a/246836180_114877  https://www.sohu.com/a/246836706_114877
Python 3.7新功能之dataclass装饰器详解  https://www.jb51.net/article/138596.htm
dataclasses-json  https://github.com/gosuai/dataclasses-json
#
'''

#from dataclasses import dataclass
#@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)


assert 1,'err'
if __debug__: pass  #-0, Python » 3.5.2 Documentation » The Python Standard Library » 3. Built-in Constants
#import this
#count: int = 0
def foo(x:int, y:float): pass #function-__annotations__
print(foo, foo.__annotations__, foo.__annotations__.__class__.__name__)


