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
from datetime import datetime, date, time

#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aquí las practicas hechas
    pass
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
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
║                              ╔══════╗   ╔═══════╗                           ║
║                              ║      ╚╗  ║                                   ║
║                              ║       ║  ║                                   ║
║                              ║       ║  ║                                   ║
║                              ║       ║  ╠══════╝                            ║
║                              ║       ║  ║                                   ║
║                              ║      ╔╝  ║                                   ║
║                              ╚══════╝   ╚═══════╝                           ║
║                                                                             ║
║                                                                             ║
║           ╔═════╗    ╔══════╗    ╔══════╗   ╔═══════╗   ╔╗      ╦           ║
║          ╔╝     ╚╗   ║      ╚╗   ║      ╚╗  ║           ║╚╗     ║           ║
║          ║       ║   ║       ║   ║       ║  ║           ║ ╚╗    ║           ║
║          ║       ║   ║      ╔╝   ║       ║  ║           ║  ╚╗   ║           ║
║          ║       ║   ╠═══╦══╝    ║       ║  ╠══════╝    ║   ╚╗  ║           ║
║          ║       ║   ║   ╚╗      ║       ║  ║           ║    ╚╗ ║           ║
║          ╚╗     ╔╝   ║    ╚╗     ║      ╔╝  ║           ║     ╚╗║           ║
║           ╚═════╝    ╩     ╚╝    ╚══════╝   ╚═══════╝   ╩      ╚╝           ║
║                                                                             ║
║                                                                             ║
║    ╔═════╗  ╦       ╦ ╔══════╗  ╔═══════╗ ╔══════╗  ╦  ╔═════╗  ╔══════╗    ║
║   ╔╝     ╚╗ ║       ║ ║      ╚╗ ║         ║      ╚╗ ║ ╔╝     ╚╗ ║      ╚╗   ║
║   ║         ║       ║ ║       ║ ║         ║       ║ ║ ║       ║ ║       ║   ║
║   ╚╗        ║       ║ ║      ╔╝ ║         ║      ╔╝ ║ ║       ║ ║      ╔╝   ║
║    ╚═════╗  ║       ║ ╠══════╝  ╠══════╝  ╠═══╦══╝  ║ ║       ║ ╠═══╦══╝    ║
║          ╚╗ ║       ║ ║         ║         ║   ╚╗    ║ ║       ║ ║   ╚╗      ║
║   ╚╗     ╔╝ ╚╗     ╔╝ ║         ║         ║    ╚╗   ║ ╚╗     ╔╝ ║    ╚╗     ║
║    ╚═════╝   ╚═════╝  ╩         ╚═══════╝ ╩     ╚╝  ╩  ╚═════╝  ╩     ╚╝    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
''');#Funciones incorporadas (map, zip, enumerate, reduce, filter).Funciones incorporadas (map, zip, enumerate, reduce, filter).
pausa();limpiar()
##################################################################################################

print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                       ╔═══════╗       ╦       ╔══════╗                      ║
║                              ╔╝       ║       ║      ╚╗                     ║
║                             ╔╝        ║       ║       ║                     ║
║                           ╔═╝         ║       ║      ╔╝                     ║
║                         ╔═╝           ║       ╠══════╝                      ║
║                        ╔╝             ║       ║                             ║
║                       ╔╝              ║       ║                             ║
║                       ╚═══════╝       ╩       ╩                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

Ej Nro 1/zip:
Con zip: lista de comprensión para devolver una lista de la misma longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un conector entre ellas.
''')
print("*"*50,"\nEj Nro 2/filter")
def concatenar(L1, L2, conector):
    return [Salida_1+conector+Salida_2 for (Salida_1,Salida_2) in zip(L1,L2)]
L1=['Don', 'Lady','Sir']
L2=['Juan','Di','Elton John']
print (f"{concatenar(L1,L2,'-')=}")
print (f"lambda {list(lambda x: x = f'{Salida_1}-{Salida_2}' for (Salida_1,Salida_2) in zip(L1,L2))}")
##################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                        ║
║                                                                                        ║
║ ╔══════╗ ╔╗      ╦  ╦      ╦ ╔╗      ╔╗ ╔══════╗ ╔═════╗   ╔════╗  ╔═══╦═══╗ ╔══════╗  ║
║ ║        ║╚╗     ║  ║      ║ ║╚╗    ╔╝║ ║        ║     ╚╗ ╔╝    ╚╗     ║     ║         ║
║ ║        ║ ╚╗    ║  ║      ║ ║ ╚╗  ╔╝ ║ ║        ║      ║ ║      ║     ║     ║         ║
║ ║        ║  ╚╗   ║  ║      ║ ║  ╚╗╔╝  ║ ║        ║     ╔╝ ║      ║     ║     ║         ║
║ ╠═════╝  ║   ╚╗  ║  ║      ║ ║   ╚╝   ║ ╠═════╝  ╠══╦══╝  ╠══════╣     ║     ╠════╝    ║
║ ║        ║    ╚╗ ║  ║      ║ ║        ║ ║        ║  ╚╗    ║      ║     ║     ║         ║
║ ║        ║     ╚╗║  ╚╗    ╔╝ ║        ║ ║        ║   ╚╗   ║      ║     ║     ║         ║
║ ╚══════╝ ╩      ╚╝   ╚════╝  ╩        ╩ ╚══════╝ ╩    ╚╝  ╩      ╩     ╩     ╚══════╝  ║
║                                                                                        ║
║                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
'''
Ej Nro 1/enumerate:
Realizar una función que tome una lista y retorne un diccionario que contenga los valores de la lista como clave y el índice como el valor. Utilizar la función enumerate.
'''
print("*"*50,"\nEj Nro 1/enumerate")
def enumerar_lista(L):
    return {key:value for value,key in enumerate(L)}
lista_=['Paloma', 'Raton', 'Gato', 'Pez' , 'Zorro' , 'Perro', 'Oso' , 'Oruga' , 'Python']
print(f"{enumerar_lista(lista_)=}")
print(f"lambda{dict(lambda key:value for value,key in enumerate(lista_))=}")
##################################################################################################
'''
Ej Nro 2/enumerate:
Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo valor es igual a su índice. Utilizar la función enumerate.
'''
print("*"*50,"\nEj Nro 2/enumerate")
def count_match_index(lista_):
    return len([num for count,num in enumerate(lista_) if num==count])
lista_ = [1, 8, 3, 4, 7, 5, 6, 2, 9 , 6, 2, 9 ,1, 8, 3, 4,1, 6, 2, 9 ,1, 8, 3, 4,3,1, 8, 3, 4, 7, 5, 6, 2, 9 ]
print(f"{count_match_index(lista_)=}")
print(f"{(len([num for count,num in enumerate(lista_) if num==count]))=}")
##################################################################################################

def sumar(x):
    return x+100
def cuadrado(x):
    return x**2
def superior(funcion,lista):
    resultado =funcion(4)
    # ~ for n in lista:
        # ~ resultado.append(funcion(n))
    return resultado
numeros = [2,5,10]
print(superior(sumar,numeros))
out: [102, 105, 110]
print(superior(cuadrado,numeros))
out: [4, 25, 100]
from statistics import mean
mean([1, 2, 3, 4, 4])

print(mean([-1.0, 2.5, 3.25, 5.75]))


# ~ from fractions import Fraction as F
# ~ mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
# ~ Fraction(13, 21)

# ~ from decimal import Decimal as D
# ~ mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
def esPositivo(n):
    return n > 0
def positivosConFilter(numeros):
    return filter(esPositivo, numeros)
for x in (positivosConFilter([2, -1, 4, 0, -10, -2, 6, -8])):
    print (x)
