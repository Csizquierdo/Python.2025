import os

    
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione enter para continuar")


def login():
     valuser = "aaa"
     valcontra = "aaa" 
     usuario = input("Ingrese usuario: ")
     contrasena = input("Ingrese contraseña: ")

     if usuario == valuser and contrasena == valcontra:
        print("Bienvenido")
        
     else:
        print("Usuario o contraseña incorrecto")
        return login()

limpiar()
login()
pausa()
