import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('172.26.49.191', 8000))
server.listen()

client_socket, client_address= server.accept()

file = open('server_image.jpg', 'wb')
image_chunk = client_socket.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)

print("File sent")

file.close()
client_socket.close()