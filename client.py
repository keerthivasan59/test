import socket as s

server_addr=('localhost',2345)

clientsocket=  s.socket(s.AF_INET,s.SOCK_STREAM)
clientsocket.connect(server_addr)
data1=" "
while(data1!="end"):
        data1=input("enter msg:")
        clientsocket.send(str.encode(data1))
        if(data1=="end"):
                break
        #clientsocket.send(str.encode(input("enter msg:")))
        data1=clientsocket.recv(1024).decode()
        print(data1)
clientsocket.close()
