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

pausa()
limpiar()

def por_2(x):
    print (f"en la funcion x vale {x} coleccion")
    x.append("NUEVO!!!!!!!!!!!!")
    return x*2
    


x = [9,7,5,3,1,2,4,6,8,10]

print (f"ANTES de la funcion x vale {x}")

resultado = por_2(x)
print (f"{resultado=}")
print (f"DESPUES de la funcion x vale {x}")
print ("*"*50)
x = por_2(x)
print (f"DESPUES de la funcion x vale {x}")



print ("*"*50)

#######################################################################################################

pausa()
x = [9,7,5,3,1,2,4,6,8,10]
def por_2():
    print (f"""en la funcion x vale {x}
    #scope o ambito de solo lectura para coleccion""")
    x.append("NUEVO!!!!!!!!!!!!")
    print (f"""en la funcion x vale {x}""")


print (f"ANTES de la funcion x vale {x}")
print (f"{por_2()=}")
print (f"DESPUES de la funcion x vale {x}")

print ("*"*50)
#######################################################################################################

pausa()
x = [9,7,5,3,1,2,4,6,8,10]
def por_2():
    x = [9,8,7]
    print (f"""en la funcion x vale {x}
    #scope o ambito de solo lectura para coleccion""")
    x.append("NUEVO!!!!!!!!!!!!")
    print (f"""en la funcion x vale {x}""")
    # estoy tratando de escribir una variable de solo lectura - creada fuera de la funcion
    #pide que se pase ccomo parametro o se cree una dentro
    

print (f"ANTES de la funcion x vale {x}")
print (f"{por_2()=}")
print (f"DESPUES de la funcion x vale {x}")
print ("*"*50)
#######################################################################################################
