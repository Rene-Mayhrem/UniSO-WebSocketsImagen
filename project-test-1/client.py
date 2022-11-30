import socket
import threading
from tkinter import *
from tkinter import filedialog
import cv2

host = 'localhost'
port = 5555

username = input('Enter your username: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "@username":
                client.send(username.encode('utf-8'))
            elif "[CLIENT]" in message:
                print(message)
            else:
                file = open("pythonimage_client.jpg", 'wb')
                while True:
                    image = client.recv(1024)
                    if str(image) == "b''":
                        break;
                    file.write(image) 
        except:
            print("An error occurred")
            client.close()
            break;

def write_messages():
    while True:
        message = f"{username} : {input('')}"
        if 'exit' in message:
            message = "Nos vamos"
        elif 'image' in message:
            message = f"{username} usernames"
            client.send(message.encode('utf-8'))
            data_image = filedialog.askopenfile(initialdir="/")
            path = str(data_image.name)
            image = open(path, 'rb')
            for meta_data in image:
                client.send(meta_data)
        client.send(message.encode('utf-8'))


    

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()
