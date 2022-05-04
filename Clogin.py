
from tkinter import *
from tkinter import ttk
import socket
import threading

root = Tk()
root.geometry("400x600")
root.resizable(0,0)
root.title("Inicia sessió")

logo_clogin = PhotoImage(file="logo.png")
zoom = logo_clogin.subsample(7)
foto = Label(root, image=zoom)
foto.place(x=125, y=0)

nom_usuari = Label(root, text="Nom d'usuari", font=("Calibri", 18))
nom_usuari.place(x=125, y=150)

contrasenya = Label(root, text="Contrasenya", font=("Calibri", 18))
contrasenya.place(x=125, y=260)

inp_nom = ttk.Entry(root, font=("Calibri", 18), width=28)
inp_nom.place(x=30, y=200)

inp_contrasenya = ttk.Entry(root, font=("Calibri", 18), width=28)
inp_contrasenya.place(x=30, y=300)
inp_contrasenya.config(show="*")

imagen_singup = PhotoImage(file="singup.png")
img = imagen_singup.subsample(5)
boton_singup = Button(root, image=img, borderwidth=0)
boton_singup.place(x=125, y=370)

root.mainloop()