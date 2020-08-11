import socket


def CreateSever(host, port):
    Sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sever.bind((host, port))
    Sever.listen(5)
    return Sever


def ReadRequest(Client):
    re = ""
    Client.settimeout(1)
    try:
        re = Client.recv(1024).decode()
        while (re):
            re = re + Client.recv(1024).decode()
    except socket.timeout:  # fail after 1 second of no activity
        if not re:
            print("Didn't receive data! [Timeout]")
    finally:
        return re


# 2. Client connect Sever + 3. Read HTTP Request
def ReadHTTPRequest(Sever):
    re = ""
    while (re == ""):
        Client, address = Sever.accept()
        print("Client: ", address, " da ket noi toi sever")
        re = ReadRequest(Client)
    return Client, re


def SendFileIndex(Client):
    f = open("helloWorld.html", "rb")
    L = f.read()
    header = """HTTP/1.1 200 OK 
    Content-Length: %d """ % len(L)
    print("-----------------HTTP response  helloWorld.html: ")
    print(header)
    header += L.decode()
    print(L.decode())
    Client.send(bytes(header, 'utf-8'))



# 4. Send HTTP Response  + 5. Close Sever
def MoveHomePage(Sever, Client, Request):
    if "GET /helloWorld.html HTTP/1.1" in Request:
        SendFileIndex(Client)
        Sever.close()
        return True


# image 1
# tu viet
# image 2
# tu viet

if __name__ == "__main__":
    print("Phan 1: tra ve trang chu khi truy cap sever")
    # 1. Create sever Socket
    Sever = CreateSever("localhost", 8080)
    # 2. Client connect Sever + 3. Read HTTP Request
    Client, Request = ReadHTTPRequest(Sever)
    print("----------------HTTP request: ")
    print(Request)
    # 4. Send HTTP Response  + 5. Close Sever
    MoveHomePage(Sever, Client, Request)

