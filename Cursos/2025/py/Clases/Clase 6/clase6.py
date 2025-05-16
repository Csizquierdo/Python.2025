#Leer
""" file = open("archivo.txt", "r")
print(file.read())
file.close() """

#Escribir
""" file = open("archivo.txt", "w")
file.write("Hola mundo de nuevo!")
file.close() """

""" file = open("archivo.txt", "a")
file.write("Tercer prompt\n")
file.close() """

""" with open("archivo.txt", "r") as file:
    print(file.read()) """

""" 
from math import *
print(sqrt(9)) """

""" from calculadora import sumar

print(sumar(2,5)) """
""" 
import os
import shutil

print(os.listdir("C:\\Users\\Cesar\\Desktop\\desk\\bootcamps\\E\\Python Programing 6\\Nueva carpeta\\\Modulo 3")) 

#os.rmdir('carpeta')
shutil.copy('carpeta/calculadora.py', 'otra_carpeta')
"""

import sqlite3

conexion = sqlite3.connect("database.db")
cursor = conexion.cursor()
#cursor.execute("CREATE TABLE personas(nombre TEXT, edad NUMERIC)")

personas = (
    ("Diego", 30),
    ("Cristian", 25),
    ("Jorge", 24)
)

for nombre, edad in personas:
    cursor.execute("INSERT INTO personas VALUES (?, ?)", (nombre, edad))

conexion.commit()
conexion.close()