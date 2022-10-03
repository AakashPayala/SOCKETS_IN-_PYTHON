from http import client
import socket

HOST="192.168.112.1"
PORT=9090

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))
client.send("hello server this is client 1".encode("utf-8"))
print("enter a value : ")
x=input()
client.send(x.encode("utf-8"))
y=input("another value  : ")
client.send(y.encode("utf-8"))

print(client.recv(1024).decode("utf-8"))

client.close()

