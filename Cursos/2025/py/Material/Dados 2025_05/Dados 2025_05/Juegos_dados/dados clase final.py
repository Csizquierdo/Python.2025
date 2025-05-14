print ("*"*50)
print ("""Ejercicio
generar un número aleatorio de 1 al 6 (simulábamos el arrojar un dado),
debemos pasarlo a una aplicación deescritorio. La vista de la aplicación debería
ser similar a:

En la caja deberían de aparecer los etiqueta_info_salida_3s aleatorios cada vez que se presióna el botón.
Antes de mostrar los etiqueta_info_salida_3s se limpia la caja, dejando el mismo etiqueta_info_salida_3 hasta que se vuelve a pulsar.
Ayuda:
Si tenemos una “caja” generada con tk.Entry()
● caja.delete(0,tk.END) llamada desde cualquier función limpia la “caja”.
● caja.insert(0,variable) llamada desde cualquier función inserta el valor de variable en la “caja”.""" )

import tkinter as tk#<----<-----<----<-----<----<-----<----<-----
''' pip install pillow                                                            importamos la biblioteca tkinter y le damos el  Alias de tk'''
from PIL import ImageTk, Image# <----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca PILLOW pip install pillow solo ImageTk, Image'''
import os#<----<-----<----<-----<----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca os (operative system)'''
import random#  <----<-----<----<-----<----<-----<----<-----<----
'''                                                             importamos la biblioteca random (aleatoriedad)'''

'''                                                     defino la función jugar q sera usada al cliquear el boton_accion_ 'boton_accion_Jugar'''
def jugar():
    '''                                                 en la variable tirada guardo un numero random(al azar..o casi) entre 0 y 6'''
    tirada = random.randint(1,6)
    '''                                                 tome el nombre de la caja de texto u lo guardo en nombre'''
    nombre=caja_info_entrada_0.get()
    '''                                                 condición nombre esta vacio '''
    if nombre == "" or nombre == "Juguemos":
        '''                                                 True  pongo !!!!! '''
        nombre = "!!!!!"
    else:
        '''                                                 No True > False
                                                            piso nombre con el contenido anterior de nombre tras ejecutar el metodo upper (mayusculas)'''
        caja_info_entrada_0.delete(0,tk.END)
        caja_info_entrada_0.insert(0,"Juguemos")
        nombre = nombre.upper()
    '''                                                 En la etiqueta_info_salida_0 etiqueta_info_salida_3 ingreso el texto genial y el nombre o !!!!! en caso de estar vacio'''
    etiqueta_info_salida_3.config(text=f"genial {nombre}")
    '''                                                 En la etiqueta_info_salida_0 etiqueta_info_salida_4 ingreso el texto 'En la tirada salio' y el contenido de la variable tirada '''
    etiqueta_info_salida_4.config(text=f"En la tirada salio {tirada}")


'''                                                       defino la función salir q sera usada al cliquear el boton_accion_ 'boton_accion_Salir'''
def salir():
    '''                                                   termino el programa '''
    exit()
##############################################################################################
'''                                                  'Programa principal' '''
'''     creo el objeto GUI con el nombre ventana'''
ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
'''     le doy al obje "!!!!!"to ventana el nombre de jugando a los dados'''
ventana.title("jugando a los dados")
'''     dimenciónamos el objeto ventana en 600 x 500 px'''
ventana.geometry("600x500")
'''    opción  dimenciónamos el objeto ventana en 600 x 500 px y ubicación de pantalla 700 x 200'''
# ~ ventana.geometry('600x500+700+200')
'''    ocpión  dimenciónamos el objeto ventana en 600 x 500 px vi config '''
#ventana.config(width=600, height=500)
# ~ '''     fijo la dimenciónamos el objeto ventana para que el usuario no pueda agrandarla ni achicarla'''
ventana.resizable(width=False, height=False)
ventana.iconbitmap('icono.ico')
# ~ ##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_0"  paso el parametro de text = " a jugar..."'''
etiqueta_info_salida_0 = tk.Label(text=" a jugar...")
'''     con al objeto "Label" "etiqueta_info_salida_0", configuro el color de fondo "bg" color de fuente "fg" fuente y tamaño "font=("Courier", 24)"'''
etiqueta_info_salida_0.config( bg="black", fg="red",font=("Courier", 24))
'''     doy al objeto "Label" "etiqueta_info_salida_0" ubicación y tamaño'''
etiqueta_info_salida_0.place(x=210, y=290)
# ~ ##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_1"  paso el parametro de text = " Ingresa tu nombre" '''
etiqueta_info_salida_1 = tk.Label(text="Ingresa tu nombre")
'''     doy al objeto "Label" "etiqueta_info_salida_1" ubicación. dejo el tamaño en defauld para q se calcule a partir del text'''
etiqueta_info_salida_1.place(x=200, y=75)
# ~ ##############################################################################################
'''     creo el objeto Entry de la biblioteca 'tk' dandole en nombre de "caja_info_entrada_0" para que el usuario ingrese sus datos'''
caja_info_entrada_0 = tk.Entry()
'''     doy al objeto "Entry" "caja_info_entrada_0" la ubicación y tamaño '''
caja_info_entrada_0.place(x=320, y=75 , width=100, height=25)

# ~ ##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_3"  paso el parametro de text = ""(vacio) '''
etiqueta_info_salida_3 = tk.Label(text="")
'''     con al objeto "Label" "etiqueta_info_salida_3", configuro fuente y tamaño "font=("Courier", 24)"'''
etiqueta_info_salida_3.config(font=("Courier", 24))
'''     doy al objeto "Label" "etiqueta_info_salida_3" ubicación y tamaño'''
etiqueta_info_salida_3.place(x=230, y=190)
# ~ ##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_4"  paso el parametro de text = ""(vacio)'''
etiqueta_info_salida_4 = tk.Label(text="")
'''     con al objeto Label "etiqueta_info_salida_4", configuro fuente y tamaño "font=("Courier", 24)"'''
etiqueta_info_salida_4.config(font=("Courier", 24))
'''     doy al objeto "Label" "etiqueta_info_salida_4" ubicación y tamaño '''
etiqueta_info_salida_4.place(x=200, y=230)
# ~ ##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el nombre boton_accion_jugar con el texto 'Jugar'
        y si es clickeado debe ejecutar la función jugar
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la finción) '''
boton_accion_Jugar = tk.Button(text="Jugar", command=jugar)
'''     ubico el objeto 'boton_accion_Jugar, en x=50 e y = 50
        doy un tamaño al objeto 'boton_accion_Jugar,  width=100(ancho), height=30(alto) '''
boton_accion_Jugar.place(x=50, y=50, width=100, height=30)
# ~ ##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el nombre boton_accion_Salir con el texto 'Salir'
        y si es clickeado debe ejecutar la función salir
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la función) '''
boton_accion_Salir = tk.Button(text="Salir", command=salir)
'''     ubico el objeto 'boton_accion_Salir, en x=50 e y = 50
        doy un tamaño al objeto 'boton_accion_Salir,  width=100(ancho), height=30(alto) '''
boton_accion_Salir.place(x=50, y=100, width=100, height=30)
# ~ ##############################################################################################
'''     creo el objeto img de la biblioteca 'PIL Image' dandole en nombre de la imagen "dados.jpg"
        que debe estar en la misma carpeta que el script python'''
img_original = Image.open("dados.jpg")
'''     doy atributos al objeto img tamaño)'''
img_resize = img_original.resize((100,100))
'''     creo el objeto dados de la biblioteca PIL 'ImageTk.PhotoImage' pasandole el objeto img como parametro '''
img_resize_tkinter =  ImageTk.PhotoImage(img_resize)
# ~ ##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_5_imagen"  paso el parametro de image = objeto dados'''
etiqueta_info_salida_5_imagen = tk.Label(image=img_resize_tkinter)
'''     doy al objeto "Label" "etiqueta_info_salida_5_imagen" ubicación y tamaño'''
etiqueta_info_salida_5_imagen.place(x=100, y=188, width=100, height=100)#.pack()

'''     cierro el loop de pantalla'''
ventana.mainloop()
##############################################################################################



