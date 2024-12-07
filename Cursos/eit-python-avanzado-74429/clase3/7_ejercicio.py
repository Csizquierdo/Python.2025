"""
Escribir un programa que le solicite al usuario
su nombre, edad, dirección y,
que, posteriormente, lo muestre por pantalla:
Ejemplo del output solicitado:
Juan tiene 25 años, y vive en Carrera 7 - Bogotá

Usar un diccionario para guardar los datos del usuario.
"""

from typing import Any

# Entrada
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su dirección: ")

# Crear la estructura de datos
formulario: dict[str, Any]  # Anotaciones e tipo o type hints
formulario = {"nombre": nombre, "edad": edad, "direccion": direccion}

# Salida
mensaje = (
    f"{formulario['nombre']} tiene "
    f"{formulario['edad']} años, y vive en {formulario['direccion']}."
)

print(mensaje)
