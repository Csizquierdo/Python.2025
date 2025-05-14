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

pausa()
limpiar()

"""
funciones de orden superior
"""
def funciones_map():
    lista = [1,2,3,4,5,6,7,8,9]
    def por_2(x):
        return x*2
    regreso = []
    for cada_dato in lista:
        regreso.append(por_2(cada_dato))

    print (f"""
    {lista=}
    {regreso=}
    """)
    pausa()

    #######################################################################################################

    def por_2(lista):
        regreso = []
        for cada_dato in lista:
            regreso.append(cada_dato*2)
        return regreso

    lista = [1,2,3,4,5,6,7,8,9]
    regreso =   por_2(lista)
    print (f"""
    {lista=}
    {regreso=}
    """)
    pausa()

    #######################################################################################################

    lista = [1,2,3,4,5,6,7,8,9]
    def por_2(x):
        return x*2

    regreso = map(    por_2    , lista)
    #        F.O.S\____________/\_____/
    #                funcion    coleccion    
    print (f"""
    {lista=}
    {regreso=}
    {list(regreso)=}
    """)
    pausa()

    ######################################################################################################

    lista = [1,2,3,4,5,6,7,8,9]

    regreso = map(lambda x : x*2, lista)
    #        F.O.S\____________/\_____/
    #                funcion    coleccion    
    print (f"""
    {lista=}
    {regreso=}
    {list(regreso)=}
    """)
    ######################################################################################################

# ~ funciones_map()

#######################################################################################################
#######################################################################################################
#######################################################################################################
def funciones_filter():

    lista = [1,2,3,4,5,6,7,8,9]
    def cual_es_impar(x):
        if x%2!=0:
            return True
        else:
            return False
        # ~ return None

    regreso = []
    for cada_dato in lista:
        es_true = cual_es_impar(cada_dato)
        if es_true is True:
            regreso.append(cada_dato)

    print (f"""
    {lista=}
    {regreso=}
    """)
    pausa()

    #######################################################################################################

    lista = [1,2,3,4,5,6,7,8,9]
    def cual_es_impar(x):
        if x%2!=0:
            return True
        else:
            return False
        # ~ return None

    regreso = filter (cual_es_impar,lista)
    #          F.O.S  \____________/\_____/
    #                funcion    coleccion 


    print (f"""
    {lista=}
    {regreso=}
    {list(regreso)=}

    """)
    pausa()


    #######################################################################################################

    lista = [1,2,3,4,5,6,7,8,9]
    regreso = filter (lambda x: True if x%2!=0 else False ,lista)
    #          F.O.S  \___________________________________/\_____/
    #                                funcion            coleccion 


    print (f"""
    {lista=}
    {regreso=}
    {list(regreso)=}

    """)
    pausa()

#######################################################################################################
#######################################################################################################
#######################################################################################################
# ~ funciones_filter()

from functools import reduce


lista = [1,2,3,4,5,6,7,8,9]


regreso = reduce (lambda x, y : x + y, lista)
print (f"""
{lista=}
{regreso=}
""")
pausa()


media = (reduce (lambda x, y : x + y, lista))/len(lista)
print (f"""
{lista=}
{media=}
""")
pausa()

print ("*"*50)##########################################################
print ("*"*50)##########################################################
print ("*"*50)################ P A R A   C L A S E #####################
print ("*"*50)##########################################################
print ("*"*50)########################  I V  ###########################
print ("*"*50)##########################################################
print ("*"*50)##########################################################

"""
@ operadores ternarios
@ listas por comprension 
@ funciones anonimas lambda
"""
