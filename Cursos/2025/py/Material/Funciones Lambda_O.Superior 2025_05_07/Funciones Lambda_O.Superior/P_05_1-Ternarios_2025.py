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
def ya_hechos():
    pass
print(Back.GREEN+"""\n
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
╠═════════════════════════════════════════════════════════════════════════════╣"""+Style.RESET_ALL+Back.BLUE+"""
║                                                                             ║
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
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝"""+Back.RESET)
pausa()
limpiar()
print(Back.GREEN+"""\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║  ╔═════╗  ╔════╗  ╔╗      ╦ ╔═════╗  ╦  ╔════╗  ╦   ╔════╗                  ║
║ ╔╝       ╔╝    ╚╗ ║╚╗     ║ ║     ╚╗ ║ ╔╝    ╚╗ ║  ╔╝    ╚╗                 ║
║ ║        ║      ║ ║ ╚╗    ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ║        ║      ║ ║  ╚╗   ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ║        ║      ║ ║   ╚╗  ║ ║      ║ ║ ║        ║  ║      ║ ╠═════╝         ║
║ ║        ║      ║ ║    ╚╗ ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ╚╗       ╚╗    ╔╝ ║     ╚╗║ ║     ╔╝ ║ ╚╗    ╔╝ ║  ╚╗    ╔╝                 ║
║  ╚════╝   ╚════╝  ╩      ╚╝ ╚═════╝  ╩  ╚════╝  ╩   ╚════╝                  ║
║                                                                             ║
║                                                                             ║
║                           ╔╗      ╦   ╔════╗  ╦         ╔══════╗  ╔════╗    ║
║                           ║╚╗     ║  ╔╝    ╚╗ ║         ║        ╔╝    ╚╗   ║
║                           ║ ╚╗    ║  ║      ║ ║         ║        ║          ║
║                           ║  ╚╗   ║  ║      ║ ║         ║        ╚╗         ║
║                           ║   ╚╗  ║  ╠══════╣ ║         ╠═════╝   ╚════╗    ║
║                           ║    ╚╗ ║  ║      ║ ║         ║              ╚╗   ║
║                           ║     ╚╗║  ║      ║ ║         ║        ╚╗    ╔╝   ║
║                           ╩      ╚╝  ╩      ╩ ╚══════╝  ╚══════╝  ╚════╝    ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣"""+Style.RESET_ALL+Back.BLUE+"""
║                                                                             ║
║ ╔══╦══╗ ╔═════╗ ╔═════╗   ╔╗      ╦  ╔════╗   ╔═════╗   ╦  ╔════╗   ╔════╗  ║
║    ║    ║       ║     ╚╗  ║╚╗     ║ ╔╝    ╚╗  ║     ╚╗  ║ ╔╝    ╚╗ ╔╝    ╚╗ ║
║    ║    ║       ║      ║  ║ ╚╗    ║ ║      ║  ║      ║  ║ ║      ║ ║        ║
║    ║    ║       ║     ╔╝  ║  ╚╗   ║ ║      ║  ║     ╔╝  ║ ║      ║ ╚╗       ║
║    ║    ╠════╝  ╠═══╦═╝   ║   ╚╗  ║ ╠══════╣  ╠═══╦═╝   ║ ║      ║  ╚════╗  ║
║    ║    ║       ║   ╚╗    ║    ╚╗ ║ ║      ║  ║   ╚╗    ║ ║      ║       ╚╗ ║
║    ║    ║       ║    ╚╗   ║     ╚╗║ ║      ║  ║    ╚╗   ║ ╚╗    ╔╝ ╚╗    ╔╝ ║
║    ╩    ╚═════╝ ╩     ╚╝  ╩      ╚╝ ╩      ╩  ╩     ╚╝  ╩  ╚════╝   ╚════╝  ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝"""+Back.RESET)
pausa()
limpiar()
print(
    """\033[1;37;44m\n
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
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                            operadores temarios                              ║
║                                                                             ║
║                                 "if else"                                   ║
║                                 <,>,==,!=                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""")
print("""Un operador temario en python evalua la condición entre True / False y 
         sobre esto da una salida usando una sola linea de comando. super compacto""")

import this
# ~ import random


def operador_ternario():
    x = 0
    if x < 0:
        print ("negativo")
    else:
        print ("no negativo")



    if x < 0:
        print ("negativo")
    else:
        if x> 0:
            print ("positivo")
        else:
            print ("cero es neutro")


    if x < 0:
        print ("negativo")
    elif x> 0:
        print ("positivo")
    else:
        print ("cero es neutro")


    print ("*"*50)#---------------------------------------------------------
    print ("operador ternario")
    print ( "negativo"      if x < 0    else       "no negativo"   )

    salida =  "negativo"      if x < 0    else       "no negativo"   
    print (f"{salida=}")

    salida =  "negativo"      if x < 0    else   ( "positivo" if x> 0 else "cero es neutro"  )  
    print (f"{salida=}")

    print ("*"*50)#---------------------------------------------------------


########################################################################
# ~ operador_ternario()
########################################################################



def por_comprension():
    entrada = [-5,8,-7,-9,-1,2,3,4,0,-4,1,-1]
    salida  = []

    #   por extension
    for x in entrada:
        if x < 0:
            salida.append(f"negativo {x}")
        elif x> 0:
            salida.append (f"positivo {x}")
        else:
            salida.append (f"cero es neutro {x}")

    print (f"""
    {entrada=}
    {salida=}
    """)
    print ("*"*50)#---------------------------------------------------------
    # mitad extension + operador ternario (no se usa)
    for x in entrada:
        salida.append("negativo"      if x < 0    else   ( "positivo" if x> 0 else "cero es neutro"  )  )

    print (f"""
    {entrada=}
    {salida=}
    """)
    print ("*"*50)#---------------------------------------------------------

    salida2= ["negativo"      if x < 0    else   ( "positivo" if x> 0 else "cero es neutro"  )  for x in entrada ]
    print (f"""
    lista por comprension - one line comprehension list
    {entrada=}

    {salida2=}

    {type(salida2)=}

    """)

    print ("*"*50)#---------------------------------------------------------



    salida2= ("negativo"      if x < 0    else   ( "positivo" if x> 0 else "cero es neutro"  )  for x in entrada )

    salida3 = list(salida2)


    print (f"""
    generador por comprension - one  line comprehension generator
    {entrada=}

    {salida2=}

    {type(salida2)=}
    {salida3=}

    {type(salida3)=}

    {list(salida2)=}

    """)
    print ("*"*50)#---------------------------------------------------------


    salida2= tuple("negativo"      if x < 0    else   ( "positivo" if x> 0 else "cero es neutro"  )  for x in entrada )




    print (f"""
    tupla por comprension - one  line comprehension tuple
    {entrada=}

    {salida2=}

    {type(salida2)=}

    {list(salida2)=}

    """)

    print ("*"*50)#---------------------------------------------------------

    salida2= {"negativo"      if x < 0    else   ( "positivo" if x> 0 else "cero es neutro"  )  for x in entrada }


    print (f"""
    conjunto por comprension - one  line comprehension set
    {entrada=}

    {salida2=}

    {type(salida2)=}

    {list(salida2)=}

    """)



    print ("*"*50)#---------------------------------------------------------
    salida2  = {}
    #   por extension
    for x in entrada:
        if x < 0:
            salida2[x]="negativo"
        elif x> 0:
            salida2[x]="positivo"
        else:
            salida2[x]="cero es neutro"

    print (f"""
    diccionario por extension
    {entrada=}
    {salida2=}
    {type(salida2)=}
    {list(salida2)=}
    """)


    salida2= {x: "negativo"      if x < 0    else   ( "positivo" if x> 0 else "cero es neutro"  )  for x in entrada }
    print (f"""
    diccionario por comprension - one  line comprehension dicc
    {entrada=}
    {salida2=}
    {type(salida2)=}
    {list(salida2)=}
    """)


    print ("*"*50)#---------------------------------------------------------
########################################################################
# ~ por_comprension()
########################################################################

def filtro():
    entrada = [-5,8,-7,-9,-1,2,3,4,0,-4,1,-1]
    salida  = []

    #   por extension
    for x in entrada:
        if x < 0:
            salida.append(x)
        


    salida2= [x     for x in entrada  if x < 0     ]

    print (f"""

    {entrada=}
    extension {salida=}
    comprension {salida2=}
    {type(salida2)=}
    """)




print ("*"*50)#---------------------------------------------------------

entrada = [-5,8,-7,-9,-1,2,3,4,0,-4,1,-1]
salida2={}
def funcion(x):
    #param \_/
    #ingreso
    if x < 0:
        salida2[x]="negativo"
    elif x> 0:
        salida2[x]="positivo"
    else:
        salida2[x]="cero es neutro"
        
    # salida2 es el parametro de salida
    # ~ return salida2

for x in entrada:
    funcion(x)

salida3 = lambda entrada:{x :"negativo" if x < 0 else ("positivo" if x> 0 else "cero es neutro") for x in entrada }
#param entrada    \____/ \_____________________________________________dic salida_________________________________/
print (f"""

{entrada=}
extension {salida2=}
comprension {salida3(entrada)=}
{type(salida2)=}
""")
exit()




print("*"*100)#-------------------------------------------------------------
pausa()
limpiar()

a=2
b=1
c="SI"
d="no"
#print (f"tiene {(A>B)?C:D}")
print("condition_if_true if condition else condition_if_false")
print('si a > b---', c if (a > b) else d, '---c o d!');
print("*"*100)#-------------------------------------------------------------
anda = True# remplazar con False
estado = "si: el codigo corre" if anda \
                                        else "bug: no, el codigo no corre"
print("estado del programa ", estado)
print("*"*50)
print("*"*100)#-------------------------------------------------------------

pausa()
limpiar()
############################################################################
print("Otra forma (no muy usada) es la siguiente:")
print("tupla + [booleano 0 o 1]")
print("if_test_is_false, if_test_is_true)[test]")
print("*"*100)#-------------------------------------------------------------
anda = True#1
lista = ["bug: no, el codigo no corre","si: el codigo corre" ]
estado = lista[False]
print("estado del programa ", estado)
estado = ["bug: no, el codigo no corre","si: el codigo corre"][anda]
print("estado del programa ", estado)
print("*"*100)#-------------------------------------------------------------
anda = True
print(lista[1] if anda else lista[0])# ternario
print(lista[anda])#slicing

anda = False
print(lista[1] if anda else lista[0])# ternario
print(lista[anda])#slicing

############################################################################
#                 ______________--------->demas si es booleana
#                /              \
coleccion = [9,6,3,2,5,8,7,4,1,0]
#        False |
#              True verdadero
print (f"{coleccion=}")
print (f"{coleccion[True]=}")
print (f"{coleccion[1]=}")

print (f"{coleccion[False]=}")
print (f"{coleccion[0]=}")


print (f"{coleccion[5]=}")
print (f"{coleccion[7]=}")









