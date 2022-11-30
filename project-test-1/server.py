import socket
import threading

host = "localhost"
port = 5555
clients = []
usernames = []
ips = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"Server is running at {host}:{port}")

def broadcast (message, _client):
    for client in clients:
        if client != _client:
            client.send(message)
    

def handle_messages (client):
    while True:
        try:
            message = client.recv(1024)
            if 'usernames' in str(message):
                print(message.decode('utf-8'))
                data = message.decode('utf-8').split()
                index = usernames.index(str(data[0]))
                next_client = index
                if (next_client + 1) < len(clients):
                    next_client += 1
                else:
                    next_client = 0
                print(usernames[next_client])
                client.send("Who do you want to send an image?\n".encode('utf-8'))
                for username in usernames:
                    client.send(username.encode('utf-8'))
                file = open("pythonimage.jpg", 'wb')
                while True:
                    image = client.recv(1024)
                    if str(image) == "b''":
                        break;
                    file.write(image)
                image = open("pythonimage.jpg", 'rb')
                new_client = clients[next_client]
                for meta_data in image:
                    next_client.send(meta_data)
            else:
                broadcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            ip = ips[index]
            broadcast(f"ChatBot: {username} disconnected".encode('utf-8'), client)
            clients.remove(client)
            usernames.remove(username)
            ips.remove(ip)
            client.close()
            break;
    
def receive_connections ():
    while True:
        client, address = server.accept()
        client.send("@username".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        
        clients.append(client)
        usernames.append(username)
        ips.append(address)
        
        print(f"{username} is connected with {str(address)}")
        
        
        message = f"Chatbot: {username} joined the chat!".encode('utf-8')
        broadcast(message, client)
        
        client.send("Connected to server c:".encode('utf-8'))
        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()
        
receive_connections()