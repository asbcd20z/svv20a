#!/usr/bin/env python3
##-*- coding:utf-8 -*-
#pyy -i

def lg():import inspect;return '--'+str(inspect.stack()[1][1:4])
class AA: pass
print("hi..")


##
'''
Python UDP实例  https://www.cnblogs.com/xiao-apple36/p/9279108.html
Python之UDP编程 https://www.cnblogs.com/yunche/p/9033666.html  https://www.liaoxuefeng.com/wiki/1016959663602400/1017790181885952
busybox nc -uv -lp 9999 127.0.0.1  #localhost. nc server use ipv6 addr by default,so assign a ipv4 more
busybox nc -v -lp 9999  127.0.0.1 -e cat; busybox nc -v 0.0.0.0 9999  #to echo.
//ps, loopback ipv6 ::1
'''

##
def doserver():
    import socket
    BUFSIZE = 1024
    ip_port = ('127.0.0.1', 9999)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
    server.bind(ip_port)
    while True:
        data,client_addr = server.recvfrom(BUFSIZE)
        print('s.recv', data)
     
        server.sendto(data.upper(),client_addr)
     
    server.close()

##
def doclient():
    import socket
    BUFSIZE = 1024
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        msg = input(">> ").strip()
        ip_port = ('127.0.0.1', 9999)
        print(msg.encode('utf-8'))
        client.sendto(msg.encode('utf-8'),ip_port)
     
        data,server_addr = client.recvfrom(BUFSIZE)
        print('c.recvfrom ',data,server_addr)
     
    client.close()
##

if __name__ == '__main__':
    import sys;print(sys.argv)
    if len(sys.argv)<2: print('+(c/s)');sys.exit(-1)
    if sys.argv[1][0]=='s': doserver()
    if sys.argv[1][0]=='c': doclient()

