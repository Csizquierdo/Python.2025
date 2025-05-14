print ("*"*50)
print ("""Ejercicio
generar un número aleatorio de 1 al 6 (simulábamos el arrojar un dado),
debemos pasarlo a una aplicación deescritorio. La vista de la aplicación debería
ser similar a:

En la caja deberían de aparecer los mensaje_1s aleatorios cada vez que se presióna el botón.
Antes de mostrar los mensaje_1s se limpia la caja, dejando el mismo mensaje_1 hasta que se vuelve a pulsar.
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
def jugar(apuesta,numero,mensaje_1,mensaje_2,saldo):
    global billetera
    '''                                                 en la variable tirada guardo un numero random(al azar..o casi) entre 0 y 6'''
    tirada = random.randint(1,6)
    '''                                                 tome el nombre de la caja de texto u lo guardo en nombre'''
    apuesta_fun=apuesta.get()
    numero_fun=numero.get()
    '''                                                 condición nombre esta vacio '''
    if not (numero_fun.isnumeric() and int(numero_fun)>=1 and int (numero_fun)<=6) : 

    # ~ if ( (not numero.isnumeric() or int(numero)<0 or int (numero)>6:) or \
        # ~ not  apuesta_fun.replace(".","").isnumeric() or float(apuesta_fun)<0 and float (apuesta_fun)>billetera) :
        mensaje_1.config(text="Por favor ingrese solo números")
        mensaje_2.config(text="entre 1 y 6")
        return
    numero_fun=int(numero_fun)
    '''                                                 condición nombre esta vacio '''
    if not (   apuesta_fun.replace(".","").isnumeric() and float(apuesta_fun)>0 and float (apuesta_fun)<=billetera) : 
        mensaje_1.config(text="Por favor ingrese solo números")
        mensaje_2.config(text=f"entre 1 y {billetera}6")
        return
    apuesta_fun=float(apuesta_fun)
    if (int(numero_fun)==tirada):
        mensaje_1.config(text=f"genial ganaste {apuesta_fun*5}")
        mensaje_2.config(text=f"En la tirada salio {tirada}")
        # ~ billetera = billetera +apuesta_fun*5
        billetera += apuesta_fun*5
    else:
        
        mensaje_1.config(text=f"la proxima seguro ganas")
        mensaje_2.config(text=f"En la tirada salio {tirada}")
        billetera = billetera -apuesta_fun
        billetera -= apuesta_fun
    saldo.config(text=f"su saldo es $  {billetera}")
def salir():
    '''                                                   termino el programa '''
    exit()
##############################################################################################
def makewindows():

    '''                                                  'Programa principal' '''
    '''     creo el objeto GUI con el nombre ventana'''
    ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
    '''     le doy al obje "!!!!!"to ventana el nombre de jugando a los dados'''
    ventana.title("jugando a los dados")
    '''     dimenciónamos el objeto ventana en 600 x 500 px'''
    ventana.geometry("600x500")
    ventana.config( bg="white")
    '''    opción  dimenciónamos el objeto ventana en 600 x 500 px y ubicación de pantalla 700 x 200'''
    # ~ ventana.geometry('600x500+700+200')
    '''    ocpión  dimenciónamos el objeto ventana en 600 x 500 px vi config '''
    #ventana.config(width=600, height=500)
    # ~ '''     fijo la dimenciónamos el objeto ventana para que el usuario no pueda agrandarla ni achicarla'''
    ventana.resizable(width=False, height=False)
    ventana.iconbitmap('icono.ico')






    ##############################################################################################
    global billetera
    saldo = tk.Label(text=f"su saldo es $  {billetera}")
    saldo.config( bg="white", fg="#00ff00",font=("Arial", 25))
    saldo.place(x=250, y=25, width=310, height=40)

    # ~ ############
    ##############################################################################################
    '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_0"  paso el parametro de text = " a jugar..."'''
    etiqueta_info_salida_0 = tk.Label(text=" a jugar...")
    '''     con al objeto "Label" "etiqueta_info_salida_0", configuro el color de fondo "bg" color de fuente "fg" fuente y tamaño "font=("Courier", 24)"'''
    etiqueta_info_salida_0.config( bg="white", fg="blue",font=("Courier", 18))
    '''     doy al objeto "Label" "etiqueta_info_salida_0" ubicación y tamaño'''
    etiqueta_info_salida_0.place(x=200, y=325,width=200, height=25)

    # ~ ##############################################################################################
    '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_1"  paso el parametro de text = " Ingresa tu nombre" '''
    etiqueta_info_salida_1 = tk.Label(text="Ingresa tu apuesta", bg="#ffffff")
    '''     doy al objeto "Label" "etiqueta_info_salida_1" ubicación. dejo el tamaño en defauld para q se calcule a partir del text'''
    etiqueta_info_salida_1.place(x=250, y=125, width=100, height=25)

    # ~ ##############################################################################################
    '''     creo el objeto Entry de la biblioteca 'tk' dandole en nombre de "caja_info_entrada_0" para que el usuario ingrese sus datos'''
    apuesta = tk.Entry()
    '''     doy al objeto "Entry" "caja_info_entrada_0" la ubicación y tamaño '''
    apuesta.place(x=375, y=125 , width=100, height=25)
    # ~ ##############################################################################################
    '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_1"  paso el parametro de text = " Ingresa tu nombre" '''
    etiqueta_info_salida_2 = tk.Label(text="Ingresa tu numero", bg="#ffffff")
    '''     doy al objeto "Label" "etiqueta_info_salida_1" ubicación. dejo el tamaño en defauld para q se calcule a partir del text'''
    etiqueta_info_salida_2.place(x=250, y=75, width=100, height=25)

    # ~ ##############################################################################################
    '''     creo el objeto Entry de la biblioteca 'tk' dandole en nombre de "caja_info_entrada_0" para que el usuario ingrese sus datos'''
    numero = tk.Entry()
    '''     doy al objeto "Entry" "caja_info_entrada_0" la ubicación y tamaño '''
    numero.place(x=375, y=75 , width=100, height=25)

    # ~ ##############################################################################################
    '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "mensaje_1"  paso el parametro de text = ""(vacio) '''
    mensaje_1 = tk.Label(text="",bg="white")
    '''     con al objeto "Label" "mensaje_1", configuro fuente y tamaño "font=("Courier", 24)"'''
    mensaje_1.config(font=("Courier", 18))
    '''     doy al objeto "Label" "mensaje_1" ubicación y tamaño'''
    mensaje_1.place(x=50, y=225, width=500, height=25)
    # ~ ##############################################################################################
    '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "mensaje_2"  paso el parametro de text = ""(vacio)'''
    mensaje_2 = tk.Label(text="",bg="#ffffff")
    '''     con al objeto Label "mensaje_2", configuro fuente y tamaño "font=("Courier", 24)"'''
    mensaje_2.config(font=("Courier", 18))
    '''     doy al objeto "Label" "mensaje_2" ubicación y tamaño '''
    mensaje_2.place(x=50, y=275, width=500, height=25)

    # ~ ##############################################################################################
    '''     creo el objeto Button de la biblioteca tk con el nombre boton_accion_jugar con el texto 'Jugar'
            y si es clickeado debe ejecutar la función jugar
            (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la finción) '''
    boton_accion_Jugar = tk.Button(text="Jugar", command=lambda : jugar(apuesta,numero,mensaje_1,mensaje_2,saldo))
    '''     ubico el objeto 'boton_accion_Jugar, en x=50 e y = 50
            doy un tamaño al objeto 'boton_accion_Jugar,  width=100(ancho), height=30(alto) '''
    boton_accion_Jugar.place(x=50, y=400, width=100, height=30)
    # ~ ##############################################################################################
    '''     creo el objeto Button de la biblioteca tk con el nombre boton_accion_Salir con el texto 'Salir'
            y si es clickeado debe ejecutar la función salir
            (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la función) '''
    boton_accion_Salir = tk.Button(text="Salir", command=salir)
    '''     ubico el objeto 'boton_accion_Salir, en x=50 e y = 50
            doy un tamaño al objeto 'boton_accion_Salir,  width=100(ancho), height=30(alto) '''
    boton_accion_Salir.place(x=450, y=400, width=100, height=30)

    # ~ ##############################################################################################
    '''     creo el objeto img de la biblioteca 'PIL Image' dandole en nombre de la imagen "dados.jpg"
            que debe estar en la misma carpeta que el script python'''
    img_original = Image.open("dados.jpg")
    '''     doy atributos al objeto img tamaño)'''
    img_resize = img_original.resize((200,200))
    '''     creo el objeto dados de la biblioteca PIL 'ImageTk.PhotoImage' pasandole el objeto img como parametro '''
    img_resize_tkinter =  ImageTk.PhotoImage(img_resize)
    # ~ ##############################################################################################
    '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "etiqueta_info_salida_5_imagen"  paso el parametro de image = objeto dados'''
    etiqueta_info_salida_5_imagen = tk.Label(image=img_resize_tkinter)
    '''     doy al objeto "Label" "etiqueta_info_salida_5_imagen" ubicación y tamaño'''
    etiqueta_info_salida_5_imagen.place(x=10, y=10, width=200, height=200)#.pack()

    '''     cierro el loop de pantalla'''
    ventana.mainloop()
    ##############################################################################################
billetera = 1000000
makewindows()



























