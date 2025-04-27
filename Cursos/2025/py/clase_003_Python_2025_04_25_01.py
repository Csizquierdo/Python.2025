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
print ("*"*50)################ P A R A   C L A S E #####################
print ("*"*50)##########################################################
print ("*"*50)######################## I I I ###########################
print ("*"*50)##########################################################
print ("*"*50)##########################################################

"""
slicing (4)
diccionarios
set
funciones builtin
funciones propias
                parametros  -   argumentos
        entrada
        salida
Ambitos        

funciones de orden superior 
                            map
                            filter
                            reduce
                            enumerate
                            zip
funciones lambda

instalamos SQL
"""


vector = [0,1,2,3,4,5,6,7,8,9]
print (f"{vector=}")
print (f"{vector[ : ]=}")
print (f"{vector[3:7]=}")
print (f"{vector[3: ]=}")
print (f"{vector[ :7]=}")
ultimo = len(vector)-1
print (f"{vector[ultimo]=}")
print (f"{vector[-1]=}")
print (f"{vector[3:7]=}")
print (f"{vector[3:-3]=}")
print (f"{vector[-7:-3]=}")
print (f"{vector[-7:7]=}")


pausa()
limpiar()
lista = list()
lista = [1,9,5,4]
tupla = tuple()
tupla = ()
lista [1]=99
dic = dict()
dic = { "A":1,
        "B":True,
        "C":6,
        "g":88
    }
print (f"""
{dic=}
{type(dic)=}
{len(dic)=}
{id(dic)=}
{dir(dic)=}
""")
"""
type(dic)=<class 'dict'>
len(dic)=4
id(dic)=2420235407040
dir(dic)=['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 



'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""
    
    
    
    
dic["f"]="Feo"
print (f"{dic=}")
dic["f"]="Feliz"
print (f"{dic=}")
dic["g"]="GRANDE"
print (f"{dic=}")

dic["nuevo"]="g"
print (f"""
{dic=}
{type(dic)=}
{len(dic)=}
{id(dic)=}
{"*"*50}
{dic.items()=}
{dic.keys()=}
{dic.values()=}
""")
for cada_clave, cada_valor in dic.items():
    print (f"""
    {cada_clave=}   {cada_valor=}""")
print ("*"*50)
for cada_clave in dic.keys():
    print (f"""
    {cada_clave=}   {dic[cada_clave]=}""")
print ("*"*50)



if 6 in dic.keys():
    print ("6 es clave del diccionario")
else:
    print ("6 no es clave del diccionario")


if 6 in dic.values():
    print ("6 es valor del diccionario")
else:
    print ("6 no es valor del diccionario")
#-----------------------------------------------------
#-----------------------------------------------------
if "G" in dic.keys():
    print ("'G' es clave del diccionario")
else:
    print ("'G' no es clave del diccionario")
#-----------------------------------------------------

if 'G' in dic.values():
    print ("'G' es valor del diccionario")
else:
    print ("'G' no es valor del diccionario")
#-----------------------------------------------------
#-----------------------------------------------------
if 'g'in dic.keys():
    print ("'g' es clave del diccionario")
else:
    print ("'g' no es clave del diccionario")

#-----------------------------------------------------
if 'g' in dic.values():
    print ("'g' es valor del diccionario")
else:
    print ("'g' no es valor del diccionario")






print (f"""{dic.get("g","la 'g' no es clave")=}""")
print (f"""{dic.get("h","la 'h' no es clave")=}""")
variable = ""
while variable not in dic.keys():
    variable = input (f"ingrese una opción entre {dic.keys()} ")
    print (f"""{dic.get(variable,f"la '{variable}' no es clave")=}""")



vector = [0,1,2,3,4,5,6,7,8,9]
dic= dict().fromkeys(vector,"blanco")
print (f"""
{dic=}
{type(dic)=}
{len(dic)=}
{id(dic)=}
{"*"*50}
{dic.items()=}
{dic.keys()=}
{dic.values()=}
""")

variable = "directorio"
vector2 = list(variable)
dic= dict(zip(vector,vector2))
print (f"""
{vector=}
{vector2=}
{dic=}
{type(dic)=}
{len(dic)=}
{id(dic)=}
{"*"*50}
{dic.items()=}
{dic.keys()=}
{dic.values()=}
""")












exit()
conj = set()
conj = {}











