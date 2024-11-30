# Entrada
edad = int(input("Ingrese la edad del cliente: "))
antiguedad = int(input("Ingrese la antigüedad en el sistema financiero: "))
ingreso = float(input("Ingrese el ingreso mensual del cliente en dólares: "))
# La técnica de bandera o flag
# 1. Se inicializa la variable bandera en False
# 2. Evaluar la condición, y si se cumple, cambiar el valor de la bandera a True
credito_aprobado = False  # flag
if edad >= 18:
    if antiguedad >= 3 and ingreso > 2500:
        credito_aprobado = True
    elif antiguedad < 3 and ingreso > 4000:
        credito_aprobado = True
# Salida
if credito_aprobado:
    print("El crédito se aprueba")
else:
    print("El crédito no se aprueba")