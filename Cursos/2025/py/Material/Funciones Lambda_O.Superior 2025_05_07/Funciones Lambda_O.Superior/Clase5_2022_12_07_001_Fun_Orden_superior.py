try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    import os
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
limpiar()
def pausa():
    temp=input("\tPresione una tecla para continuar")
    print("\n")
def Ej_ya_hechos():
##################################################################################################################################
    #Con tab colocaremos aqui las prácticas hechas
    pass
print(Fore.WHITE +Back.GREEN+f'''
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

    funciones propias
        de orden superior

''')

'''
def sumar(datos):
    print (f"{(datos[0] + datos[1])=}")
def restar(datos):
    print (f"{(datos[0] - datos[1])=}")


def funcion (parametro,funcion):
    funcion(parametro)



lista = [8,4]

funcion (lista,sumar)

funcion (lista,restar)
'''
########################################################################################
'''

print ("&"*100)
lista = [ 8,3,7,0,4,2,6,21,12]
for index,cada_dato in enumerate(lista):#lista[::-1]
    print (f"en el index {index} se encuentra el dato {cada_dato}")
print ("&"*100)


lista1 = [ 8,3,7,0,4,2,6,21,12]
lista2 = [ "A","E","C","L","T","I","P","Q","S","Ariel","Q","S"]
for cada_dato1,cada_dato2 in zip(lista1,lista2):#lista[::-1]
    print (f"{cada_dato1=} {cada_dato2=}")
print ("&"*100)



for index , [cada_dato1,cada_dato2] in enumerate(zip(lista1,lista2)):#lista[::-1]
    print (f"en el index {index} se encuentra los datos {cada_dato1=} {cada_dato2=}")


'''
########################################################################################
'''
# ~ def sumar(dato):
    # ~ print (f"{(dato + 10)=}")
    # ~ return dato + 10

lista = [ 8,3,7,0,4,2,6,21,12]
#-------------------------------------------------------
sumar = lambda x : x+10
#-------------------------------------------------------


resultado = []
for cada_dato in lista:
    resultado.append(sumar(cada_dato))
print ("metodo for:",resultado, type(resultado),dir(resultado))
print ("*"*100)


resultado = list(map(sumar, lista))
# ~ resultado = list(resultado)
print ("map:",resultado, type(resultado),dir(resultado))
print ("*"*100)


resultado = list(map(lambda cada_dato : cada_dato+10, lista))
# ~ resultado = list(resultado)
print ("map + lambda:",resultado, type(resultado),dir(resultado))
'''
########################################################################################
'''
lista = [ 8,3,7,0,4,2,6,21,12]


def par(dato):
    if dato %2==0:
        return True
    else:
        return False


resultado = []
for cada_dato in lista:
    regreso = (par(cada_dato))
    if regreso is True:
        resultado.append(cada_dato)
print ("metodo for:",resultado, type(resultado),dir(resultado))
print ("*"*100)
resultado =list( filter(par,lista))
# ~ resultado = list(resultado)
print ("filter:",resultado, type(resultado),dir(resultado))


print ("*"*100)
resultado =list( filter(lambda cada_dato : True if cada_dato %2==0 else False ,lista))
print ("filter + lambda:",resultado, type(resultado),dir(resultado))
'''
########################################################################################

from functools import reduce
def sumar (dato1,dato2):
    return(dato1+dato2)

lista = [ 8,3,7,0,4,2,6,21,12,9]

resultado=[]
for index in range(0,len(lista)-1,2):
    resultado.append(sumar(lista[index],lista[index+1] ))
print ("metodo for:",sum(resultado))

print ("*"*100)
resultado = reduce((lambda x, y: x + y),  [ 8,3,7,0,4,2,6,21,12,9])
print ("reduce+ lambda:",resultado, type(resultado),dir(resultado))
print ("*"*100)
# ~
# ~ producto = reduce((lambda x, y: x + y),  [ 8,3,7,0,4,2,6,21,12]))
# ~ print (f"{producto=}")






















exit()
class Mi_objeto:
    def __init__ (self,**datos_obj):
        for c,v in datos_obj.items():
            setattr(self, c, v)
        # ~ self.nombre=nombre
        # ~ self.apellido=apellido
        # ~ self.DNI=DNI
        # ~ self.telefono=telefono
        print (f'''
        {self.nombre=}
        {self.apellido=}
        {self.DNI=}
        {self.telefono=}''')
        print ("Desde_dic:",self.__dict__)

datos={'nombre':'Juan','apellido':'Perez','DNI':'23456789','telefono':'2345678765'}
x=Mi_objeto(**datos)
print("*"*100)
print (f'''
{x.nombre=}
{x.apellido=}
{x.DNI=}
{x.telefono=}''')
print ("Desde_dic:",x.__dict__)
