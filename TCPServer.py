#import socket module

from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#prepare a server socket

serverHost = '127.0.0.1'
serverPort = 1412
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(5)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('connected from ', addr)

    connectionSocket.settimeout(1)
    try:
        message = connectionSocket.recv(4096).decode()
        print(message)
        fileName = message.split()[1]
        f = open(fileName[1:], "rb")
        L = f.read()
        # Send one HTTP header line into socket
        header = """HTTP/1.1 200 OK 
            Content-Length: %d """ % len(L)
        print("-----------------HTTP response  helloWorld.html: ")
        print(header)
        header += L.decode()
        print(L.decode())
        # Send the content of the requested file to the client
        #connectionSocket.send(bytes(header, 'utf-8'))
        for i in range(0, len(header)):
            connectionSocket.send(header[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(b'Not Found')
        # Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data