"""
Manejo de excepciones con try-except

try:
    bloque de código que puede generar un error
except:
    bloque de código que se ejecuta si hay un error en el bloque try
else:
    (opcionales) bloque de código que se ejecuta si NO HAY un error en el bloque try
finally:
    (opcionales) bloque de código que se ejecuta SIEMPRE, haya o no haya un error en el bloque try
"""

try:
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Ingrese el segundo número: "))
    resultado = numero_1 / numero_2
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Debe ingresar un número")
except Exception as mensaje:
    print("Ha ocurrido un error:", type(mensaje))
else:
    print(f"El resultado de la división es: {resultado}")
