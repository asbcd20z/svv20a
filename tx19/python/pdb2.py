#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i
#eg: pyy pdb2.py aa  # kill to signal by self

'''
关于python：使用pdb附加进程  https://www.codenong.com/25308847/
os.kill(pid, sig) 
kill -30
##
有一个pdb的克隆，想象中称为pdb克隆，它可以附加到正在运行的进程上。
只需在主进程的代码中添加from pdb_clone import pdbhandler; pdbhandler.register()，然后就可以用pdb-attach --kill --pid PID启动pdb。
'''

import os
import signal
import sys
import time    

def handle_pdb(sig, frame):
    import pdb
    pdb.Pdb().set_trace(frame)    

def loop():
    while True:
        x = 'foo'
        #time.sleep(0.2)
        print(time.time())
        time.sleep(2)

if __name__ == '__main__':
    signal.signal(signal.SIGUSR1, handle_pdb)
    print(os.getpid())
    print((len(sys.argv),sys.argv))
    if (len(sys.argv)>1):
    	os.kill(os.getpid(), signal.SIGUSR1)
    	print(os.getpid(),'killed')
    loop()
