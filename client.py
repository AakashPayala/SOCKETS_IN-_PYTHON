import socket

HOST = "10.7.221.105"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("hello world ".encode("utf-8"))
print(client.recv(1024).decode("utf-8"))
