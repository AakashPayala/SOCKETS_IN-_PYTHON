from audioop import add
from email import message_from_string
import socket
from xmlrpc.client import ProtocolError
from xmlrpc.server import ServerHTMLDoc

HOST="192.168.112.1"
PORT=9090

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()
print("waiting for connection : ")
while True:
    
    client_communication, address=server.accept()
    
    print(f"connected to {address}")
    client_communication.send("thank you for connecting with us!! ".encode("utf-8"))
    message_from_client =client_communication.recv(1024).decode("utf-8")
    print(message_from_client)
    message2=client_communication.recv(1024).decode("utf-8")
    print(message2)
    message3=client_communication.recv(1024).decode("utf-8")
    print("2nd value is ->", message3)
    print(f"[connection with {address} is closed ]")
    client_communication.close()

