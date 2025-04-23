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


'''
        Te damos la bienvenida al curso de Python Programming
        Organización del curso
        Instructivo de Instalación
        Glosario - Terminología a utilizar
        Python y herramientas
        Acerca de Python
        Instalaciones y Hola Mundo!
        Introducción y cuestiones básicas
        Tipo de datos y colecciones
        Operadores
        Sentencias de control
        Funciones primera parte
        Funciones Built-in (integradas)
                A=abs(),aiter(),all(),any(),anext(),ascii()
                B=bin(),bool(),breakpoint(),bytearray(),bytes()
                C=callable(),chr(),classmethod(),compile(),complex()
                D=delattr(),dict(),dir(),divmod()
                E,enumerate(),eval(),exec()
                F=filter(),float(),format(),frozenset()
                G=getattr(),globals()
                H=hasattr(),hash(),help(),hex()
                I=id(),input(),int(),isinstance(),issubclass(),iter()
                L=len(),list(),locals()
                M=map(),max(),memoryview(),min()
                N=next()
                O=object(),oct(),open(),ord()
                P=pow(),print(),property()
                R=range(),repr(),reversed(),round()
                S=set(),setattr(),slice(),sorted(),staticmethod(),str(),sum(),super()
                T=tuple(),type()
                V=vars()
                Z=zip()
                _=__import__()
            condicionales = if elif else, match case, ¿while?
            bucles = while, for
'''



pausa()
limpiar










"""
int var ;
var = 1234;

float var ;
var = 12.34;


char var [5];
var = "12.34";
"""

obj = 1234
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id  (obj)=}
""")
"""
dir (obj)=['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 

'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

"""
obj = 1235
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id  (obj)=}
""")

print (f"{obj**2=}")

print ("*"*50)##########################################################
obj = 12.34
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id  (obj)=}
""")
"""
dir (obj)=['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 

'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
"""
print (f"{obj**2=}")

print ("*"*50)##########################################################

櫰櫪櫨櫹 = "櫰櫹"
if 櫰櫪櫨櫹 == "櫰櫹":
    print ("櫰櫹")

print (f"""
{櫰櫪櫨櫹=}
{type(櫰櫪櫨櫹)=}
""")



obj = "uno dos tres cuatro"
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id  (obj)=}
""")
"""
dir (obj)=['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""


obj = "HoLa MuNdo it"

print ("""
tipo de objeto. STRING
metodos de estilo 
            'capitalize', 'casefold', 'lower',  'swapcase', 'title', 'upper'
""")

print (obj)
print ( "el contenido del objeto es {obj}")
print (f"el contenido del objeto es {obj}")
print (f"el contenido del objeto es {obj=}")

print (f" capitalize    {obj.capitalize()}")
print (f" casefold      {obj.casefold()}")
print (f" lower         {obj.lower()}")
print (f" swapcase      {obj.swapcase()}")
print (f" title         {obj.title()}")
print (f" upper         {obj.upper()}")
pausa()

print ("""
tipo de objeto. STRING
metodos de Lugar 
            'center', 'ljust', 'rjust',
""")
print (f"el contenido del objeto es {obj=}")
print (f" center        |{obj.center(50)}|")
print (f" ljust         |{obj.ljust(50)}|")
print (f" rjust         |{obj.rjust(50)}|")

print (f" upper.rjust(50)      |{obj.upper().rjust(50)}|")
print (f" center.upper         |{obj.center(50).upper()}|")
print (f" .rjust(50).upper.center         |{obj.rjust(50).upper().center(50)}|")


pausa()
print ("""
tipo de objeto. STRING
metodos booleanos 
            'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'startswith' , 'endswith'
""")
print (f"el contenido del objeto es {obj=}")

print (f"isalnum {obj.isalnum()=}")
print (f"isalpha {obj.isalpha()=}")
print (f"isascii {obj.isascii()=}")
print (f"isdecimal {obj.isdecimal()=}")
print (f"isdigit {obj.isdigit()=}")
print (f"isnumeric {obj.isnumeric()=}")


print ("*"*50)
print (f"el contenido del objeto +.replace(' ','') es   {obj=}")

print (f"isalnum {obj.replace(' ','').isalnum()=}")
print (f"isalpha {obj.replace(' ','').isalpha()=}")
print (f"isascii {obj.replace(' ','').isascii()=}")
print (f"isdecimal {obj.replace(' ','').isdecimal()=}")
print (f"isdigit {obj.replace(' ','').isdigit()=}")
print (f"isnumeric {obj.replace(' ','').isnumeric()=}")

print ("*"*50)
obj="987654"

print (f"el contenido del objeto es {obj=}")

print (f"isalnum {obj.isalnum()=}")
print (f"isalpha {obj.isalpha()=}")
print (f"isascii {obj.isascii()=}")
print (f"isdecimal {obj.isdecimal()=}")
print (f"isdigit {obj.isdigit()=}")
print (f"isnumeric {obj.isnumeric()=}")
print ("*"*50)
obj="987.654"

print (f"el contenido del objeto .replace('.','') es {obj=}")

print (f"isalnum {obj.replace('.','').isalnum()=}")
print (f"isalpha {obj.replace('.','').isalpha()=}")
print (f"isascii {obj.replace('.','').isascii()=}")
print (f"isdecimal {obj.replace('.','').isdecimal()=}")
print (f"isdigit {obj.replace('.','').isdigit()=}")
print (f"isnumeric {obj.replace('.','').isnumeric()=}")



#               print (f"isnumeric {obj.isnumeric().replace('.','')=}") nuna booleana no tiene el metodo replace. Ver orde de iz a derecha
print ("*"*50)
pausa()
limpiar()
obj="987.654"
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id  (obj)=}
""")


if obj.isdigit():
    # casting
    obj = int(obj)
    print (f"""
    {obj=}
    {type(obj)=}
    {dir (obj)=}
    {id  (obj)=}
    """)
elif  obj.replace(".","",1).isdigit():
    # casting
    obj = float(obj)
    print (f"""
    {obj=}
    {type(obj)=}
    {dir (obj)=}
    {id  (obj)=}
    """)
else:
    print (f"el obj {obj} no puede tranformarse en numerico")
print ("fin")

pausa()

# ~ 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
# ~ 'format_map', 'index',  'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
# ~ 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
# ~ 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

x = 7
y = 3
print (f"el resultado de x + y es {x+y} sumar")

x = "hola "
y = "mundo IT"
print (f"el resultado de x + y es {x+y} concatenar")

x = 7
y = 3
print (f"el resultado de x * y es {x*y} multiplica")

x = "hola "
y = 8
print (f"el resultado de x * y es {x*y} replica")

pausa()


import this

print ("*"*50)##########################################################
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
obj = 1,2
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id (obj)=}
""")

"""
obj=(1, 2)
type(obj)=<class 'tuple'>
dir (obj)=['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
"""

print ("*"*50)##########################################################
obj = [1,2]
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id (obj)=}
""")
"""
obj=[1, 2]
type(obj)=<class 'list'>
dir (obj)=['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""

print ("*"*50)##########################################################

obj = {1,2}
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id (obj)=}
""")
"""
obj={1, 2}
type(obj)=<class 'set'>
dir (obj)=['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

print ("*"*50)##########################################################

obj = {1:"hola",2:"chau"}
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
{id (obj)=}
""")
"""
obj={1: 'hola', 2: 'chau'}
type(obj)=<class 'dict'>
dir (obj)=['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

print ("*"*50)##########################################################
print ("*"*50)################ P A R A   C L A S E #####################
print ("*"*50)##########################################################
print ("*"*50)######################## I I #############################
print ("*"*50)##########################################################
print ("*"*50)##########################################################
col =[ 0,4,9,3,"pepe"]
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


""")


pausa()

obj = "hola MuNdO It"
print (f"""
{obj=}
{type(obj)=}
""")
"""
dir (obj)=['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

"""
print (f"""
{obj.upper()=}
{type(obj.upper())=}
""")
print (f"""
{obj.lower()=}
{type(obj.lower())=}
""")
print (f"""
{obj.capitalize()=}
{type(obj.capitalize())=}
""")


print (f"""
{obj.rjust(50)=}
{type(obj.rjust(50))=}
""")
print (f"""
{obj.ljust(50)=}
{type(obj.ljust(50))=}
""")
print (f"""
{obj.center(50)=}
{type(obj.center(50))=}
""")

print (f"""
{obj.center(50).upper()=}
{type(obj.center(50).upper())=}
""")

print ("*"*50)
print ("*","METODOS DE ESTILO".center(46),"*")
print ("*"*50)
m=['capitalize', 'casefold',  'lower', 'swapcase', 'title', 'translate', 'upper']

print ("*"*50)
print ("*","METODOS DE PLACE".center(46),"*")
print ("*"*50)
m='center',"ljust","rjust"



print ("*"*50)
print ("*","METODOS DE BOOLEANO".center(46),"*")
print ("*"*50)


m= ['capitalize', 'casefold', 'center', 'count', 'encode', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper','startswith', 'endswith']

print ("*"*50)
print ("*","METODOS DE REPLACE".center(46),"*")
print ("*"*50)
m='replace'


print ("*"*50)
print ("*","OTROS METODOS".center(46),"*")
print ("*"*50)
m =  ['count', 'encode',  'expandtabs', 'find', 'format', 'format_map', 'index', 'join', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', '', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'strip', 'translate',  'zfill']




exit()
#################################################################
# Clase_Variables_04
print(
    """\033[1;37;44m\n
╔══════════════════════════╦══════════════════════════╦══════════════════════════╗
║                          ║                          ║                          ║
║    + Suma                ║         a += b           ║           a = a + b      ║
║    - Resta               ║         a -= b           ║           a = a - b      ║
║    * Multiplicación      ║         a *= b           ║           a = a * b      ║
║    ** Exponente          ║         a **= b          ║           a = a ** b     ║
║    / División            ║         a /= b           ║           a = a / b      ║
║    // División entera    ║         a //= b          ║           a = a // b     ║
║    % Módulo              ║         a %= b           ║           a = a % b      ║
║                          ║                          ║                          ║
╚══════════════════════════╩══════════════════════════╩══════════════════════════╝\033[0;m
"""
)
# Precedencia (jerarquía) de operadores:

from math import sqrt

resultado = 5 / 2 + 4
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 4 + 5 / 2
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 5 / (2 + 4)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 5 / (2 + 4) + sqrt(25)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 25 ** 1 / 2
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 25 ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = (13 + 3) ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = sum(numeros[0:5])
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

numero = -100

resultado = -(100 ** (1 / 2))
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = -(numero ** (1 / 2))
print("El contenido de la variable `resultado` es:", resultado)
print("Tipo de dato de la variable `resultado`:", type(resultado).__name__)

pausa()
#################################################################

resultado = (-numero) ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)
print("Tipo de dato de la variable `resultado`:", type(resultado).__name__)

#################################################################
a = 1
b = 2
c = 3
d = 16

resultado = a / (b * c) / d ** (1 / 2) ** 3

print("Resultado:", resultado)

pausa()
#################################################################

e = 7

resultado = (a ** 3) ** 2 - b * c / (d * e)

print("Resultado:", resultado)
#################################################################

numero = int(input("Ingrese un numero: "))

if numero >= 0:
    factorial = 1

    if numero == 0 or numero == 1:
        factorial = 1
    else:
        for i in range(1, numero + 1):
            factorial *= i

    print(f"{numero}! = {factorial}")
else:
    print(
        "MENSAJE: Ha escrito un valor negativo. La función factorial no está definida para los números negativos."
    )
#################################################################
from decimal import Decimal as D
dato= 0.1+0.2
print (dato)
print( D("0.1")+ D("0.2"))
dato=D(0.1+0.2)
print (dato)

dato=D("0.1")+ D("0.2")
print (dato)
#################################################################
# ~ #pip install Fraction
from fractions import Fraction as F

print ("en fraccion: ",F(1.5))
print ("en fraccion: ",F(4.10))
print ("en fraccion: ",F(8.5))
# ~ #################################################################
import random
for x in range(11):
	print (f"Numero aleatorio en {x} lugar:",random.randrange(1,1000))
#################################################################
lista = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
print ("lista original:",lista)

print ("random.choice(lista):",random.choice(lista))
random.shuffle(lista)
print ("random.shuffle(lista):",lista)

#################################################################
print ("random.random():",random.random())

dato = 8
print (f"{dato=} {type(dato)=}  {id(dato)} ")
#--------------------------------------------------

dato = 3.14159
print (f"{dato=} {type(dato)=}  {id(dato)} ")
#--------------------------------------------------

dato = "Ariel"
print (f"{dato=} {type(dato)=}  {id(dato)} ")
#--------------------------------------------------


datos = [8,3.14159,"Ariel"]

print (f"{datos=} {type(datos)=}  {id(datos)} ")
print (f"{datos[0]=} {type(datos[0])=}  {id(datos[0])} ")
print (f"{datos[1]=} {type(datos[1])=}  {id(datos[1])} ")
print (f"{datos[2]=} {type(datos[2])=}  {id(datos[2])} ")
#--------------------------------------------------

anidado = [
            [8,3.14159,"Ariel"],
            [9,"Pepe"],
            ["Andy",1,2,3,4,5,6,7,9,8]
        ]
print (f"{anidado[2][9]=} {type(anidado[2][9])=}  {id(anidado[2][9])} ")

anidado[2][9]="abc"
print (f"{anidado[2][9]=} {type(anidado[2][9])=}  {id(anidado[2][9])} ")


ingreso = input ("ingrese un dato:")
if ingreso.isdigit():
    ingreso = int(ingreso)
elif ingreso.replace(".","",1).isdigit():
    ingreso = float(ingreso)
else:
    ingreso = ingreso.upper()
print (f"{ingreso=} {type(ingreso)=}  {id(ingreso)} ")

x=9_999_000_00.29

print (x+1)

















entrada.append(40)
dato = [10, 20, 30]
funcion(dato)
print(f"{dato=}")
print('''
        Argumentos de longitud variable
        Al declarar la función con un parámetro *, hará que los argumentos, sean la cantidad que fueran, lleguen individualmente y que una vez recibido
            la función lo empaquete en una tupla de manera automática.
        Atención: No confundir * con los punteros en otros lenguajes de programación, no tiene nada que ver
        ¡En Python existen los punteros a memoria!
''')
def sumar(*args):
    print(f"{args=}")
    print(f"{type(args)=}")
    total = 0
    for n in args:
        total += n
    return total
l=sumar(10,0,5,4)
print(f"{l=}")
print('''
        El doble asterisco ** (usualmente acompañado por el nombre kwargs) captura cualquier keyword argument que no haya sido definido junto con la función.
        Los argumentos capturados por este operador son almacenados, como dijimos, en un diccionario que tiene como claves los strings que representan los
            nombres de los argumentos, y como valor, el valor del argumento.
        Este operador debe ir al final de la definición de otros parámetros, si los hubiera.
''')
# ~ Ejemplo:
def sumar(**kwargs):
    print(f"{kwargs=}")
    print(f"{type(kwargs)=}")
    total = 0
    for n in kwargs:
        total+= kwargs[n]

    print(f"{total=}")
sumar(a=5, b=20, c=23)
# ~ Orden para usar diferentes argumentos
def funcion(a,b,*args,c=100,**kwargs):
    print(f"{a=}\t\t\t{type(a)=}")
    print(f"{b=}\t\t\t{type(b)=}")
    print(f"{args=}\t\t\t{type(args)=}")
    print(f"{c=}\t\t\t{type(c)=}")
    print(f"{kwargs=}\t\t\t{type(kwargs)=}")

######################################

def superior(funcion,lista):
    nueva = []
    for n in lista:
        nueva.append(funcion(n))
    return nueva


######################################

print(f"{superior(lambda x : x**3,[1,2,3])=}")
print()

input("Enter para continuar......")
