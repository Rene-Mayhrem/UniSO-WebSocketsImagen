import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.26.49.191', 8000))

file = open('shrek.jpg', 'rb')
image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)

file.close ()
client.close()