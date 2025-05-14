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

class dados:
    def __init__(self):
        self.billetera = 1000000
        self.makewindows()



    def jugar(self):

        '''                                                 en la variable tirada guardo un numero random(al azar..o casi) entre 0 y 6                          '''
        tirada = random.randint(1,6)
        '''                                                 tome el nombre de la caja de texto u lo guardo en nombre                                            '''
        nombre=self.caja_nombre.get()
        '''                                                 condición nombre esta vacio      '''
        
        numero  = self.caja_numero.get()
        apuesta = self.caja_apuesta.get()

        if not (numero.isdigit() and int(numero) >0 and int(numero) <=6) :
            self.salida.config(text=f"numero no valido")
            self.caja_numero.delete(0,tk.END)
            return
        else:
            numero = int(numero)
        if not (apuesta.replace(".","").isdigit() and float(apuesta) >0 and float(apuesta) <=self.billetera) :
            self.salida.config(text=f"apuesta no valida")
            self.caja_apuesta.delete(0,tk.END)
            return
        else:
            apuesta = float(apuesta)           
            '''                                                 No True > False
                                                                piso nombre con el contenido anterior de nombre tras ejecutar el metodo upper (mayusculas)      '''
        self.caja_nombre.delete(0,tk.END)
        self.caja_nombre.insert(0,"")
        nombre = nombre.upper()

                
        if numero == tirada:
            self.billetera += (apuesta *5)
            string = f"genial {nombre} ganastes {apuesta*5}..."
        else:
            self.billetera -= apuesta
            string = f"{nombre} la proxima sera ..."
        self.etiqueta.config(text=f"tu saldo es {self.billetera}")          '''                                                 En la self.etiqueta salida ingreso el texto genial y el nombre o !!!!! en caso de estar vacio            '''
        self.salida.config(text=f"{string}")                                '''                                                 En la self.etiqueta resultado ingreso el texto 'En la tirada salio' y el contenido de la variable tirada '''
        self.resultado.config(text=f"En la tirada salio {tirada}")          '''                                                 defino la función salir q sera usada al cliquear el boton 'botonSalir'    '''
        return
    def salir(self):
        '''                                                   termino el programa                                                                                 '''
        exit()
    ##############################################################################################
    def makewindows(self):
        print ("creamos ventana")
        '''                                                  'Programa principal'                                                                                   '''
        '''     creo el objeto GUI con el nombre self.ventana                                                                                                            '''
        self.ventana = tk.Tk()# llamo a la bibloioteca q importe mediante el alias
        '''     le doy al obje "!!!!!"to self.ventana el nombre de jugando a los dados'''
        self.ventana.title("jugando a los dados")
        '''     dimenciónamos el objeto self.ventana en 600 x 500 px                                                                                                     '''
        self.ventana.config(bg="white")
        self.ventana.geometry("600x500")
        
        
        
        
        ##############################################################################################
        '''     creo el objeto Button de la biblioteca tk con el nombre botonjugar con el texto 'Jugar'
                y si es clickeado debe ejecutar la función jugar
                (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la finción)                                                 '''
        self.botonJugar = tk.Button(text="Jugar", command=self.jugar)# lambda 
        '''     ubico el objeto 'botonJugar, en x=50 e y = 50
                doy un tamaño al objeto 'botonJugar,  width=100(ancho), height=30(alto)                                                                             '''
        self.botonJugar.place(x=100, y=420, width=100, height=30)
        ##############################################################################################
        '''     creo el objeto Button de la biblioteca tk con el nombre botonSalir con el texto 'Salir'
                y si es clickeado debe ejecutar la función salir
                (nota: q en este caso la función no lleva (parentesis ni argumentos), solo el nombre de la función)                                                 '''
        self.botonSalir = tk.Button(text="Salir", command=self.salir)
        '''     ubico el objeto 'botonSalir, en x=50 e y = 50
                doy un tamaño al objeto 'botonSalir,  width=100(ancho), height=30(alto)                                                                             '''
        self.botonSalir.place(x=400, y=420, width=100, height=30)
        ##############################################################################################
        '''     creo el objeto img de la biblioteca 'PIL Image' dandole en nombre de la imagen "dados.jpg"
                que debe estar en la misma carpeta que el script python'                                                                                            '''
        self.img = Image.open("dados.jpg")
        '''     doy atributos al objeto img (tamaño)                                                                                                                '''
        self.img = self.img.resize((200,200))
        '''     creo el objeto dados de la biblioteca PIL 'ImageTk.PhotoImage' pasandole el objeto img como parametro                                               '''
        self.dados =  ImageTk.PhotoImage(self.img)
        ##############################################################################################
        '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "lab_im"  paso el parametro de image = objeto dados                                 '''
        self.lab_im = tk.Label(image=self.dados)
        '''     doy al objeto "Label" "lab_im" ubicación y tamaño                                                                                                   '''
        self.lab_im.place(x=10, y=10, width=200, height=200)#.pack()
        ##############################################################################################
        '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "self.etiqueta"  paso el parametro de text = " a jugar..."                               '''
        self.etiqueta = tk.Label(text=f"tu saldo es {self.billetera}")
        '''     con al objeto "Label" "self.etiqueta", configuro el color de fondo "bg" color de fuente "fg" fuente y tamaño "font=("Courier", 24)"                      '''
        self.etiqueta.config( bg="#ffffff", fg="blue",font=("Courier", 18))
        '''     doy al objeto "Label" "self.etiqueta" ubicación y tamaño                                                                                                 '''
        self.etiqueta.place(x=100, y=380, width=400, height=30)
        ##############################################################################################
        '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "self.etiqueta_nombre"  paso el parametro de text = " Ingresa tu nombre"                 '''
        self.etiqueta_nombre = tk.Label(text="Ingresa tu nombre", bg="white")
        '''     doy al objeto "Label" "self.etiqueta_nombre" ubicación. dejo el tamaño en defauld para q se calcule a partir del text                                    '''
        self.etiqueta_nombre.place(x=200, y=75)
        ##############################################################################################
        '''     creo el objeto Entry de la biblioteca 'tk' dandole en nombre de "self.caja_nombre" para que el usuario ingrese sus datos                                 '''
        self.caja_nombre = tk.Entry()
        '''     doy al objeto "Entry" "self.caja_nombre" la ubicación y tamaño                                                                                           '''
        self.caja_nombre.place(x=320, y=75 , width=100, height=25)
        ##############################################################################################
        self.etiqueta_apuesta = tk.Label(text="Ingresa tu apuesta", bg="white")
        self.etiqueta_apuesta.place(x=200, y=125 , width=100, height=25)
        ##############################################################################################
        self.caja_apuesta = tk.Entry()
        self.caja_apuesta.place(x=320, y=125 , width=100, height=25)
        ##############################################################################################
        self.etiqueta_numero = tk.Label(text="Ingresa tu número", bg="white")
        self.etiqueta_numero.place(x=200, y=175 , width=100, height=25)
        ##############################################################################################       
        self.caja_numero = tk.Entry()
        self.caja_numero.place(x=320, y=175 , width=100, height=25)
        ##############################################################################################
        '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "salida"  paso el parametro de text = ""(vacio)                                     '''
        self.salida = tk.Label(text="")
        '''     con al objeto "Label" "salida", configuro fuente y tamaño "font=("Courier", 24)"                                                                    '''
        self.salida.config(font=("Courier", 12), bg="white")
        '''     doy al objeto "Label" "salida" ubicación y tamaño                                                                                                   '''
        self.salida.place(x=100, y=225, width=400, height=30)
        ##############################################################################################
        '''     creo el objeto Label de la biblioteca 'tk' dandole en nombre de "resultado"  paso el parametro de text = ""(vacio)                                  '''
        self.resultado = tk.Label(text="")
        '''     con al objeto Label "resultado", configuro fuente y tamaño "font=("Courier", 24)"                                                                   '''
        self.resultado.config(font=("Courier", 12), bg="white")
        '''     doy al objeto "Label" "resultado" ubicación y tamaño                                                                                                '''
        self.resultado.place(x=100, y=325 , width=400, height=30)
        ##############################################################################################
        '''     cierro el loop de pantalla'''
        self.ventana.mainloop()

obj=dados()


