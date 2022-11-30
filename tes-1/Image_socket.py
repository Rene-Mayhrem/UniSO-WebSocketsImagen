import tkinter
from tkinter import *
from tkinter import filedialog
import socket
import cv2
from PIL import Image, ImageOps


data = filedialog.askopenfile(initialdir="/")
path = str(data.name)
pic = cv2.imread(path)
(B, G, R) = cv2.split(pic)


def edge_img():
    pic_1 = cv2.Canny(pic, 100, 200)
    final_pic = Image.open(pic_1)
    final_pic.save('pythonimage.jpg')

def bgr2rgb_img():
    pic_2 = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
    final_pic = Image.open(pic_2)
    final_pic.save('pythonimage.jpg')

def print_menu():
    print ('2 -- Option 2: Margenes' )
    print ('3 -- Option 3: BGR a RGB' )
    print ('4 -- Exit' )

def menu():
    print_menu()
    opc = int(input("Selecciona filtro: "))
    while True:
        if opc == 2:
            edge_img()
            break
        if opc == 3:
            bgr2rgb_img()
            break
        if opc == 4:
            break

menu()



c = 0
port = 5555
q1 = input('IP address: ')
q2 = port
s = socket.socket()
s.bind((q1,  port))

image = open('pythonimage.jpg', 'rb')
s.listen()
c, address = s.accept()
if c!= 0:
    for i in image:
        c.send(i)

