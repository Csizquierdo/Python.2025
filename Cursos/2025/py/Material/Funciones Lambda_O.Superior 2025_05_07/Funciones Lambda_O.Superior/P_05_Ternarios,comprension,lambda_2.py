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
def ternarios():
    pass
    print(F'''{Fore.WHITE+ Style.BRIGHT + Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                                                                             ║
    ║    ╔═══════╗            ╦                                                   ║
    ║    ║                    ║                                                   ║
    ║    ║                    ║                                                   ║
    ║    ║                    ║                                                   ║
    ║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗                         ║
    ║    ║            ║       ║    ║       ║    ║                                 ║
    ║    ║            ║       ║    ║       ║    ║          ╔╗                     ║
    ║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝                     ║
    ║                                                                             ║
    ║                                                                             ║
    ║                                                                             ║
    ║              ╦     ╔═════╗     ╔═══╦═══╗   ╔═══════╗     ╔═════╗            ║
    ║              ║    ╔╝     ╚╗        ║       ║            ╔╝     ╚╗           ║
    ║              ║    ║                ║       ║            ║       ║           ║
    ║              ║    ╚╗               ║       ║            ║       ║           ║
    ║              ║     ╚═════╗         ║       ╠══════╣     ╠═══════╣           ║
    ║              ║           ╚╗        ║       ║            ║       ║           ║
    ║              ║    ╚╗     ╔╝        ║       ║            ║       ║           ║
    ║              ╩     ╚═════╝         ╩       ╚═══════╝    ╩       ╩           ║
    ║                                                                             ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    ║       https://docs.python.org/es/3.12/library/functions.html#reversed       ║
    ╚═════════════════════════════════════════════════════════════════════════════╝
    ''')
    pausa()



    """
    valor = 4

    ################################################################
    if valor %2!=0:
        print ("impar")
    else:
        print ("par")
    print ("*"*50)
    print ( "impar" if valor %2!=0 else "par")
    ################################################################
    print ("-"*50)
    if valor %2!=0:
        print ("impar")
    elif valor ==0:
        print ("neutro")
    else:
        print ("par")
    print ("*"*50)
    print ( "impar" if valor %2!=0 else ("neutro" if valor ==0 else "par") )
    ################################################################
    tipo_valor ="impar" if valor %2!=0 else ("neutro" if valor ==0 else "par")
    print (f"{tipo_valor=}")
    print ("-"*50)

    """
################################################################
# ternarios()
################################################################
def one_line():

    #one line comprehension list
    entrada = [9,5,1,4,2,3,6,7,5,1,0,3,6,9,8,5,2,1,4,7,0]


    salida= [] #entrada * 2

    for cada_dato in entrada:
        salida.append(cada_dato*2)

    print(f"""
    {entrada=}
    {salida =}
    """)
    print ("*"*50)
    ################################################################


    salida_c = [cada_dato*2 for cada_dato in entrada]

    print(f"""
    {entrada = }
    {salida_c= }
    """)
    print ("-"*50)
    ################################################################
    entrada = [9,5,1,4,2,3,6,7,5,1,0,3,6,9,8,5,2,1,4,7,0]


    salida= [] #entrada * 2 si es >5 , sino * 10

    for cada_dato in entrada:
        if cada_dato >5:
            salida.append(cada_dato*2)
        else:
            salida.append(cada_dato*10)
    print(f"""
    {entrada=}
    {salida =}
    """)
    print ("*"*50)



    salida_c = [cada_dato*2 if cada_dato >5 else cada_dato*10 for cada_dato in entrada]

    print(f"""
    {entrada  =}
    {salida_c =}
    """)


    salida_c = ["impar" if cada_dato %2!=0 else ("neutro" if cada_dato ==0 else "par") for cada_dato in entrada]

    print(f"""
    {entrada  =}
    {salida_c =}
    """)
    #one line comprehension dic


    ################################################################
    entrada = [9,5,1,4,2,3,6,7,5,1,0,3,6,9,8,5,2,1,4,7,0]


    salida= {}  #           clave = entrada : salidas= entrada * 2 

    for cada_dato in entrada:
        salida[cada_dato]=cada_dato*2

    print ("extencion:",salida)
    for clave, valor in salida.items():
        print (f"extencion {clave}--->{valor}")

    salida= {}  #           clave = entrada : salidas= entrada * 2 si es >5 , sino * 10
    print ("*"*50)
    salida_c_d = {cada_dato : cada_dato*2 for cada_dato in entrada}

    print ("comprension:",salida_c_d)
    for clave, valor in salida_c_d.items():
        print (f"comprension {clave}--->{valor}")
    print ("-"*50)
    ################################################################
    pausa()
    limpiar()
    for cada_dato in entrada:
        if cada_dato > 5:
            salida[cada_dato]=cada_dato*2
        else:
            salida[cada_dato]=cada_dato*10
    print ("extencion:",salida_c_d)
    for clave, valor in salida.items():
        print (f"extencion {clave}--->{valor}")
    salida_c_d = {cada_dato : cada_dato*2 if cada_dato>5 else  cada_dato *10 for cada_dato in entrada}

    print ("comprension:",salida_c_d)
    for clave, valor in salida_c_d.items():
        print (f"comprension {clave}--->{valor}")
    print ("-"*50)
    ################################################################
    entrada = [9,5,1,4,2,3,6,7,5,1,0,3,6,9,8,5,2,1,4,7,0]
    salida={}
    for cada_dato in entrada:
        if cada_dato %2!=0:
            sal= "impar"
        elif cada_dato ==0:
            sal= "neutro"
        else:
            sal= "par"
        salida[cada_dato]=sal
    for clave, valor in salida.items():
        print (f"extencion {clave}--->{valor}")
    print ("*"*50)

    salida={cada_dato: "impar" if cada_dato %2!=0 else ("neutro" if cada_dato ==0 else "par") for cada_dato in entrada}

    for clave, valor in salida.items():
        print (f"comprension {clave}--->{valor}")

    print ("-"*50)
    pausa()
    limpiar()
    import this
################################################################
# ~ one_line()
################################################################
def filtro():


    ################################################################
    #                           filtro
    ################################################################
    entrada = [9,5,1,4,2,3,6,7,5,1,0,3,6,9,8,5,2,1,4,7,0]

    salida = [dato*2  for dato in entrada]
    print (f"""
    {entrada=}
    {salida=}
    """)

    salida = [dato*2 if dato%2!=0 else dato**2 for dato in entrada]
    print (f"""
    {entrada=}
    {salida=}
    """)



    salida = [True if dato<5 else False for dato in entrada]
    print (f"""
    {entrada=}
    {salida=}
    """)


    filtro = [dato  for dato in entrada   if dato<5  ]
    print (f"""
    {entrada=}
    {filtro=}
    """)

    entrada_dic={"Ariel":10,"Beto":1,"Carla":9,"Dany":3,"Esty":2}



    filtro = [nombre  for nombre,edad in entrada_dic.items() if edad<5  ]
    print (f"""
    {entrada_dic=}
    {filtro=}
    """)

    filtro = {nombre:edad  for nombre,edad in entrada_dic.items() if edad<5  }
    print (f"""
    {entrada_dic=}
    {filtro=}
    """)
################################################################
# ~ filtro()
################################################################

################################################################
#                       lambda
################################################################


def sumar (d1,d2):
    """
    docstring
    """
    return d1+d2
    
    
print (f"{sumar(2,6)=}")

sumar_l= lambda e1,e2 : e1+e2
print (f"{sumar_l(2,6)=}")
print (f"{sumar_l(1,2)=}")
print (f"{sumar_l(77,2)=}")


def mayor (d1,d2):
    """
    docstring
    """
    if d1 > d2:
        return d1
    elif d1 < d2:
        return d2
    else: #son iguales
        return "="
    
print (f"{mayor(2,6)=}")
print (f"{mayor(1,2)=}")
print (f"{mayor(77,2)=}")


mayor_l= lambda e1,e2 : e1 if e1>e2 else (e2 if e1 < e2 else "=" )
print (f"{mayor_l(2,6)=}")
print (f"{mayor_l(1,2)=}")
print (f"{mayor_l(77,2)=}")


entrada = [9,5,1,4,2,3,6,7,5,1,0,3,6,9,8,5,2,1,4,7,0]

true_false = lambda entrada : [True if dato%2!=0 else False for dato in entrada]
print (f"{true_false(entrada)=}")







"""

Temario del Parcial

Compilador e intérprete
Lenguajes de alto y bajo nivel.
normas de nombres de objetos correcta e incorrecta, aceptadas por la comunidad y no aceptadas
1. Tipos de Datos y Objetos en Python
    Objetos de 1 Dato
        Enteros
        Flotantes
        Cadenas de texto
        Booleanos
        
    Objetos de Colección o Múltiples Datos
        Listas
        Tuplas
        Diccionarios
        
    Objetos Mutables
        Listas
        Diccionarios
        
    Objetos Inmutables
        Tuplas
        Cadenas de texto
        Números
2. Operadores y Expresiones
    Operadores Ternarios
        resultado = "Mayor" if x > 10 else "Menor o igual"
    Expresiones por Comprensión
        Listas: [x**2 for x in range(10)]
        Diccionarios: {x: x**2 for x in range(10)}
    Funciones Lambda
        f = lambda x: x**2
3. Funciones y Control de Flujo
    Funciones Built-in
        print()
        input()
        len()
        type()
        range()
    Estructuras de Control
        while
        for
        if, else, y elif
        match y case (Python 3.10+)
    Funciones Propias
        Definición de funciones
        Argumentos y parámetros
        Valores por defecto y *args, **kwargs
    Funciones de Orden Superior
        zip()
        enumerate()
        map()
        filter()
        reduce() (de functools)
    Funciones Recursivas
        Definición
        Caso base y caso recursivo
        Ejemplo de recursión simple (como la serie de Fibonacci)
    Funciones all() y any()
        all(iterable): Verifica si todos los elementos son verdaderos
        any(iterable): Verifica si al menos un elemento es verdadero
4. Estructuras de Datos
    FIFO (First In, First Out)
        Colas
        Implementación con listas y collections.deque
    LIFO (Last In, First Out)
        Pilas
        Implementación con listas

    """

