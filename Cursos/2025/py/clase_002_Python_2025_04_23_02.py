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




def programa_1():
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



    print ("*"*100)
    col =   4 ,4, 9, 3.5 ,"pepe", False
    col = ( 4, 4, 9, 3.5, 'pepe', False)
    print (f"""
    {col=}
    {type(col)=}
    {dir(col)=}
    {id(col)=}
    """)
    """
    type(col)=<class 'tuple'>
    dir(col)=['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',


                                'count',        'index']
    id(col)=2225980531392
    """


    col =[ 4,4,9,3.5 ,"pepe", False]
    print (f"""
    {col=}
    {type(col)=}
    {dir(col)=}
    {id(col)=}
    """)
    """
    type(col)=<class 'list'>
    dir(col)=['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 



    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    """

    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]

    print (f""" original
    {lista=}
    {len(lista)=}
    """)
    print ("*"*50)
    print ("*","METODOS DE AGREGACION".center(46),"*")
    print ("*"*50)
    m=['append', 'extend',  'insert']


    lista.append("fin")

    print (f"""   append
    {lista=}
    {len(lista)=}
    """)
    lista.extend([101,102,103,104,105,106,108,109,110])

    print (f"""   extend
    {lista=}
    {len(lista)=}
    """)



    lista.insert(0, "inicio")
    lista.insert(15, "medio")
    print (f"""   extend
    {lista=}
    {len(lista)=}
    """)




    pausa()
    print ("*"*50)
    print ("*","METODOS DE REDUCCION".center(46),"*")
    print ("*"*50)
    m=['clear', 'pop', 'remove']

    #del lista

    lista.clear()
    print (f"""   extend
    {lista=}
    {len(lista)=}
    """)
    print ("*"*50)##########################################################
    print ("*"*50)##########################################################
    print ("*"*50)###################  Fifo & Lifo  ########################
    print ("*"*50)##########################################################
    print ("*"*50)##########################################################

    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]
    salida = lista.pop()
    print (f"""   pop()--> pop (len(coleccion)-1)
    {lista=}
    {len(lista)=}
    {salida = }
    """)

    lista.pop()
    print (f"""   pop() --> pop (len(coleccion)-1)
    {lista=}
    {len(lista)=}
    {salida = }
    """)



    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]
    salida = lista.pop(0)
    print (f"""   pop (0)
    {lista=}
    {len(lista)=}
    {salida = }
    """)

    lista.pop(0)
    print (f"""   pop (0)
    {lista=}
    {len(lista)=}
    {salida = }
    """)

    # ~ lista.pop(44)#pop index out of range
    # ~ print (f"""   pop (0)
    # ~ {lista=}
    # ~ {len(lista)=}
    # ~ {salida = }
    # ~ """)
    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]
    while 5 in lista:
        salida = lista.remove(5)
        print (f"""   remove 
        {lista=}
        {len(lista)=}
        {salida = }
        """)

    # ~ lista.remove(25)#list.remove(x): x not in list
    # ~ print (f"""   remove 
    # ~ {lista=}
    # ~ {len(lista)=}
    # ~ {salida = }
    # ~ """)


    pausa()

    print ("*"*50)
    print ("*","METODOS DE INFORMACION".center(46),"*")
    print ("*","Polimorficos con tuppla".center(46),"*")
    print ("*"*50)
    m=[ 'count','index',]

    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]

    cant_de_5 = lista.count(5)
    print (f"""   count 
    {lista=}
    {len(lista)=}
    {cant_de_5 = }
    """)


    cant_de_4 = lista.count(3)
    print (f"""   count 
    {lista=}
    {len(lista)=}
    {cant_de_4 = }
    """)

    donde_esta_5_primero = lista.index(5)
    print (f"""   index 
    {lista=}
    {len(lista)=}
    {donde_esta_5_primero = }
    """)


    donde_esta_2_primero = lista.index(2)
    print (f"""   index 
    {lista=}
    {len(lista)=}
    {donde_esta_2_primero = }
    """)

    pausa()
    print ("*"*50)
    print ("*","METODOS DE ORDEN".center(46),"*")
    print ("*"*50)
    m=['reverse', 'sort']
    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]
    lista.reverse()
    print (f"""   reverse *--indices
    {lista=}
    {len(lista)=}
    """)


    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]
    lista.sort()
    print (f"""   sort  --- contenido o valor(menor a mayor) - (AZ & az)
    {lista=}
    {len(lista)=}
    """)

    lista = [9,7,5,1,2,3,6,4,8,0,2,5,7,9,4,2,6,5,1,3,1]
    lista.sort(reverse=True)
    print (f"""   sort --- contenido o valor + reverse=True + (mayor a menor ) - (za & ZA)
    {lista=}
    {len(lista)=}
    """)





    pausa()
    print ("*"*50)
    print ("*","METODO COPY (ver alias)".center(46),"*")
    print ("*"*50)
    m = "copy"
    pausa()


#################################################
#programa_1()
#################################################


escalar = 89
vector = [1,2,3,4,5,6,7,8,9,0]#coleccion de objetos  (enteros)1D
vector = [ [1,2,3],[4,5,6],[7,8,9,0],"Juan"]# coleccion de objetos (colecciones)
vector = [  [1,2,3],
            [4,5,6],
            [7,8,9,0],
            "Juan"         #[[1, 2, 3], [4, 5, 6], [7, 8, 9, 0],"Juan"]
        ]
print (f"{vector=}")

print (f"{vector[1]=}")

print (f"{vector[1][1]=}")
print (f"{vector[3]=}")
print (f"{vector[3][2]=}")



print ("*"*50)##########################################################
print ("*"*50)################ P A R A   C L A S E #####################
print ("*"*50)##########################################################
print ("*"*50)######################## I I I ###########################
print ("*"*50)##########################################################
print ("*"*50)##########################################################

"""
slicing (4)
dictcionarios
set
funciones builtin
funciones propias
                parametros  -   argumentos
        entrada
        salida
funciones de orden superior 
                            map
                            filter
                            reduce
                            enumerate
                            zip
funciones lambda

instalamos SQL
"""
























