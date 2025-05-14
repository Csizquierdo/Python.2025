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
billetera =100000
'''                                             defino la función jugar q sera usada al cliquear el boton 'botonJugar'                                      '''
def jugar():
    '''                                                 en la variable tirada guardo un numero random(al azar..o casi) entre 0 y 6                          '''
    tirada = random.randint(1,6)
    '''                                                 tome el nombre de la caja de texto u lo guardo en nombre                                            '''
    nombre=caja_nombre.get()
    '''                                                 condición nombre esta vacio                                                                         '''
    if nombre == "" or nombre == "Juguemos":
        '''                                                 True  pongo !!!!!                                                                               '''
        nombre = "!!!!!"
    else:
        '''                                                 No True > False
                                                            piso nombre con el contenido anterior de nombre tras ejecutar el metodo upper (mayusculas)      '''
        caja_nombre.delete(0,tk.END)
        caja_nombre.insert(0,"Juguemos")
        nombre = nombre.upper()
    '''                                                 En la etiqueta salida ingreso el texto genial y el nombre o !!!!! en caso de estar vacio            '''
    salida.config(text=f"genial {nombre}")
    '''                                                 En la etiqueta resultado ingreso el texto 'En la tirada salio' y el contenido de la variable tirada '''
    numero = int(caja_numero.get())
    global billetera
    if numero==tirada:
        resultado.config(text=f"En la tirada salio {tirada} ganastes")
        billetera+=float(caja_apuesta.get())*5

    else:
        resultado.config(text=f"En la tirada salio {tirada} la proxima sera")
        billetera-=float(caja_apuesta.get())
    etiq_billetera.config(text=f"su saldo es {billetera}")


'''                                             defino la función salir q sera usada al cliquear el boton 'botonSalir'                                      '''
def salir():
    '''                                                   termino el programa                                                                                 '''
    exit()
##############################################################################################
'''                                                  'Programa principal'                                                                                   '''
'''     creo el objeto GUI con el nombre ventana                                                                                                            '''
ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
'''     le doy al obje "!!!!!"to ventana el nombre de jugando a los dados'''
ventana.title("jugando a los dados")
'''     dimenciónamos el objeto ventana en 600 x 500 px                                                                                                     '''
ventana.geometry("600x500")
##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el nombre botonjugar con el texto 'Jugar'
        y si es clickeado debe ejecutar la función jugar
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la finción)                                                 '''
botonJugar = tk.Button(text="Jugar", command=jugar)
'''     ubico el objeto 'botonJugar, en x=50 e y = 50
        doy un tamaño al objeto 'botonJugar,  width=100(ancho), height=30(alto)                                                                             '''
botonJugar.place(x=50, y=400, width=100, height=30)
##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el nombre botonSalir con el texto 'Salir'
        y si es clickeado debe ejecutar la función salir
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la función)                                                 '''
botonSalir = tk.Button(text="Salir", command=salir)
'''     ubico el objeto 'botonSalir, en x=50 e y = 50
        doy un tamaño al objeto 'botonSalir,  width=100(ancho), height=30(alto)                                                                             '''
botonSalir.place(x=450, y=400, width=100, height=30)
##############################################################################################
'''     creo el objeto img de la biblioteca 'PIL Image' dandole en nombre de la imagen "dados.jpg"
        que debe estar en la misma carpeta que el script python'                                                                                            '''
img = Image.open("dados.jpg")
'''     doy atributos al objeto img (tamaño)                                                                                                                '''
img = img.resize((100,100), Image.ANTIALIAS)
'''     creo el objeto dados de la biblioteca PIL 'ImageTk.PhotoImage' pasandole el objeto img como parametro                                               '''
dados =  ImageTk.PhotoImage(img)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "lab_im"  paso el parametro de image = objeto dados                                 '''
lab_im = tk.Label(image=dados)
'''     doy al objeto "Label" "lab_im" ubicación y tamaño                                                                                                   '''
lab_im.place(x=10, y=10, width=100, height=100)#.pack()

##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta"  paso el parametro de text = " a jugar..."                               '''
etiqueta = tk.Label(text=" a jugar...")
'''     con al objeto "Label" "etiqueta", configuro el color de fondo "bg" color de fuente "fg" fuente y tamaño "font=("Courier", 24)"                      '''
etiqueta.config( bg="black", fg="red",font=("Courier", 24))
'''     doy al objeto "Label" "etiqueta" ubicación y tamaño                                                                                                 '''
etiqueta.place(x=210, y=290)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta"  paso el parametro de text = " a jugar..."                               '''
etiq_billetera = tk.Label(text=f"su saldo es {billetera}")
'''     con al objeto "Label" "etiqueta", configuro el color de fondo "bg" color de fuente "fg" fuente y tamaño "font=("Courier", 24)"                      '''
etiq_billetera.config( bg="black", fg="red",font=("Courier", 24))
'''     doy al objeto "Label" "etiqueta" ubicación y tamaño                                                                                                 '''
etiq_billetera.place(x=100, y=10)


##############################################################################################
'''     creo el objeto Entry de la biblioteca 'tk' dandole en nombre de "caja_nombre" para que el usuario ingrese sus datos                                 '''
caja_nombre = tk.Entry()
'''     doy al objeto "Entry" "caja_nombre" la ubicación y tamaño                                                                                           '''
caja_nombre.place(x=320, y=75 , width=100, height=25)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_nombre"  paso el parametro de text = " Ingresa tu nombre"                 '''
etiqueta_nombre = tk.Label(text="Ingresa tu nombre")
'''     doy al objeto "Label" "etiqueta_nombre" ubicación. dejo el tamaño en defauld para q se calcule a partir del text                                    '''
etiqueta_nombre.place(x=200, y=75)

##############################################################################################
'''     creo el objeto Entry de la biblioteca 'tk' dandole en numero de "caja_numero" para que el usuario ingrese sus datos                                 '''
caja_numero = tk.Entry()
'''     doy al objeto "Entry" "caja_numero" la ubicación y tamaño                                                                                           '''
caja_numero.place(x=320, y=125 , width=100, height=25)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en numero de "etiqueta_numero"  paso el parametro de text = " Ingresa tu numero"                 '''
etiqueta_numero = tk.Label(text="Ingresa tu numero")
'''     doy al objeto "Label" "etiqueta_numero" ubicación. dejo el tamaño en defauld para q se calcule a partir del text                                    '''
etiqueta_numero.place(x=200, y=125)
##############################################################################################
'''     creo el objeto Entry de la biblioteca 'tk' dandole en apuesta de "caja_apuesta" para que el usuario ingrese sus datos                                 '''
caja_apuesta = tk.Entry()
'''     doy al objeto "Entry" "caja_apuesta" la ubicación y tamaño                                                                                           '''
caja_apuesta.place(x=320, y=175 , width=100, height=25)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en apuesta de "etiqueta_apuesta"  paso el parametro de text = " Ingresa tu apuesta"                 '''
etiqueta_apuesta = tk.Label(text="Ingresa tu apuesta")
'''     doy al objeto "Label" "etiqueta_apuesta" ubicación. dejo el tamaño en defauld para q se calcule a partir del text                                    '''
etiqueta_apuesta.place(x=200, y=175)

##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "salida"  paso el parametro de text = ""(vacio)                                     '''
salida = tk.Label(text="")
'''     con al objeto "Label" "salida", configuro fuente y tamaño "font=("Courier", 24)"                                                                    '''
salida.config(font=("Courier", 24))
'''     doy al objeto "Label" "salida" ubicación y tamaño                                                                                                   '''
salida.place(x=230, y=190)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "resultado"  paso el parametro de text = ""(vacio)                                  '''
resultado = tk.Label(text="")
'''     con al objeto Label "resultado", configuro fuente y tamaño "font=("Courier", 24)"                                                                   '''
resultado.config(font=("Courier", 24))
'''     doy al objeto "Label" "resultado" ubicación y tamaño                                                                                                '''
resultado.place(x=25, y=230)
##############################################################################################


'''     cierro el loop de pantalla'''
ventana.mainloop()




