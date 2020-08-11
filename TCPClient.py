from socket import *

HOST = '127.0.0.1'
PORT = 10399

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST, PORT))
sentent = ('KhanhUong.txt')
try:
    clientSocket.sendall(sentent.encode())
    message = clientSocket.recv(1024).decode()
    print(message)
finally:
    clientSocket.close()