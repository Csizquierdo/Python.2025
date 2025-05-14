print ("*"*50)

from datetime import datetime, date, timedelta
import tkinter as tk#<----<-----<----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca tkinter y le damos el  Alias de tk                                 '''
# ~ from tkinter import ttk
try:
    from PIL import ImageTk, Image# <----<-----<----<-----<----<-----
    '''                                                             importamos la biblioteca PIL solo ImageTk, Image '''
except Exception as error_:
    import pip
    pip.main(['install', 'pillow'])
    from PIL import ImageTk, Image

import os
import random
billetera = 1000000
salidas=[]
salidas_dic = {}
def jugar_consola():
    print("·"*50)
    global billetera
    numero = input("ingrese un numero a jugar entre 2 a 12:")
    if not (numero.isdigit() and int(numero)>= 2 and int(numero)<= 12):
        print(f"numero {numero} no valido")
        print("se aceptan entre 2 y 12")
        return
    numero = int (numero)
    apuesta = input(f"ingrese su apuesta entre 10 a {billetera}:")
    if not (apuesta.replace(".","").isdigit() and  float(apuesta) >=  10 and  float(apuesta) <=  billetera):
        print(f"apuesta {apuesta} no valida")
        print(f"se aceptan entre 10 y {billetera}")
        return
    apuesta= float(apuesta)
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    print (f"salio {dado_1=} + {dado_2=}   = {dado_1+dado_2}")
    if (dado_1+dado_2)==numero:
        saldo = apuesta * 10
        print (f"ganaste {saldo}")
    else:
        saldo = -apuesta
        print ("la proxima ganas seguro")
    salidas.append(dado_1+dado_2)

    if (dado_1+dado_2) not in salidas_dic.keys():
        salidas_dic[dado_1+dado_2]=1
    else:
        salidas_dic[dado_1+dado_2]+=1
    billetera += saldo # billetera = billetera + saldo
    print (f"su saldo es {billetera}                {salidas}      {salidas_dic} ")

# ~ while True:
    # ~ jugar_consola()
##########################################################################
def jugar():
    print("·"*50)
    global billetera
    if billetera < 10:
        etiqueta5.config(text=f"tu saldo es {billetera}")
        etiqueta6.config(text=f"no te alcanza")
        etiqueta2.place_forget()
        etiqueta3.place_forget()
        etiqueta4.place_forget()
        entrada_apuesta.place_forget()
        entrada_numero.place_forget()
        botonJugar.place_forget()
        botonrecarga.place(x=50, y=450, width=100, height=30)
        return



    numero=entrada_numero.get()
    if not (numero.isdigit() and int(numero)>= 2 and int(numero)<= 12):
        etiqueta5.config(text=f"numero {numero} no valido")
        etiqueta6.config(text="se aceptan entre 2 y 12")
        entrada_numero.delete(0,tk.END)
        return
    numero = int (numero)
    apuesta=entrada_apuesta.get()
    if not (apuesta.replace(".","").isdigit() and  float(apuesta) >=  10) and  float(apuesta) <=  billetera:
        etiqueta5.config(text=f"apuesta {apuesta} no valida")
        etiqueta6.config(text=f"se aceptan entre 10 y {billetera}")
        entrada_apuesta.delete(0,tk.END)
        return
    apuesta= float(apuesta)
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    etiqueta5.config(text=f"salio {dado_1=} + {dado_2=}   = {dado_1+dado_2}")
    if (dado_1+dado_2)==numero:
        saldo = apuesta * 10
        etiqueta6.config(text= f"ganaste {saldo}")
    else:
        saldo = -apuesta
        etiqueta6.config(text= "la proxima ganas seguro")
    billetera += saldo # billetera = billetera + saldo

    salidas.append(dado_1+dado_2)
    if (dado_1+dado_2) not in salidas_dic.keys():
        salidas_dic[dado_1+dado_2]=1
    else:
        salidas_dic[dado_1+dado_2]+=1
    etiqueta1.config(text=f"su saldo es $ {billetera}")
    print (f"su saldo es {billetera}                {salidas}      {salidas_dic} ")

##############################################################################################
def salir():
    exit()
##############################################################################################
def recargar_saldo():
    global  billetera
    print ("la proxima")
    billetera += 500000
    etiqueta1.config(text=f"su saldo es $ {billetera}")
    etiqueta2.place(x=260, y=60, width=150, height=30)
    entrada_numero.place(x=430, y=60 , width=120, height=25)
    etiqueta3.place(x=260, y=110, width=150, height=30)
    entrada_apuesta.place(x=430, y=110 , width=120, height=25)
    etiqueta4 = tk.Label(text=" a jugar ...")
    etiqueta4.place(x=50, y=250, width=500, height=30)
    etiqueta5.config(text="Saldo recargado")
    etiqueta5.place(x=50, y=300, width=500, height=30)
    etiqueta6.config(text="a recuperar lo perdido")
    etiqueta6.place(x=50, y=350, width=500, height=30)
    botonJugar.place(x=50, y=450, width=100, height=30)
    botonrecarga.place_forget()

##############################################################################################
'''     creo el objeto GUI con el nombre ventana                                '''
ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
ventana.title("jugando a los dados")
ventana.iconbitmap("icono.ico")
ventana.geometry("600x500")
ventana.config( bg="white")
ventana.resizable(width=False, height=False)
##############################################################################################
etiqueta1 = tk.Label(text=f"su saldo es {billetera}")
etiqueta1.config( bg="white", fg="green",font=("Arial", 12))
etiqueta1.place(x=260, y=10, width=290, height=30)
##############################################################################################
etiqueta2 = tk.Label(text="Su numero es :")
etiqueta2.config( bg="white", fg="#770BFE",font=("Arial", 12))
etiqueta2.place(x=260, y=60, width=150, height=30)
#---------------------------------------------------------------------------------------------
entrada_numero = tk.Entry()
entrada_numero.place(x=430, y=60 , width=120, height=25)
##############################################################################################
etiqueta3 = tk.Label(text="Su apuesta es :")
etiqueta3.config( bg="white", fg="#770BFE",font=("Arial", 12))
etiqueta3.place(x=260, y=110, width=150, height=30)
#---------------------------------------------------------------------------------------------
entrada_apuesta = tk.Entry()
entrada_apuesta.place(x=430, y=110 , width=120, height=25)
##############################################################################################
etiqueta4 = tk.Label(text=" a jugar ...")
etiqueta4.config( bg="white", fg="blue",font=("Arial", 16))
etiqueta4.place(x=50, y=250, width=500, height=30)
##############################################################################################
etiqueta5 = tk.Label(text="")
etiqueta5.config( bg="white", fg="#E000FF",font=("Arial", 16))
etiqueta5.place(x=50, y=300, width=500, height=30)
##############################################################################################
etiqueta6 = tk.Label(text="")
etiqueta6.config( bg="white", fg="#E000FF",font=("Arial", 16))
etiqueta6.place(x=50, y=350, width=500, height=30)
##############################################################################################
img = Image.open("dados.jpg")
img = img.resize((190,190))
dados =  ImageTk.PhotoImage(img)
etiqueta_imagen = tk.Label(image=dados)
etiqueta_imagen.config( bg="blue")
etiqueta_imagen.place(x=10, y=10, width=200, height=200)
##############################################################################################
botonJugar = tk.Button(text="Jugar", command=jugar)
botonJugar.place(x=50, y=450, width=100, height=30)
##############################################################################################
botonSalir = tk.Button(text="Salir", command=salir)
botonSalir.place(x=450, y=450, width=100, height=30)
##############################################################################################
botonrecarga = tk.Button(bg="red",text="recargar saldo", command=recargar_saldo)
botonrecarga.place(x=50, y=450, width=100, height=30)
botonrecarga.place_forget()
##############################################################################################
ventana.mainloop()
