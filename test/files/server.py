import socket, threading

PORT = 9090
#to get the ip (linux and other)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
HOST = s.getsockname()[0]
s.close()
print(HOST)


#to become server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
   while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send(["NICK"].encode('utf-8'))
        nickname = client.recv(1024)


        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is [{nickname}]")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print("Server is running...")
receive()
