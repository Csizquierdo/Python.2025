"""
Escribir un programa que pida al usuario que ingrese una lista de palabras
Debe salir con un break cuando el usuario ingresa un string vacío
"""

lista = []

while True:
    palabra = input("Ingrese una palabra (dejar en blanco para salir:): ")
    if palabra:
        lista.append(palabra.strip())
    else:
        break

print(f"La lista de palabras ingresadas es: {lista}")
