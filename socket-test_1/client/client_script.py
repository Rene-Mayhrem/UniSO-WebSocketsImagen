import socket
import sys   
import threading

username = input("Enter your username: ")

host = '192.168.1.83'
port = 40000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error Ocurred")
            client.close
            break

def write_messages():
    while True:
        message = f"{username}: {input('')}"
        if message == f'{username}: exit':
            client.close()
            sys.exit(0)
        elif message == f'{username}: exit':
            client.send("Una imagen será enviada jsakjskajsk")
        else:
            client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()