from audioop import add
import socket

HOST = "10.7.221.105"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
print("[SERVER IS RUNNING WAITING FOR CLIENT ]")
server.listen()

while(True):

    client_comm, address = server.accept()
    print(f"connected with client {address} ")

    client_comm.send("thank you for connecting with us ".encode("utf-8"))
    message = client_comm.recv(1024).decode("utf-8")

    print(f"message from client {message}")

    client_comm.close()
