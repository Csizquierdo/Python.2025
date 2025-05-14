import json
import random
import os
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tPresione enter para continuar")
limpiar();
#################################################################
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
#################################################################
def pausa():
    input("\tPresione una tecla para continuar")
#################################################################
limpiar()
#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aqui las precticas hechas
    pass
from datetime import datetime, date, time

print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║ ╔══════╗ ╦      ╦ ╔╗      ╦  ╔════╗  ╦  ╔════╗  ╔╗      ╦ ╔══════╗  ╔════╗  ║
║ ║        ║      ║ ║╚╗     ║ ╔╝    ╚╗ ║ ╔╝    ╚╗ ║╚╗     ║ ║        ╔╝    ╚╗ ║
║ ║        ║      ║ ║ ╚╗    ║ ║        ║ ║      ║ ║ ╚╗    ║ ║        ║        ║
║ ║        ║      ║ ║  ╚╗   ║ ║        ║ ║      ║ ║  ╚╗   ║ ║        ╚╗       ║
║ ╠════╗   ║      ║ ║   ╚╗  ║ ║        ║ ║      ║ ║   ╚╗  ║ ╠═════╝   ╚════╗  ║
║ ║        ║      ║ ║    ╚╗ ║ ║        ║ ║      ║ ║    ╚╗ ║ ║              ╚╗ ║
║ ║        ╚╗    ╔╝ ║     ╚╗║ ╚╗    ╔╝ ║ ╚╗    ╔╝ ║     ╚╗║ ║        ╚╗    ╔╝ ║
║ ╩         ╚════╝  ╩      ╚╝  ╚════╝  ╩  ╚════╝  ╩      ╚╝ ╚══════╝  ╚════╝  ║
║                                                                             ║
║                                                                             ║
║    ╦           ╔═════╗     ╔╗      ╔╗   ╔══════╗    ╔══════╗     ╔═════╗    ║
║    ║          ╔╝     ╚╗    ║╚╗    ╔╝║   ║      ╚╗   ║      ╚╗   ╔╝     ╚╗   ║
║    ║          ║       ║    ║ ╚╗  ╔╝ ║   ║      ╔╝   ║       ║   ║       ║   ║
║    ║          ║       ║    ║  ╚╗╔╝  ║   ╠══════╣    ║       ║   ║       ║   ║
║    ║          ╠═══════╣    ║   ╚╝   ║   ║      ╚╗   ║       ║   ╠═══════╣   ║
║    ║          ║       ║    ║        ║   ║       ║   ║       ║   ║       ║   ║
║    ║          ║       ║    ║        ║   ║      ╔╝   ║      ╔╝   ║       ║   ║
║    ╚═══════   ╩       ╩    ╩        ╩   ╚══════╝    ╚══════╝    ╩       ╩   ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                              funciones y Metodos                            ║
║                              -------------------                            ║
║          funciones    Description                                           ║
║                   lambda                                                    ║
║                                                                             ║
║          Metodos son funciones dentro de clases donde se deberia instanciar ║
║                   a la clase con self nombre_objeto                         ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              funciones,  Metodos                            ║
║                                  y Generadores                              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

pausa();limpiar();
#################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  Lambda                                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""")





impar = lambda numero: numero%2 != 0
impar(5)
#True
#Función lambda - operaciones de cadena

#A continuación, se presenta un ejemplo para darle la vuelta a una cadena rebanándola en sentido inverso:

revertir = lambda cadena: cadena[::-1]
revertir("Plone")
#'enolP'
revertir("enolP")
#'Plone'
#Función lambda - varios parámetros

#A continuación, se presenta un ejemplo para varios parámetros, por ejemplo para sumar dos números:

sumar = lambda x,y: x+y
sumar(5,2)
#7


#################################################################
print ("Forma clasica")
def CalculoVolumneCubo(b,a,p):#base, altura, profundidad
    return (b*a*p)
print ( CalculoVolumneCubo(10,2,5))
print ( CalculoVolumneCubo(20,10,50))
print ("Forma lambda")

CalculoVolumneCubo=lambda b,a,p : (b*a*p)#<---------return
#                           ^
#                           L___parametros de entrada
print ( CalculoVolumneCubo(10,2,5))
print ( CalculoVolumneCubo(20,10,50))
pausa()
limpiar()

datos=lambda nombre, puesto : f"el empleado {nombre} trabaja como {puesto}"
print (datos("Ariel","Mantenimiento"))
pausa()
limpiar()




#################################################################
#Ejercicio_funciones_Ej_010

print("""Vamos a hacer una función
def doblar(num):
    resultado = num*2
    return resultado
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num):
    resultado = num*2
    return resultado
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
pausa()
print ("-"*50)
print("""Vamos a hacerlo mas simple
def doblar(num):
    return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num):
    return num*2
print (f"el valor ingresado es de {valor}")
print("el doble es :",doblar(valor))
pausa()
print ("-"*50)
print(""" mas simple
def doblar(num): return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num): return num*2
print (f"el valor ingresado es de {valor}")
print("el doble es :",doblar(valor))

print(""" y ahora......
Esta notación simple es la que una función lambda intenta replicar, fijaros, vamos a convertir la función en una función anónima:
doblar = (lambda num: num*2)
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

pausa()
print ("-"*50)
doblar = lambda num: num*2
print ("doblar = lambda num: num*2")
print (f"el valor ingresado es de {valor}")
print("el doble es :",doblar(valor))
print(""" Ejemplo""")
pausa()
print ("-"*50)
impar = lambda num: num%2 != 0
print ("impar = lambda num: num%2 != 0")
print (f"el valor ingresado es de {valor}")
print("es impar :",impar(valor))

pausa();limpiar();#1);
#################################################################
#Ejercicio_funciones_Ej_011
print ("""
Función lambda
--------------
La función lambda se utiliza para declarar funciones que sólo ocupan una línea. Son objetos que se pueden asignar a variables para usar con posterioridad.
""")
array = [11, 25, 34, 100,0, 23]
print(f"array = {array}")

dato = lambda x :x**2#<----salida
#             ^
#             L__dato q recibe
print ("dato = lambda x :x**2")
for valor in array:
    print ("dato(valor)**2:",dato(valor))

pausa();limpiar();#2);
#################################################################

dato = lambda x: x*x

lista = [1,2,3,5,8,13]
print (f"lista{lista}")
print ("dato = lambda x :x*x")
for elemento in lista:
    print(f"elemento^elemento:",dato(elemento))
pausa()
print ("-"*50)
#################################################################

print (""" Lambda, con 2 argumentos:""")

area_triangulo = (lambda b,h: b*h/2)
medidas = [(34, 8), (26, 8), (44, 18)]
print (f"medidas{medidas}")
print ("area_triangulo = (lambda b,h: b*h/2)")
for datos in medidas:
    base = datos[0]
    altura = datos[1]
    print("area_triangulo(base, altura):",area_triangulo(base, altura))
pausa();limpiar();#3);
#################################################################
mensaje = lambda numero: f"el número ingresado es: {numero}"
print("texto:",mensaje(2))
pausa()
print ("-"*50)
pausa();limpiar();#4)
#################################################################
binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2
print ("binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2")
print ("binomio_cuadrado de (2,3):",binomio_cuadrado(2,3))
pausa()
print ("-"*50)
pausa();limpiar();#5)
#################################################################
# ~ def cubos(numero):
    # ~ str_numero = str(numero)
    # ~ cubos = (int(valor)**3 for valor in str_numero)
    # ~ return sum(cubos)

# ~ valores_buscados = []
# ~ print ("Origen de datos: range(100,1000):")
# ~ for numero in range(100,1000):
    # ~ if numero == cubos(numero):
        # ~ valores_buscados.append(numero)
# ~ print(valores_buscados)
#                                       o
suma_cubos = lambda numero: sum(int(digito)**3 for digito in str(numero))
numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]
print ("suma_cubos = lambda numero: sum(int(digito)**3 for digito in str(numero))")
print ("numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]")
print ("numeros_buscados:",numeros_buscados)
pausa();limpiar();#6);
##############################################################
lista_anidada=[ ["Jose", 30], ["pedro", 55],["Ariel",47],["Ana",40],["Bea", 30]]
print (f"lista_anidada:{lista_anidada}")
lista_anidada.sort(key = lambda dato : dato [1])
print ("lista_anidada.sort(key = lambda dato : dato [1])<---1 es el 2do dato de una lista")
print (f"lista_anidada ordenadas x edad:{lista_anidada}")
pausa();limpiar();#7)
#################################################################
#lambda <arguments> : <value_1> if <condition_1> else (<value_2> if <condition_2> else <value_3>)

dato = lambda x :1000/x if (x  != 0) else "Error"
array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x :1000/x if (x  != 0) else 'Error'")
for valor in array:
    print (f"1000/ {valor}= {dato(valor)}")
print ("-"*50)
pausa();limpiar();#8)
#################################################################

dato = lambda x : True if (x > 10 and x < 30) else False
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x : True if (x > 10 and x < 30) else False")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa();limpiar();#9)
#################################################################

dato = lambda x: x**2 if x%2 == 0 else x**3
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x**2 if x%2 == 0 else x**3")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa();limpiar();#10)
#################################################################
dato = lambda x : x*2 if x <=25 else (x*3 if x < 50 else -x)
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print("dato = lambda x : x*2 if x <=25  else (x*3 if x < 50 else -x)")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)

pausa();limpiar();#11)
#################################################################

dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )

Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa();limpiar();#12)
#################################################################

#numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]
#################################################################
dato = lambda x :x**2 if x % 2 == 0 else "Impar"
print ("Array:", array)
print ("dato = lambda x :x**2 if x % 2 == 0 else 'Impar'")
for valor in array:
    print (f"test",valor,dato(valor))
pausa();limpiar();#13)


#################################################################

print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + map                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
Operador Map:
El operador Map, toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento . Ejemplo:
Como pueden ver, "map" nos a devuelto una lista con todo los elementos de la lista "array", vemos que a cada elemento le sumo 5.

resultado = map(funcion, lista)
                   ^       ^___lista de parametros para la funcion
                   L______funcion a la que llamo mandandole dato por dato de la lista
""")
#################################################################
dato = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cubo = list(map(lambda x: x**3, dato))
print(cubo)
#################################################################
#Ejemplo del operador Map
def add_five(x):
    return x + 5
array = [11, 25, 34, 100, 23]
print(f"array = {array}")
resultado = list(map(add_five, array))

print("función normal + 5",resultado)
#        lo mismo pero en lambda


resultado = list(map(lambda x:x+5, array))
print("resultado = list(map(lambda x:x+5, array))")
print("función lambda + 5",resultado)

resultado = list(map(lambda x: x**2, array))
print("resultado = list(map(lambda x: x**2, array))")
print(resultado)
pausa();limpiar();#14)

#################################################################
#Ejercicio_funciones_Ej_012
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + filter (true / false)                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m

Operador Filter:

El operado filter (función, lista) ofrece una forma elegante de filtrar todos los elementos de una lista, para los que la función de función devuelve True.
El operador filter(f, l) necesita una función f como primer argumento. f devuelve un valor booleano, es decir, verdadero o falso. Esta función se aplicará a cada elemento de la lista. Solo si f devuelve True, el elemento de la lista se incluirá en la lista de resultados.
""")
#esta funcion necesita una lista de datos y devuelve otra de los datos filtrados true

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even = list(filter(lambda x: x%2 == 0, datos))
print(even)

#################################################################




array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]

def filtro(DatoElLista):
    if DatoElLista % 2 == 0:# es par
        return True
print (filter(filtro,array))
print (list(filter(filtro,array)))


#Usando el operador Filter
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
print("array",array)
resultado = list(filter(lambda x: x % 2 == 0, array))
print ("resultado = list(filter(lambda x: x % 2 == 0, array))")
print("x % 2 == 0, :",resultado)
print ("-"*50)
resultado = list(filter(lambda x: x > 0, array))
print ("resultado = list(filter(lambda x: x > 0, array))")
print("x > 0 :",resultado)
print ("-"*50)
resultado = list(filter(lambda x: x % 3 != 0, array))
print ("resultado = list(filter(lambda x: x % 3 != 0, array))")
print("x % 3 != 0 :",resultado)
print ("-"*50)
resultado = list(filter(lambda x: x % 3 <= 5, array)) # list()' convierte el iterable
print ("resultado = list(filter(lambda x: x % 3 <= 5, array))")
print("x % 3 <= 5 :",resultado)
print ("-"*50)
pausa();limpiar();#15);
#################################################################
#Ejercicio_funciones_Ej_013
# Ejercicio 5.6: Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.

pausa();limpiar();#4);
