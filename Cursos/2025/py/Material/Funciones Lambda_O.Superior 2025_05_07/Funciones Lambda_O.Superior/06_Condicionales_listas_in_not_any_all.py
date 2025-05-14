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
import datetime
pausa()
limpiar()
print(Back.GREEN+"""\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║  ╔═══╗  ╔═════╗ ╔╗    ╦ ╔══╦══╗ ╔═════╗ ╔╗    ╦  ╔════╗  ╦  ╔═══╗   ╔═══╗   ║
║ ╔╝   ╚╗ ║       ║╚╗   ║    ║    ║       ║╚╗   ║ ╔╝    ╚╗ ║ ╔╝   ╚╗ ╔╝   ╚╗  ║
║ ║       ║       ║ ╚╗  ║    ║    ║       ║ ╚╗  ║ ║        ║ ║     ║ ║        ║
║ ╚╗      ║       ║  ╚╗ ║    ║    ║       ║  ╚╗ ║ ║        ║ ║     ║ ╚╗       ║
║  ╚═══╗  ╠════╝  ║   ╚╗║    ║    ╠════╝  ║   ╚╗║ ║        ║ ╠═════╣  ╚═══╗   ║
║      ╚╗ ║       ║    ╚║    ║    ║       ║    ╚║ ║        ║ ║     ║      ╚╗  ║
║ ╚╗   ╔╝ ║       ║     ║    ║    ║       ║     ║ ╚╗    ╔╝ ║ ║     ║ ╚╗   ╔╝  ║
║  ╚═══╝  ╚═════╝ ╩     ╚    ╩    ╚═════╝ ╩     ╚  ╚════╝  ╩ ╩     ╩  ╚═══╝   ║
║                                                                             ║
║                             ╔═════╗   ╔══════╗                              ║
║                             ║     ╚╗  ║                                     ║
║                             ║      ║  ║                                     ║
║                             ║      ║  ║                                     ║
║                             ║      ║  ╠═════╝                               ║
║                             ║      ║  ║                                     ║
║                             ║     ╔╝  ║                                     ║
║                             ╚═════╝   ╚══════╝                              ║
║                                                                             ║
║       ╔════╗   ╔════╗  ╔╗      ╦  ╔═══╦═══╗ ╔══════╗   ╔════╗  ╦            ║
║      ╔╝    ╚╗ ╔╝    ╚╗ ║╚╗     ║      ║     ║      ╚╗ ╔╝    ╚╗ ║            ║
║      ║        ║      ║ ║ ╚╗    ║      ║     ║       ║ ║      ║ ║            ║
║      ║        ║      ║ ║  ╚╗   ║      ║     ║      ╔╝ ║      ║ ║            ║
║      ║        ║      ║ ║   ╚╗  ║      ║     ╠═══╦══╝  ║      ║ ║            ║
║      ║        ║      ║ ║    ╚╗ ║      ║     ║   ╚╗    ║      ║ ║            ║
║      ╚╗       ╚╗    ╔╝ ║     ╚╗║      ║     ║    ╚╗   ╚╗    ╔╝ ║            ║
║       ╚════╝   ╚════╝  ╩      ╚╝      ╩     ╩     ╚╝   ╚════╝  ╚═════╝      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝"""+Back.RESET)
pausa()
limpiar()
print(Back.GREEN+"""\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║                 ╔═════╗         ╔╗      ╦      ╦       ╦                    ║
║                ╔╝     ╚╗        ║╚╗     ║      ╚╗     ╔╝                    ║
║                ║       ║        ║ ╚╗    ║       ╚╗   ╔╝                     ║
║                ║       ║        ║  ╚╗   ║        ╚╗ ╔╝                      ║
║                ╠═══════╣        ║   ╚╗  ║         ╚╦╝                       ║
║                ║       ║        ║    ╚╗ ║          ║                        ║
║                ║       ║        ║     ╚╗║          ║                        ║
║                ╩       ╩        ╩      ╚╝          ╩                        ║
║                                                                             ║
║                                                                             ║
║                        ╠═══════════════════════╣                            ║
║                                                                             ║
║                 ╔═════╗         ╦               ╦                           ║
║                ╔╝     ╚╗        ║               ║                           ║
║                ║       ║        ║               ║                           ║
║                ║       ║        ║               ║                           ║
║                ╠═══════╣        ║               ║                           ║
║                ║       ║        ║               ║                           ║
║                ║       ║        ║               ║                           ║
║                ╩       ╩        ╚═══════╝       ╚═══════╝                   ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣"""+Style.RESET_ALL+Back.BLUE+"""
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           CONDICION EN GRUPO                                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝"""+Back.RESET)


def validar_entero(texto):
    dato = input (texto)
    if dato.isdigit():
        return int(dato)

nota_matematica =   validar_entero ("que nota tenes en matemática:")
nota_lengua     =   validar_entero ("que nota tenes en lengua:")
nota_fisica     =   validar_entero ("que nota tenes en física:")
nota_quimica    =   validar_entero ("que nota tenes en química:")
nota_gimnacia   =   validar_entero ("que nota tenes en gimnacia:")
nota_dibujo     =   validar_entero ("que nota tenes en dibujo:")
lista_materias  =   ["nota_matematica","nota_lengua","nota_fisica","nota_quimica","nota_gimnacia","nota_dibujo"]
estado_toda_las_materias = [    nota_matematica >= 7,
                                nota_lengua     >= 7,
                                nota_fisica     >= 7,
                                nota_quimica    >= 7,
                                nota_gimnacia   >= 7,
                                nota_dibujo     >= 7 ]

for estado_materia in estado_toda_las_materias:
    print (f"Estado materia aprobado {estado_materia}")

for materia, estado_materia in zip(lista_materias, estado_toda_las_materias):#      zip
    print (f"Estado de {materia} aprobado {estado_materia}")

if False in estado_toda_las_materias:
    print ('"IN" al menos desaprobada una')

if False not in estado_toda_las_materias:
    print ('"NOT IN" ni una desaprobada una')

if all (estado_toda_las_materias):
    print ('"ALL" felicitaciones todo aprobado')

if  any (estado_toda_las_materias):
    print ('"ANY" al menos aprobada una')
if not all (estado_toda_las_materias):
    print ('"NOT ALL" al menos desaprobada una')
    print ('"NOT ALL" te quedo algo colgado para rendir')

if  not any (estado_toda_las_materias):
    print ('"NOT ANY"todo mallllllll')
