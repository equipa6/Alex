from tkinter import *
import socket
import threading

root = Tk()
root.geometry("600x300")
root.resizable(0,0)
root.title("Inicia sessió")

nom_empresa = Label(root, text="CLOGIN", font=("Calibri", 30))
nom_empresa.place(x=240, y=0)

nom_usuari = Label(root, text="Nom d'usuari", font=("Calibri", 20))
nom_usuari.place(x=10, y=90)

contrasenya = Label(root, text="Contrasenya", font=("Calibri", 20))
contrasenya.place(x=10, y=160)

root.mainloop()