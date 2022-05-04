from tkinter import *
from tkinter import ttk
import socket
import threading

root = Tk()
root.geometry("400x600")
root.resizable(0,0)
root.title("Inicia sessió")
root.config(bg="#ccdadd")

logo_clogin = PhotoImage(file="logo.png")
zoom = logo_clogin.subsample(7)
foto = Label(root, image=zoom, bg="#ccdadd")
foto.place(x=125, y=0)

nom_usuari = Label(root, text="Nom d'usuari", font=("Calibri", 18), bg="#ccdadd")
nom_usuari.place(x=128, y=150)

contrasenya = Label(root, text="Contrasenya", font=("Calibri", 18), bg="#ccdadd")
contrasenya.place(x=130, y=260)

inp_nom = ttk.Entry(root, font=("Calibri", 18), width=28)
inp_nom.place(x=28, y=200)

inp_contrasenya = ttk.Entry(root, font=("Calibri", 18), width=28)
inp_contrasenya.place(x=28, y=300)
inp_contrasenya.config(show="*")

imagen_singup = PhotoImage(file="singup.png")
imgagen_singup = imagen_singup.subsample(5)
boton_singup = Button(root, image=imgagen_singup, borderwidth=0, bg="#ccdadd", cursor="hand2")
boton_singup.place(x=125, y=370)

lab_register = Label(root, text="No tens compte", font=("Calibri", 14, "underline"), bg="#ccdadd")
lab_register.place(x=50, y=530)

foto_register = PhotoImage(file="register.png")
foto_register = foto_register.subsample(2)
button_register = Button(root, image=foto_register, bg="#ccdadd",borderwidth=0)
button_register.place(x=175, y=510)


root.mainloop()