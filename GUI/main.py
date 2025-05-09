import tkinter as tk

root=tk.Tk()
root.title("Sistema de Gestion")
root.geometry("600x400")





titulo=tk.Label(root, text="Bienvenido a nuestro Sistema Gestion Tienda", font=("Times New Roman", 15))
titulo.pack(pady=10)


boton= tk.Button(root, text="Gestion de Productos")
boton.pack()







root.mainloop() 