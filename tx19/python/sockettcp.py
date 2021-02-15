

#Python学习之Socket通信的实现
#https://blog.csdn.net/m0_37717595/article/details/81101895
#socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)


##
def doserver():
	import socket
	 
	#1、创建服务端的socket对象
	server_socket = socket.socket()
	 
	#2、绑定一个ip和端口
	#server_socket.bind(('192.168.0.9',9091))
	server_socket.bind(('',9091)) #0.0.0.0
	 
	#3、服务器端一直监听是否有客户端进行连接
	print('server_socket is listening 9091')
	server_socket.listen(3)
	 
	#4、如果有客户端进行连接、则接受客户端的连接
	clientSockt,addr =  server_socket.accept()   #返回客户端socket通信对象和客户端的ip
	 
	#5、客户端与服务端进行通信
	data = clientSockt.recv(1024).decode('utf-8')
	print('服务端收到客户端发来的消息:%s'%(data))
	 
	#6、服务端给客户端回消息
	clientSockt.send(b'I am a server')
	 
	#7、关闭socket对象
	clientSockt.close()    #客户端对象
	server_socket.close()  #服务端对象


##
def doclient():
	import socket
	#1、创建socket通信对象
	clientSocket = socket.socket()
	 
	#2、使用正确的ip和端口去链接服务器
	#clientSocket.connect(('192.168.0.9',9091))
	clientSocket.connect(('',9091)) #127.0.0.1
	 
	#3、客户端与服务器端进行通信
	    # 给socket服务器发送信息
	clientSocket.send(b'I am a client')
	 
	    # 接收服务器的响应(服务器回复的消息)
	recvData = clientSocket.recv(1024).decode('utf-8')
	print('客户端收到服务器回复的消息:%s'%(recvData))
	 
	#4、关闭socket对象


##
def main(argv):
    if argv[1][0]=='s': doserver()
    if argv[1][0]=='c': doclient()

if __name__ == '__main__':
    import sys;print(sys.argv)
    if len(sys.argv)<2: print('+(c/s)');sys.exit(-1)
    main(sys.argv)

