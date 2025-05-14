print ("*"*50)

import tkinter as tk#<----<-----<----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca tkinter y le damos el  Alias de tk                                 '''
from PIL import ImageTk, Image# <----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca PIL solo ImageTk, Image                                            '''
import os#<----<-----<----<-----<----<-----<----<-----<----<-----
'''                                                             importamos la biblioteca os (operative system)                                              '''
import random#<----<-----<----<-----<----<-----<----<-----<----<
'''                                                             importamos la biblioteca random (aleatoriedad)                                              '''


'''                                             defino la función jugar q sera usada al cliquear el boton 'botonJugar'                                      '''
def jugar():
    global billetera
    '''                                                 en la variable tirada guardo un numero random(al azar..o casi) entre 0 y 6                          '''
    tirada = random.randint(1,6)
    '''                                                 tome el apuesta de la caja de texto u lo guardo en apuesta                                            '''
    apuesta= caja_apuesta.get()
    numero = caja_numero.get()
    '''                 
                                    condición apuesta esta vacio                                                                         '''
    if apuesta == "" or apuesta.isdigit() is False or (apuesta.replace(".","").isdigit() is True  and  (0> float(apuesta) <=billetera)): 
        salida.config(text=f"por favor ingrese una apuesta dentro de su saldo")
    elif numero == "" or numero.isdigit() is False or (numero.replace(".","").isdigit() is True  and  (1    >= int(numero) <=6)): 
        salida.config(text=f"por favor ingrese un numero entre 1 y 6")
                
    else:
        apuesta=float(apuesta)
        caja_apuesta.delete(0,tk.END)
        caja_apuesta.insert(0,"$$$")
        numero=int(numero)
        if numero == tirada:
            salida.config(text=f"igual. Se repite")
        elif  numero > tirada and var_menor_mayor == "menor":
            
            salida.config(text=f"Ganaste")
            billetera +=apuesta

        elif  numero < tirada and var_menor_mayor == "mayor":
            salida.config(text=f"Ganaste")
            billetera +=apuesta
        else: 
            billetera -=apuesta
            salida.config(text=f"La proxima sera")
    etiqueta_saldo.config(text=f"su saldo es {billetera}", bg="white")
    resultado.config(text=f"En la tirada salio {tirada}")


'''                                             defino la función salir q sera usada al cliquear el boton 'botonSalir'                                      '''
def menor_mayor():
    global var_menor_mayor
    if var_menor_mayor == "menor":
        var_menor_mayor= "mayor"

    else:
        var_menor_mayor= "menor"
    salida_mayor_menor=f"Estas jugando al {var_menor_mayor}"
    etiqueta_menor_mayor .config(text=salida_mayor_menor)
    etiqueta_menor_mayor.place(x=20, y=155, width=150, height=25)


def salir():
    '''                                                 termino el programa                                                                                 '''
    exit()
billetera=100000
var_menor_mayor = "menor"
##############################################################################################
'''                                                  'Programa principal'       '''
'''     creo el objeto GUI con el apuesta ventana                                '''
ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
'''     le doy al objeto ventana el apuesta de jugando a los dados'''
ventana.title("jugando a los dados")
ventana.config(bg="white")
'''     dimenciónamos el objeto ventana en 600 x 500 px                         '''
ventana.geometry("600x500")
##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el apuesta botonjugar con el texto 'Jugar'
        y si es clickeado debe ejecutar la función jugar
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el apuesta de la finción)         '''
botonJugar = tk.Button(text="Jugar", command=jugar)
'''     ubico el objeto 'botonJugar, en x=50 e y = 50
        doy un tamaño al objeto 'botonJugar,  width=100(ancho), height=30(alto)                         '''
botonJugar.place(x=50, y=450, width=100, height=30)
##############################################################################################
'''     creo el objeto Button de la biblioteca tk con el apuesta botonSalir con el texto 'Salir'
        y si es clickeado debe ejecutar la función salir
        (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el apuesta de la función)         '''
botonSalir = tk.Button(text="Salir", command=salir)
'''     ubico el objeto 'botonSalir, en x=50 e y = 50
        doy un tamaño al objeto 'botonSalir,  width=100(ancho), height=30(alto)                         '''
botonSalir.place(x=450, y=450, width=100, height=30)
##############################################################################################
'''     creo el objeto img de la biblioteca 'PIL Image' dandole en apuesta de la imagen "dados.jpg"
        que debe estar en la misma carpeta que el script python'        '''
img = Image.open("dados.jpg")
'''     doy atributos al objeto img (tamaño)  '''
img = img.resize((200,200))
'''     creo el objeto dados de la biblioteca PIL 'ImageTk.PhotoImage' pasandole el objeto img como parametro '''
dados =  ImageTk.PhotoImage(img)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en apuesta de "lab_im"  paso el parametro de image = objeto dados '''
lab_im = tk.Label(image=dados)
'''     doy al objeto "Label" "lab_im" ubicación y tamaño  '''
lab_im.place(x=390, y=10, width=200, height=200)#.pack()
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en apuesta de "etiqueta"  paso el parametro de text = " a jugar..."   '''
etiqueta = tk.Label(text=" a jugar ...")
'''     con al objeto "Label" "etiqueta", configuro el color de fondo "bg" color de fuente "fg" fuente y tamaño "font=("Courier", 24)" '''
etiqueta.config( bg="black", fg="red",font=("Courier", 24))
'''     doy al objeto "Label" "etiqueta" ubicación y tamaño  '''
etiqueta.place(x=210, y=290)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en apuesta de "etiqueta_apuesta"  paso el parametro de text = " Ingresa tu apuesta" '''
etiqueta_apuesta = tk.Label(text="Ingresa tu apuesta", bg="white")
'''     doy al objeto "Label" "etiqueta_apuesta" ubicación. dejo el tamaño en defauld para q se calcule a partir del text  '''
etiqueta_apuesta.place(x=20, y=75, width=150, height=25)
'''     creo el objeto Entry de la biblioteca 'tk' dandole en apuesta de "caja_apuesta" para que el usuario ingrese sus datos     '''
caja_apuesta = tk.Entry()
'''     doy al objeto "Entry" "caja_apuesta" la ubicación y tamaño  '''
caja_apuesta.place(x=170, y=75 , width=100, height=25)
##############################################################################################

etiqueta_numero = tk.Label(text="Ingresa el numero a jugar" , bg="white")
etiqueta_numero.place(x=20, y=115, width=150, height=25)

caja_numero = tk.Entry()
caja_numero.place(x=170, y=115 , width=100, height=25)

##############################################################################################
etiqueta_menor_mayor = tk.Label(text="Estas jugando al menor ", bg="white")
etiqueta_menor_mayor.place(x=20, y=155, width=150, height=25)
botonmenor_mayor = tk.Button(text="Mayor menor", command=menor_mayor)
botonmenor_mayor.place(x=170, y=155, width=100, height=30)
##############################################################################################
etiqueta_saldo = tk.Label(text=f"su saldo es {billetera}", bg="white")
etiqueta_saldo.config( bg="lightblue1", fg="green",font=("Courier", 24))
etiqueta_saldo.place(x=20, y=25)
##############################################################################################
# ~ '''     creo el objeto Label de la biblioteca 'tk' dandole en apuesta de "etiqueta_apuesta"  paso el parametro de text = " Ingresa tu apuesta" '''
# ~ etiqueta_apuesta = tk.Label(text="Ingresa tu apuesta")
# ~ '''     doy al objeto "Label" "etiqueta_apuesta" ubicación. dejo el tamaño en defauld para q se calcule a partir del text  '''
# ~ etiqueta_apuesta.place(x=200, y=75)
##############################################################################################



'''     creo el objeto Label de la biblioteca 'tk' dandole en apuesta de "salida"  paso el parametro de text = ""(vacio)  '''
salida = tk.Label(text="")
'''     con al objeto "Label" "salida", configuro fuente y tamaño "font=("Courier", 24)" '''
salida.config(font=("Courier", 24))
'''     doy al objeto "Label" "salida" ubicación y tamaño  '''
salida.place(x=230, y=190)
##############################################################################################
'''     creo el objeto Label de la biblioteca 'tk' dandole en apuesta de "resultado"  paso el parametro de text = ""(vacio)  '''
resultado = tk.Label(text="")
'''     con al objeto Label "resultado", configuro fuente y tamaño "font=("Courier", 24)" '''
resultado.config(font=("Courier", 24))
'''     doy al objeto "Label" "resultado" ubicación y tamaño  '''
resultado.place(x=200, y=230)
##############################################################################################
'''     cierro el llop de pantalla'''
ventana.mainloop()




