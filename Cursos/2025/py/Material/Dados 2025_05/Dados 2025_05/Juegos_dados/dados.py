print ("*"*50)
print ("""Ejercicio
generar un número aleatorio de 1 al 6 (simulábamos el arrojar un dado),
debemos pasarlo a una aplicación deescritorio. La vista de la aplicación debería
ser similar a:

En la caja deberían de aparecer los salidas aleatorios cada vez que se presióna el botón.
Antes de mostrar los salidas se limpia la caja, dejando el mismo salida hasta que se vuelve a pulsar.
Ayuda:
Si tenemos una “caja” generada con tk.Entry()
● caja.delete(0,tk.END) llamada desde cualquier función limpia la “caja”.
● caja.insert(0,variable) llamada desde cualquier función inserta el valor de variable en la “caja”.""" )

import tkinter as tk#<----<-----<----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca tkinter y le damos el  Alias de tk                                 '''
from PIL import ImageTk, Image# <----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca PILLOW pip install pillow solo ImageTk, Image                                            '''
import os#<----<-----<----<-----<----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca os (operative system)                                              '''
import random#  <----<-----<----<-----<----<-----<----<-----<----
'''                                                             importamos la biblioteca random (aleatoriedad)                                              '''

'''                                                     defino la función jugar q sera usada al cliquear el boton 'botonJugar'                                      '''
def jugar():
    global billetera
    '''                                                 en la variable tirada guardo un numero random(al azar..o casi) entre 0 y 6                          '''
    tirada = random.randint(1,6)
    '''                                                 tome el nombre de la caja de texto u lo guardo en nombre                                            '''
    nombre=caja_nombre.get()
    '''                                                 condición nombre esta vacio      '''
    
    numero=caja_numero.get()
    apuesta = caja_apuesta.get()

    if not (numero.isdigit() and int(numero) >0 and int(numero) <=6) :
        salida.config(text=f"numero no valido")
        caja_numero.delete(0,tk.END)
        return
    else:
        numero = int(numero)
    if not (apuesta.replace(".","").isdigit() and float(apuesta) >0 and float(apuesta) <=billetera) :
        salida.config(text=f"apuesta no valida")
        caja_apuesta.delete(0,tk.END)
        return
    else:
        apuesta = float(apuesta)     
     
    
        '''                                                 No True > False
                                                            piso nombre con el contenido anterior de nombre tras ejecutar el metodo upper (mayusculas)      '''
    caja_nombre.delete(0,tk.END)
    caja_nombre.insert(0,"")
    nombre = nombre.upper()

            
    if numero == tirada:
        billetera += (apuesta *5)
        string = f"genial {nombre} ganastes {apuesta*5}..."
    else:
        billetera -= apuesta
        string = f"{nombre} la proxima sera ..."
        
    etiqueta.config(text=f"tu saldo es {billetera}")
        
        
        
    '''                                                 En la etiqueta salida ingreso el texto genial y el nombre o !!!!! en caso de estar vacio            '''
    salida.config(text=f"{string}")
    '''                                                 En la etiqueta resultado ingreso el texto 'En la tirada salio' y el contenido de la variable tirada '''
    resultado.config(text=f"En la tirada salio {tirada}")
'''                                             defino la función salir q sera usada al cliquear el boton 'botonSalir'                                      '''
def salir():
    '''                                                   termino el programa                                                                                 '''
    exit()
##############################################################################################
billetera = 1000000
'''                                                  'Programa principal'                                                                                   '''
'''     creo el objeto GUI con el nombre ventana                                                                                                            '''
ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
'''     le doy al obje "!!!!!"to ventana el nombre de jugando a los dados'''
ventana.title("jugando a los dados")
'''     dimenciónamos el objeto ventana en 600 x 500 px                                                                                                     '''
ventana.config(bg="white")
ventana.geometry("600x500")
##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el nombre botonjugar con el texto 'Jugar'
        y si es clickeado debe ejecutar la función jugar
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la finción)                                                 '''
botonJugar = tk.Button(text="Jugar", command=jugar)# lambda 
'''     ubico el objeto 'botonJugar, en x=50 e y = 50
        doy un tamaño al objeto 'botonJugar,  width=100(ancho), height=30(alto)                                                                             '''
botonJugar.place(x=100, y=420, width=100, height=30)
##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el nombre botonSalir con el texto 'Salir'
        y si es clickeado debe ejecutar la función salir
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la función)                                                 '''
botonSalir = tk.Button(text="Salir", command=salir)
'''     ubico el objeto 'botonSalir, en x=50 e y = 50
        doy un tamaño al objeto 'botonSalir,  width=100(ancho), height=30(alto)                                                                             '''
botonSalir.place(x=400, y=420, width=100, height=30)
##############################################################################################
'''     creo el objeto img de la biblioteca 'PIL Image' dandole en nombre de la imagen "dados.jpg"
        que debe estar en la misma carpeta que el script python'                                                                                            '''
img = Image.open("dados.jpg")
'''     doy atributos al objeto img (tamaño)                                                                                                                '''
img = img.resize((200,200))
'''     creo el objeto dados de la biblioteca PIL 'ImageTk.PhotoImage' pasandole el objeto img como parametro                                               '''
dados =  ImageTk.PhotoImage(img)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "lab_im"  paso el parametro de image = objeto dados                                 '''
lab_im = tk.Label(image=dados)
'''     doy al objeto "Label" "lab_im" ubicación y tamaño                                                                                                   '''
lab_im.place(x=10, y=10, width=200, height=200)#.pack()
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta"  paso el parametro de text = " a jugar..."                               '''
etiqueta = tk.Label(text=f"tu saldo es {billetera}")
'''     con al objeto "Label" "etiqueta", configuro el color de fondo "bg" color de fuente "fg" fuente y tamaño "font=("Courier", 24)"                      '''
etiqueta.config( bg="#ffffff", fg="blue",font=("Courier", 18))
'''     doy al objeto "Label" "etiqueta" ubicación y tamaño                                                                                                 '''
etiqueta.place(x=100, y=380, width=400, height=30)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_nombre"  paso el parametro de text = " Ingresa tu nombre"                 '''
etiqueta_nombre = tk.Label(text="Ingresa tu nombre", bg="white")
'''     doy al objeto "Label" "etiqueta_nombre" ubicación. dejo el tamaño en defauld para q se calcule a partir del text                                    '''
etiqueta_nombre.place(x=200, y=75)
##############################################################################################
'''     creo el objeto Entry de la biblioteca 'tk' dandole en nombre de "caja_nombre" para que el usuario ingrese sus datos                                 '''
caja_nombre = tk.Entry()
'''     doy al objeto "Entry" "caja_nombre" la ubicación y tamaño                                                                                           '''
caja_nombre.place(x=320, y=75 , width=100, height=25)
##############################################################################################
etiqueta_apuesta = tk.Label(text="Ingresa tu apuesta", bg="white")
etiqueta_apuesta.place(x=200, y=125 , width=100, height=25)
##############################################################################################
caja_apuesta = tk.Entry()
caja_apuesta.place(x=320, y=125 , width=100, height=25)
##############################################################################################
etiqueta_numero = tk.Label(text="Ingresa tu número", bg="white")
etiqueta_numero.place(x=200, y=175 , width=100, height=25)
##############################################################################################       
caja_numero = tk.Entry()
caja_numero.place(x=320, y=175 , width=100, height=25)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "salida"  paso el parametro de text = ""(vacio)                                     '''
salida = tk.Label(text="")
'''     con al objeto "Label" "salida", configuro fuente y tamaño "font=("Courier", 24)"                                                                    '''
salida.config(font=("Courier", 12), bg="white")
'''     doy al objeto "Label" "salida" ubicación y tamaño                                                                                                   '''
salida.place(x=100, y=225, width=400, height=30)

##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "resultado"  paso el parametro de text = ""(vacio)                                  '''
resultado = tk.Label(text="")
'''     con al objeto Label "resultado", configuro fuente y tamaño "font=("Courier", 24)"                                                                   '''
resultado.config(font=("Courier", 12), bg="white")
'''     doy al objeto "Label" "resultado" ubicación y tamaño                                                                                                '''
resultado.place(x=100, y=325 , width=400, height=30)
##############################################################################################
'''     cierro el loop de pantalla'''
ventana.mainloop()




