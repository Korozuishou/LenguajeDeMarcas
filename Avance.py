from tkinter import *
from tkinter import ttk
import pyzbar.pyzbar as pyzbar
import cv2
import os
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
from pyzbar.pyzbar import decode, ZBarSymbol
import numpy as np
import sys
import os
from PIL import Image, ImageTk, ImageDraw
import time



class App:
        
    def __init__(self, statWindow):
        statWindow.title("View Statistics")
        statWindow.config(bg = "grey")
        statWindow.geometry('800x900')

        

        self.searched = StringVar()
        searchBox = Entry(statWindow, textvariable=self.searched)
        searchBox.place(x= 1350, y=750, width = 450, height = 200)
        
        
        delayImagen= ttk.Entry(root)  # DELAY el de mitad pantalla
        delayImagen.place(x=1350, y=690)# Posicionarla en la ventana.
        
        ######## FUNCION CONVERSOR STR A INT  PARA DELAY ######
        def conversionInt(delayImagen):
                tiempoImagen = delayImagen.get()
                try:
                        return int(tiempoImagen)
                except ValueError:
                        print ("error")
                        return None
        
        ######## FIN FUNCION CONVERSOR STR A INT  PARA DELAY ######

        def handler(e):
                enterButton = Button(statWindow, text ="CLICK", command= lambda: (searchButton(self), searchBox.delete(0,'end')))
                enterButton.config(height = 1, width = 4)
                #enterButton.place(x=652, y=50)
                root.bind('<Return>',lambda event=None: enterButton.invoke())    
        root.bind('<Return>',handler)

        
        imagenPequeña = ttk.Entry(root)  # IMAGEN PEQUEÑA
        imagenPequeña.place(x=1350, y=100, width=450, height=450) # Posicionarla en la ventana.

                

######### BUSCAR #########
        def searchButton(self):
                
                text = self.searched.get()
                print(text)
                f = open("text.txt", "a")
                f.write(text + os.linesep)
        ######### APERTURA RUTA DE IMAGEN #########
                f = open("text.txt",'r+')
                image1 = Image.open(text)
        ######### REDIMENSIONAR #########
                image1 = image1.resize((960,860),Image.ANTIALIAS)
                test = ImageTk.PhotoImage(image1)
                label1 = ttk.Label(image=test)
                label1.image = test
        ######### POSICION #########
                label1.place(x=100, y=100)

        ######### DELAY #########
                tiempoImagen =  conversionInt(delayImagen)
                time.sleep(int(tiempoImagen))
        ######### FIN DELAY #########        
                
        
       

        
        
######### POSICION #########
root = Tk()
app = App(root)
root.mainloop()
