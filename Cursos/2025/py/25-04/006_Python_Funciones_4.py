
from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aquí las practicas hechas
    pass
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
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
╠═════════════════════════════════════════════════════════════════════════════╣
║                              Funciones y Metodos                            ║
║                              -------------------                            ║
║          Funciones    Description                                           ║
║                   lambda                                                    ║
║                                                                             ║
║          Metodos son funciones dentro de clases donde se deberia instanciar ║
║                   a la clase con self nombre_objeto                         ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              Funciones,  Metodos                            ║
║                                  y Generadores                              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m\033[0;m
""")

def funcion_numero(info):
    if info.isdigit():
        info = int (info)
    else:
        print ("son caracteres")
    return (info)


def suma_SIMPLE():
    DATO1 = input ("INGRESE EL PRIMER DATO:")
    DATO2 = input ("INGRESE EL SEGUNDO DATO:")
    DATO1 =  funcion_numero (DATO1)
    DATO2 =  funcion_numero (DATO2)
    RESULTADO = DATO1+DATO2
    print ( RESULTADO)
suma_SIMPLE()


pausa();limpiar();


def suma_RETURN(DATO1,DATO2):
    RESULTADO = DATO1+DATO2
    return RESULTADO

DATO1 = input ("INGRESE EL PRIMER DATO:")
DATO2 = input ("INGRESE EL SEGUNDO DATO:")
DATO1 =  funcion_numero (DATO1)
DATO2 =  funcion_numero (DATO2)



RESULTADO= suma_RETURN(DATO1,DATO2)
print (RESULTADO)

pausa();limpiar();






pausa();limpiar();
def sumar(x,y):
   return x+y

def restar(x,y):
   return x-y

def operar(operacion,x,y):
   return operacion(x,y)
x=9
y=10
print(operar(sumar,x,y))
print(operar(restar,x,y))
