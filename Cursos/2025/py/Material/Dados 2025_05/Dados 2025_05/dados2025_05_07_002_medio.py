print ("*"*50)





from datetime import datetime, date, timedelta


import tkinter as tk
# ~ from tkinter import ttk
try:
    from PIL import ImageTk, Image
except Exception as error_:
    import pip
    pip.main(['install', 'pillow'])
    from PIL import ImageTk, Image


import os
import random
def jugar():
    global billetera
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    numero = ingreso_numero.get()
    if not (numero.isdigit() and  int(numero)>=2 and  int(numero)<=12):
        etiqueta2.config(text ="solo numeros")
        etiqueta3.config(text ="entre 2 y 12")
        return
    apuesta = ingreso_apuesta.get()
    if not (apuesta.isdigit() and  int(apuesta)<=billetera):
        etiqueta2.config(text ="su apuesta no es aceptada")
        etiqueta3.config(text =f"maximo {billetera}")
        return
    numero = int (numero)
    apuesta = int (apuesta)
    
    etiqueta2.config(text =f"salio {dado1} + {dado2} = {dado1+dado2}")
    if numero == dado1+dado2:
        saldo = apuesta * 10
        etiqueta3.config(text =f"ganaste")
    else:
        etiqueta3.config(text =f"la proxima segura ganas")
        saldo = - apuesta 
    billetera = billetera + saldo
   
    etiqueta4.config(text=f"su saldo es {billetera}")



def salir():
    '''                                                 termino el programa                                                                                 '''
    exit()

billetera = 1000000
ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias

ventana.title("jugando a los dados")

ventana.config( bg="white")
ventana.iconbitmap("icono.ico")
ventana.geometry("600x500")
ventana.resizable(width=False, height=False)
##############################################################################################
etiqueta1 = tk.Label(text=" a jugar que la mesa esta caliente ...")
etiqueta1.config( bg="white", fg="blue",font=("Courier", 16))
etiqueta1.place(x=10, y=280 ,width=580, height=30)


etiqueta2 = tk.Label(text="")
etiqueta2.config( bg="white", fg="blue",font=("Courier", 16))
etiqueta2.place(x=10, y=330 ,width=580, height=30)


etiqueta3 = tk.Label(text="")
etiqueta3.config( bg="white", fg="blue",font=("Courier", 16))
etiqueta3.place(x=10, y=380 ,width=580, height=30)



etiqueta4 = tk.Label(text=f"su saldo es {billetera}")
etiqueta4.config( bg="white", fg="blue",font=("Courier", 16))
etiqueta4.place(x=250, y=30 ,width=300, height=30)




etiqueta5 = tk.Label(text=f"Numero:")
etiqueta5.config( bg="white", fg="blue",font=("Courier", 16))
etiqueta5.place(x=250, y=80 ,width=200, height=30)




etiqueta6 = tk.Label(text=f"Apuesta:")
etiqueta6.config( bg="white", fg="blue",font=("Courier", 16))
etiqueta6.place(x=250, y=130 ,width=200, height=30)


img = Image.open("dados.jpg")
img = img.resize((190,190))
img_dados =  ImageTk.PhotoImage(img)

etiqueta_imagen = tk.Label(image=img_dados)
etiqueta_imagen.config( bg="blue")
etiqueta_imagen.place(x=10, y=10 ,width=200, height=200)



##############################################################################################

ingreso_numero = tk.Entry()
ingreso_numero.place(x=500, y=80 , width=50, height=25)



ingreso_apuesta = tk.Entry()
ingreso_apuesta.place(x=500, y=130 , width=50, height=25)

# ~ ##############################################################################################

botonJugar = tk.Button(text="Jugar", command=jugar)
botonJugar.place(x=150, y=450, width=100, height=30)
##############################################################################################
botonSalir = tk.Button(text="Salir", command=salir)
botonSalir.place(x=350, y=450, width=100, height=30)
##############################################################################################
   
ventana.mainloop()




