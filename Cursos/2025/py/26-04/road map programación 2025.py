import os
from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione enter para continuar")
limpiar();
#################################################################
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
║                                                                             ║
║    Modulos IT -  Programacion                                               ║
║        Constantes y variables, tipos de datos.                              ║
║        Operadores lógicos y matemáticos.                                    ║
║        Estructuras de toma de decisiones.                                   ║
║        Estructuras de repeticiones.                                         ║
║        Procedimientos y funciones.                                          ║
║        Listas, tuplas, diccionarios.                                        ║
║        Algoritmos y estructuras de datos.                                   ║
║        Bases de datos                                                       ║
║               Conexión - Cursor                                             ║
║                      BBDD                                                   ║
║                      Tablas                                                 ║
║                      Campos (tipos de datos)                                ║
║                      Registros                                              ║
║               CRUD - ABM                                                    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}{Fore.BLACK+Back.CYAN}
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║    Road map de clases con Ariel                                             ║
║        Programación Modulo 1 - presentación e instalacion                   ║
║        Programación Modulo 2 - t obj_1ros operadores                        ║
║        Programación Modulo 3 - m flujo - if                                 ║
║        Programación Modulo 4 - entradas de datos                            ║
║        Programación Modulo 5 - m flujo - while                              ║
║        Programación Modulo 6 - colecciones - m flujo - for                  ║
║                                          ingresar                           ║
║                                          eliminar                           ║
║                                          modificar                          ║
║        Programación Modulo 7 - random - ternarios - comprension             ║
║        Programación Modulo 8 - funciones propias                            ║
║                                          parametro    | entrada - salida    ║
║                                          argumento                          ║
║                                          recursividad                       ║
║                                                                             ║
║        Programación Modulo 9 - lambda - o_sup                               ║
║                                        map(funcion_accion simple, coleccion)║
║                                        filter(funcion_booleana, coleccion)  ║
║                                        reduce(funcion-2 parametros entrada  ║
║                                                       1 parametro de salida)║
║                                                                             ║
║        Programación Modulo 10 - externos with open(nombre archivo, mode     ║
║                                                rb             r read        ║
║                                                wb             w write       ║
║                                                ab             a append      ║
║                                                xb?            x crea vacio  ║
║                                          binario pickle     json            ║
║                                                                             ║
║        Programación Modulo 10 - try except basico                           ║
║        Programación Modulo 11 - web                                         ║
║                                     Requests                                ║
║                                                                             ║
║        Programación Modulo 12 - BBDD                                        ║
║                               Estructura de dados                           ║
║                                   Conexión - Cursor                         ║
║                                          BBDD                               ║
║                                          Tablas                             ║
║                                          Campos (tipos de datos)            ║
║                                          Registros                          ║
║                                   CRUD - ABM                                ║
║                                          insert                             ║
║                                          select                             ║
║                                          update                             ║
║                                          delete                             ║
║                                   filtros                                   ║
║                                          where                              ║
║                                          like                               ║
║                                                                             ║
║        Programación Modulo 13 - GUI                                         ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')

