from audioop import add
from email import message
import socket
from xmlrpc.client import ProtocolError

# print(socket.gethostbyname(socket.gethostname()))

HOST = "10.7.221.105"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)


while True:
    communication_socket, address = server.accept()
    print(f"[connection established : address {address}]")
    message = communication_socket.recv(1024).decode("utf-8")
    print("message from client =", message)
    communication_socket.send("got your message".encode("utf-8"))
    communication_socket.close()
    print(f"connection with {address} is closed")
