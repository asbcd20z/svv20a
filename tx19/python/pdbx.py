#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i
#pyy -mpdb
#python2 -m trace --trace sinx.py | grep sinx.py  
#traceback.extract_stack()  

'''
Documentation » The Python Standard Library » Debugging and Profiling »
pdb — The Python Debugger  https://docs.python.org/3/library/pdb.html
Python » 3.5.2 Documentation » The Python Standard Library » 27. Debugging and Profiling » 
#
入门 Python 调试器 pdb  https://blog.csdn.net/weixin_30230009/article/details/106346139
//调试线上的 Python 程序时，虽然 PyCharm 可以实现远程调试，但 pdb 才是最便捷的方式，...   
//设置断点分两种，一种是侵入式的添加断点，需要在希望被断点处添加 **「import pdb;pdb.set_trace ()」，
//另一种则是非入侵式的添加断点，通过 - m 指定参数指定通过 pdb 来运行项目，完整命令为「python3 -m pdb 斐波那契数列.py」**，该命令会将断点打在程序的入口。
#
python pdb attach_关于python：使用pdb附加进程  https://blog.csdn.net/weixin_39866487/article/details/111538420
关于python：使用pdb附加进程  https://www.codenong.com/25308847/
'''

import pdb
import sys
def lg():import inspect;return '--'+str(inspect.stack()[1][1:4])
class AA: pass
##
def handle_pdb(sig,frame):import pdb;pdb.Pdb().set_trace(frame)
import signal; signal.signal(signal.SIGUSR1, handle_pdb)
#import os; os.kill(os.getpid(), signal.SIGUSR1)    
##
#
print("hi..")
#pdb.set_trace ()

x=1
print(x)

def foo():
	print(1)
def f2():
	foo()
f2()

print('end..')