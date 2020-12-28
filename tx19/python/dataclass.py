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
__annotations__  
annotation  https://docs.python.org/3.9/glossary.html#term-annotation
See variable annotation, function annotation, PEP 484 and PEP 526,  
PEP 526 -- Syntax for Variable Annotations  https://www.python.org/dev/peps/pep-0526/
PEP 484 -- Type Hints                       https://www.python.org/dev/peps/pep-0484/
PEP 557 -- Data Classes                     https://www.python.org/dev/peps/pep-0557/
mixin??
#
理解Python数据类（上）  https://www.sohu.com/a/246836180_114877  https://www.sohu.com/a/246836706_114877
Python 3.7新功能之dataclass装饰器详解  https://www.jb51.net/article/138596.htm
dataclasses-json  https://github.com/gosuai/dataclasses-json
#
'''

#from dataclasses import dataclass
#@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)


__debug__  #Python » 3.5.2 Documentation » The Python Standard Library » 3. Built-in Constants
#import this
#count: int = 0
def foo(x:int, y:float): pass #function-__annotations__
print(foo, foo.__annotations__, foo.__annotations__.__class__.__name__)


