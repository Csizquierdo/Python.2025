import os
try:
    from colorama import *
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import *
    
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione enter para continuar")
limpiar();
import math
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║    ╔═══════╗            ╦                                   ╦   ╔═══╦═══╗   ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗         ║       ║       ║
║    ║            ║       ║    ║       ║    ║                 ║       ║       ║
║    ║            ║       ║    ║       ║    ║          ╔╗     ║       ║       ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝     ╩       ╩       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║  ╔═════╗   ╔╗       ╔╗   ╔═════╗    ╔╗      ╦                               ║
║ ╔╝     ╚╗   ║       ║   ╔╝     ╚╗   ║╚╗     ║                               ║
║ ║       ║   ╚╗     ╔╝   ║       ║   ║ ╚╗    ║                               ║
║ ║       ║    ║     ║    ║       ║   ║  ╚╗   ║                               ║
║ ╠═══════╣    ╚╗   ╔╝    ╠═══════╣   ║   ╚╗  ║  ╠═════╣                      ║
║ ║       ║     ║   ║     ║       ║   ║    ╚╗ ║                               ║
║ ║       ║     ╚╗ ╔╝     ║       ║   ║     ╚╗║                               ║
║ ╩       ╩      ╚═╝      ╩       ╩   ╩      ╚╝                               ║
║                                                                             ║
║                                                                             ║
║                             ╔═══════╗   ╔═════╗  ╔══════╗    ╔═════╗        ║
║                                    ╔╝  ╔╝     ╚╗ ║      ╚╗  ╔╝     ╚╗       ║
║                                   ╔╝   ║       ║ ║       ║  ║       ║       ║
║                                  ╔╝    ║       ║ ║       ║  ║       ║       ║
║                               ╔══╝     ╠═══════╣ ║       ║  ║       ║       ║
║                              ╔╝        ║       ║ ║       ║  ║       ║       ║
║                             ╔╝         ║       ║ ║      ╔╝  ╚╗     ╔╝       ║
║                             ╚═══════╝  ╩       ╩ ╚══════╝    ╚═════╝        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝''')
pausa()
limpiar()
init()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                                                                             ║
║                                                                             ║
║                          print                                              ║
║                          variables (objetos con un dato)                    ║
║                              -int,                                          ║
║                              -float,                                        ║
║                              -reales,                                       ║
║                              -booleanas,                                    ║
║                              -¿strings?                                     ║
║                          type()                                             ║
║                          casting                                            ║
║                          condicional if else elif                           ║
║                          operadores                                         ║
║                              - + - * / // % **                              ║
║                              - de asignacion = += -= *= /=                  ║
║                              - de relacion == < <= > >= !=                  ║
║                              - de logica not is or in                       ║
║                          bucles while                                       ║
║                          colecciones(objetos con multiples datos)           ║
║                              -listas, Tuplas                                ║
║                              -   append, pop, insert, index, remove, sort,  ║
║                              -   min, max, sum                              ║
║                              -set, fs                                       ║
║                              -diccionarios                                  ║
║                          bucles for                                         ║
║                          continue / break                                   ║
║                          archivos externos TX, json open                    ║
║                              - r read / w write / a append / x crear,       ║
║                              - b binrios,                                   ║
║                              - json load dump,                              ║
║                              - pickle,                                      ║
║                              -                                              ║
║                          lista de palabras reservadas                       ║
║                          Funciones built-in / integradas                    ║
║           https://docs.python.org/es/3.13/library/functions.html            ║
║                                                                             ║
║                          Funciones estandar                                 ║
║                              -argumentos posicionales                       ║
║                              -argumentos arbitrarios posicionales (*args),  ║
║                              -Keywords arguments número arbitrario(**kwargs)║
║                              -argumentos por omisión                        ║
║                               return                                        ║
║                               agrupar - desagrupar                          ║
║                          ambitos de objetos (variables - colecciones)       ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║   ╔══════╗     ╔═══════╗    ╔══════╗     ╔═════╗     ╔═════╗     ╔═════╗    ║
║   ║      ╚╗    ║            ║      ╚╗   ╔╝     ╚╗   ╔╝     ╚╗   ╔╝     ╚╗   ║
║   ║       ║    ║            ║       ║   ║       ║   ║           ║       ║   ║
║   ║      ╔╝    ║            ║      ╔╝   ║       ║   ╚╗          ║       ║   ║
║   ╠══╦═══╝     ╠═════╣      ╠══════╝    ╠═══════╣    ╚═════╗    ║       ║   ║
║   ║  ╚═╗       ║            ║           ║       ║          ╚╗   ║       ║   ║
║   ║    ╚═╗     ║            ║           ║       ║   ╚╗     ╔╝   ╚╗     ╔╝   ║
║   ╩      ╚═    ╚═══════╝    ╩           ╩       ╩    ╚═════╝     ╚═════╝    ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
Las palabras clave assert, try, except, finally y raise están relacionadas con las excepciones, y nos permiten tratar el qué hacer
cuando las cosas no salen como esperamos. El siguiente código intenta hacer un cast de cadena a entero, manejando un posible error.
Si x="10" el casteo se realiza sin problemas, ya que es posible representar esa cadena como un entero.
Sin embargo hay que estar preparados siempre para lo peor.
Si x="a" no se podría hacer int() y tendríamos un error.
Si no manejamos este error, el programa se pararía, y esto no es algo deseable.
El uso de try, except y finally nos permite controlar dicho error y actuar en consecuencia sin que el programa se pare.
''')
#######################################################################################################
#######################################################################################################
pausa()
limpiar()
obj=9
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id  (obj)=}
""")
print ("*"*50)##########################################################
print ("*"*50)##########################################################
print ("*"*50)###################   C L A S E   ########################
print ("*"*50)##########################################################
print ("*"*50)######################## I I #############################
print ("*"*50)##########################################################
print ("*"*50)##########################################################





obj = "pepe"
print (f"""
{obj=}
{type(obj)=}
{id(obj)=}
""")


col =[ 4,4,9,3.5 ,"pepe", False]
print (f"""
{col=}
{type(col)=}
{id(col)=}
--------------------
{col[0]=}
{type(col[0])=}
{id(col[0])=}

{col[1]=}
{type(col[1])=}
{id(col[1])=}

{col[2]=}
{type(col[2])=}
{id(col[2])=}

{col[3]=}
{type(col[3])=}
{id(col[3])=}

{col[4]=}
{type(col[4])=}
{id(col[4])=}

{col[5]=}
{type(col[5])=}
{id(col[5])=}
""")
pausa()

obj = "hola MuNdO It"
print (f"""
{obj=}
{type(obj)=}
""")
"""
dir (obj)=['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
print (f"""
{obj.upper()=}
{type(obj.upper())=}
""")
print (f"""
{obj.lower()=}
{type(obj.lower())=}
""")
print (f"""
{obj.capitalize()=}
{type(obj.capitalize())=}
""")


print (f"""
{obj.rjust(50)=}
{type(obj.rjust(50))=}
""")
print (f"""
{obj.ljust(50)=}
{type(obj.ljust(50))=}
""")
print (f"""
{obj.center(50)=}
{type(obj.center(50))=}
""")

print (f"""
{obj.center(50).upper()=}
{type(obj.center(50).upper())=}
""")

print ("*"*50)
print ("*","METODOS DE ESTILO".center(46),"*")
print ("*"*50)
m=['capitalize', 'casefold',  'lower', 'swapcase', 'title', 'translate', 'upper']

print ("*"*50)
print ("*","METODOS DE PLACE".center(46),"*")
print ("*"*50)
m='center',"ljust","rjust"



print ("*"*50)
print ("*","METODOS DE BOOLEANO".center(46),"*")
print ("*"*50)


m= ['capitalize', 'casefold', 'center', 'count', 'encode', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper','startswith', 'endswith']

print ("*"*50)
print ("*","METODOS DE REPLACE".center(46),"*")
print ("*"*50)
m='replace'


print ("*"*50)
print ("*","OTROS METODOS".center(46),"*")
print ("*"*50)
m =  ['count', 'encode',  'expandtabs', 'find', 'format', 'format_map', 'index', 'join', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', '', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'strip', 'translate',  'zfill']





#################################################################
# Clase_Variables_04
print(
    """\033[1;37;44m\n
╔══════════════════════════╦══════════════════════════╦══════════════════════════╗
║                          ║                          ║                          ║
║    + Suma                ║         a += b           ║           a = a + b      ║
║    - Resta               ║         a -= b           ║           a = a - b      ║
║    * Multiplicación      ║         a *= b           ║           a = a * b      ║
║    ** Exponente          ║         a **= b          ║           a = a ** b     ║
║    / División            ║         a /= b           ║           a = a / b      ║
║    // División entera    ║         a //= b          ║           a = a // b     ║
║    % Módulo              ║         a %= b           ║           a = a % b      ║
║                          ║                          ║                          ║
╚══════════════════════════╩══════════════════════════╩══════════════════════════╝\033[0;m
"""
)
# Precedencia (jerarquía) de operadores:

from math import sqrt

resultado = 5 / 2 + 4
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 4 + 5 / 2
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 5 / (2 + 4)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 5 / (2 + 4) + sqrt(25)
resultado = 5 / (2 + 4) + (25**(1/2))
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 25 ** 1 / 2
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 25 ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = (13 + 3) ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = sum(numeros[0:5])
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

numero = -100

resultado = -(100 ** (1 / 2))
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = -(numero ** (1 / 2))
print("El contenido de la variable `resultado` es:", resultado)
print("Tipo de dato de la variable `resultado`:", type(resultado).__name__)

pausa()
#################################################################

resultado = (-numero) ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)
print("Tipo de dato de la variable `resultado`:", type(resultado).__name__)

#################################################################
a = 1
b = 2
c = 3
d = 16

resultado = a / (b * c) / d ** (1 / 2) ** 3

print("Resultado:", resultado)

pausa()
#################################################################

e = 7

resultado = (a ** 3) ** 2 - b * c / (d * e)

print("Resultado:", resultado)
#################################################################

numero = int(input("Ingrese un numero: "))

if numero >= 0:
    factorial = 1

    if numero == 0 or numero == 1:
        factorial = 1
    else:
        for i in range(1, numero + 1):
            factorial *= i

    print(f"{numero}! = {factorial}")
else:
    print(
        "MENSAJE: Ha escrito un valor negativo. La función factorial no está definida para los números negativos."
    )
#################################################################
from decimal import Decimal as D
dato= 0.1+0.2
print (dato)
print( D("0.1")+ D("0.2"))
dato=D(0.1+0.2)
print (dato)

dato=D("0.1")+ D("0.2")
print (dato)
#################################################################
# ~ #pip install Fraction
from fractions import Fraction as F

print ("en fraccion: ",F(1.5))
print ("en fraccion: ",F(4.10))
print ("en fraccion: ",F(8.5))
# ~ #################################################################
import random
for x in range(11):
	print (f"Numero aleatorio en {x} lugar:",random.randrange(1,1000))
#################################################################
lista = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
print ("lista original:",lista)

print ("random.choice(lista):",random.choice(lista))
random.shuffle(lista)
print ("random.shuffle(lista):",lista)

#################################################################
print ("random.random():",random.random())

dato = 8
print (f"{dato=} {type(dato)=}  {id(dato)} ")
#--------------------------------------------------

dato = 3.14159
print (f"{dato=} {type(dato)=}  {id(dato)} ")
#--------------------------------------------------

dato = "Ariel"
print (f"{dato=} {type(dato)=}  {id(dato)} ")
#--------------------------------------------------


datos = [8,3.14159,"Ariel"]

print (f"{datos=} {type(datos)=}  {id(datos)} ")
print (f"{datos[0]=} {type(datos[0])=}  {id(datos[0])} ")
print (f"{datos[1]=} {type(datos[1])=}  {id(datos[1])} ")
print (f"{datos[2]=} {type(datos[2])=}  {id(datos[2])} ")
#--------------------------------------------------
