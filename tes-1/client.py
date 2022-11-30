import socket
import cv2
import time

c = socket.socket()
q = input('Enter IP address where you want o receive the image: ')
p = int(input("Enter port number: "))
r = input("Enter the extensionof the selected file (jpg - png - bmp)")
s = "pythonimage."+r
print(s)
condition = True
c.connect((q, p))
f = open(s, 'wb')
while condition:
    image = c.recv(1024)
    if str(image) == "b''":
        condition = False
    f.write(image)
