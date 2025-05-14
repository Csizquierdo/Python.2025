print ("*"*50)

import tkinter as tk
from PIL import ImageTk, Image#pip install pillow
import os
import random
billetera= 10000000
minimo_de_mesa = 100   
"""
def jugar_consola():
    global billetera
    numero = input ("ingrese un numero :")
    if not( numero.isdigit() and 2 <= int(numero) <=  12 ):
        print ("ingreso un numero no valido")
        print ("solo numeros de 1 y 12")
        return jugar_consola()
    numero = int (numero)
    apuesta = input ("ingrese su apuesta :")
    if not (apuesta.replace(".","").isdigit() and minimo_de_mesa <= float(apuesta) <=  billetera ):
        print ("ingreso una apuesta no validao")
        print (f"solo numeros de {minimo_de_mesa} y {billetera}")
        return jugar_consola() 
    apuesta = float (apuesta)
    dado1= random.randint(1,6)
    dado2= random.randint(1,6)
    print (f"salio {dado1} + {dado2} = {dado1+dado2}")
    if dado1+dado2 == numero:
        saldo = apuesta * 6
        print (f"Ganaste!!! ${saldo}")
    else:
        saldo = -apuesta 
        print (f"la proxima sera")
    
    billetera= billetera + saldo
    print (f"su saldo es {billetera}")

jugar_consola()
"""
def recargar():
    global billetera
    billetera += 500000
    ventana_cerrar_abrir(False)

def ventana_cerrar_abrir(estado):
    if estado is True:
        etiqueta2.place_forget()
        etiqueta3.place_forget()
        entrada_apuesta.place_forget()
        entrada_numero.place_forget()
        etiqueta4.config( text="su saldo es insuficiente")
        etiqueta5.config( text="recargue y siga jugando")
        botonJugar.place_forget()
        botonRecargar.place(y=400, height=30, x=50, width=100)

    else:
        
        etiqueta2.place(x=250, y=100 , width=160, height=30)
        etiqueta3.place(x=250, y=150 , width=160, height=30)
        entrada_numero.place(x=460, y=100 , width=90, height=25)
        entrada_apuesta.place(x=460, y=150 , width=90, height=25)
        etiqueta4.config( text="")
        etiqueta5.config( text="")
        botonRecargar.place_forget()
        botonJugar.place(y=400, height=30, x=50, width=100)
    etiqueta1.config(text=f"Su saldo es {billetera}.")
    return
        
        
def jugar_gui():
    global billetera
    if billetera < minimo_de_mesa:
        ventana_cerrar_abrir(True)
        return
    
    numero = entrada_numero.get()
    if not( numero.isdigit() and 2 <= int(numero) <=  12 ):
        etiqueta4.config( text="ingreso un numero no valido")
        etiqueta5.config( text="solo numeros de 1 s 12")
        return 
    numero = int (numero)

    apuesta = entrada_apuesta.get()
    if not (apuesta.replace(".","").isdigit() and minimo_de_mesa <= float(apuesta) <=  billetera ):
        etiqueta4.config( text="ingreso una apuesta no valida")
        etiqueta5.config( text=f"solo numeros de {minimo_de_mesa} y {billetera}")
        return 
    apuesta = float (apuesta)
    dado1= random.randint(1,6)
    dado2= random.randint(1,6)
    etiqueta4.config( text=f"salio {dado1} + {dado2} = {dado1+dado2}")
    if dado1+dado2 == numero:
        saldo = apuesta * 6
        etiqueta5.config( text=f"Ganaste!!! ${saldo}")
    else:
        saldo = -apuesta 
        etiqueta5.config( text="la proxima sera")
    
    billetera= billetera + saldo
    etiqueta1.config(text=f"Su saldo es {billetera}.")
        
def salir():
    print ("adios")
    exit()
    
    

    
    
    
    
    

##############################################################################################
'''                                                  'Programa principal'       '''
'''     creo el objeto GUI con el nombre ventana                                '''
ventana = tk.Tk()
ventana.title("jugando a los dados")
ventana.iconbitmap("icono.ico")
ventana.geometry("600x500")
ventana.resizable(width=False, height=False)
##############################################################################################
etiqueta1 = tk.Label(text=f"Su saldo es {billetera}.")
etiqueta1.config( bg="white", fg="blue",font=("Courier", 18))
etiqueta1.place(x=250, y=50 , width=300, height=30)


etiqueta2 = tk.Label(text="Numero.")
etiqueta2.config( bg="white", fg="blue",font=("Courier", 8))
etiqueta2.place(x=250, y=100 , width=160, height=30)

etiqueta3 = tk.Label(text="Apuesta")
etiqueta3.config( bg="white", fg="blue",font=("Courier", 8))
etiqueta3.place(x=250, y=150 , width=160, height=30)


etiqueta4 = tk.Label(text="")
etiqueta4.config( bg="white", fg="blue",font=("Courier", 10))
etiqueta4.place(x=10, y=300 , width=580, height=30)

etiqueta5 = tk.Label(text="")
etiqueta5.config( bg="white", fg="blue",font=("Courier", 10))
etiqueta5.place(x=10, y=350 , width=580, height=30)


etiqueta6 = tk.Label(text=" a jugar que la mesa esta caliente...")
etiqueta6.config( bg="white", fg="blue",font=("Courier", 18))
etiqueta6.place(x=10, y=250 , width=580, height=30)

img = Image.open("dados.jpg")
img = img.resize((190,190))
dados =  ImageTk.PhotoImage(img)
etiqueta_imagen = tk.Label(image=dados)
etiqueta_imagen.config( bg="blue")
etiqueta_imagen.place(x=10, y=10 , width=200, height=200)
##############################################################################################
entrada_numero = tk.Entry()
entrada_numero.place(x=460, y=100 , width=90, height=25)

entrada_apuesta = tk.Entry()
entrada_apuesta.place(x=460, y=150 , width=90, height=25)
##############################################################################################

botonJugar = tk.Button(text="Jugar", command=jugar_gui)
botonJugar.place(y=400, height=30, x=50, width=100)

botonSalir = tk.Button(text="Salir", command=salir)
botonSalir.place( x=490, width=100, height=30, y=400 )

botonRecargar = tk.Button(text="Recargar", command=recargar)
botonRecargar.place(y=400, height=30, x=50, width=100)
botonRecargar.place_forget()

ventana.mainloop()
##############################################################################################
exit()


