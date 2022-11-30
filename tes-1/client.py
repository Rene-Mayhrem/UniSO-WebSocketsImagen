import socket
import cv2
import time

port = 5555

c = socket.socket()
q = input('Enter IP address where you want o receive the image: ')
s = "pythonimage_client.jpg"
print(s)
condition = True
c.connect((q, port))

f = open(s, 'wb')
while condition:
    image = c.recv(1024)
    if str(image) == "b''":
        condition = False
    f.write(image)

