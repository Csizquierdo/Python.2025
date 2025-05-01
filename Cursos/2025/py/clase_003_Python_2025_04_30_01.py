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
"""

######################################################################
def sumar(p1,p2):
    return p1+p2
######################################################################
def restar(p1,p2):
    return p1-p2
######################################################################
def dividir(p1,p2):#ver
    if p2 == 0:
        print ("Esta operacion no acepta cero (0)")
        p2    = consulta_numero ()
        return dividir(p1,p2)
       #return  p1
    return p1/p2
       
    """
    try :
        return p1/p2
    except Exception as macana:
        print (f"se genero una excepción del tipo {macana}")
        return  p1
    """
######################################################################
def dividir_base(p1,p2):#ver
    if p2 == 0:
        print ("Esta operacion no acepta cero (0)")
        p2    = consulta_numero ()
        return dividir_base(p1,p2)
       #return  p1
    return p1//p2
######################################################################
def multiplicar(p1,p2):
    return p1*p2
###################################################################### 
def expo(p1,p2):
    return p1**p2
######################################################################
def raiz(p1,p2):#ver
    if p2 == 0:
        print ("Esta operacion no acepta cero (0)")
        p2    = consulta_numero ()
        return raiz(p1,p2)
       #return  p1
    return p1**(1/p2)
######################################################################

def resto(p1,p2):#ver
    if p2 == 0:
        print ("Esta operacion no acepta cero (0)")
        p2    = consulta_numero ()
        return raiz(p1,p2)
       #return  p1
    return p1%p2
######################################################################
def consulta_operador (resultado):
    if resultado == 0:return "+"
    #operador =input(f"ingrese un operador entre {tuple(diccionario.keys())}")
    operador =input(f"ingrese un operador entre ({','.join(diccionario.keys())})").upper()
    if operador not in diccionario.keys() :
        return consulta_operador (resultado)
    return operador
######################################################################
def consulta_numero ():
    valor =input("ingrese un valor:")
    if not valor.replace(".","",1).isdigit():
        return consulta_numero ()
    return  float(valor) 
######################################################################
resultado = 0
diccionario = {
                "+":sumar,
                "-":restar,
                "/":dividir,
                "*":multiplicar,
                "**":expo,
                "^":raiz,
                "//":dividir_base,
                "%":resto,
                "S":"",
                "=":""
                }
while True:  
    operador = consulta_operador (resultado)
    anterior = resultado
    if operador == "=":
        print (f"""
        el resultado final = {anterior}  
        reinicio en 0
        """)
        resultado =0
    elif operador == "S":
        print ("Gracias por haber usado la calcu de consola. Adios")
        quit()
    else:
        valor    = consulta_numero ()
        resultado =  diccionario[operador] (resultado,valor)
        #            \___________________/
        #resultado = diccionario   ["+"]   (resultado,valor)
        #            \___________________/
        #resultado =        sumar          (resultado,valor)
        print (f"el resultado de {anterior}{operador}{valor}={resultado}  ")    
        
"""
resultado = 0
while True:  
    operador = ""
    if resultado != 0:
        while  operador not in ("+","-","*","/") :
            operador =input("ingrese un operador entre (+,-,*,/)")
    else:
        operador = "+"
    valor =""
    while  not valor.replace(".","",1).isdigit():
        valor =input("ingrese un valor:")
    valor = float(valor)
    anterior = resultado
    if operador =="+":
        resultado = sumar (resultado,valor)
    elif operador =="-":
        resultado = restar (resultado,valor)
    elif operador =="*":
        resultado = multiplicar (resultado,valor)
    elif operador =="/":
        resultado = dividir (resultado,valor)
    print (f"el resultado de {anterior}{operador}{valor}={resultado}  ")
"""
#######################################################################
"""
resultado = 0
while True:  
    operador = ""
    if resultado != 0:
        while  operador not in ("+","-","*","/") :
            operador =input("ingrese un operador entre (+,-,*,/)")
    else:
        operador = "+"
    valor =""
    while  not valor.replace(".","",1).isdigit():
        valor =input("ingrese un valor:")
    valor = float(valor)
    anterior = resultado
    match operador :
        case "+":
            resultado = sumar (resultado,valor)
        case "-":
            resultado = restar (resultado,valor)
        case "*":
            resultado = multiplicar (resultado,valor)
        case "/":
            resultado = dividir (resultado,valor)
        case _:
            print(f"el operador '{operador}' no tiene funcion aun")
        
    print (f"el resultado de {anterior}{operador}{valor}={resultado}  ")
"""
