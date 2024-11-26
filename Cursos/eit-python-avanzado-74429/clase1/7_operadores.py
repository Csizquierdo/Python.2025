# OPERADORES ARITMÉTICOS

a = 7
b = 5

# Suma (+)
print("Suma:", a + b)

# Resta (-)
print("Resta:", a - b)

# Multiplicación (*)
print("Multiplicación:", a * b)

# División (/). Resultado en punto flotante (float)
print("División:", a / b)

# División entera (//). Resultado en número entero
print("División entera:", a // b)

# Módulo (%). Resto de la división
print("Módulo:", a % b)

# Potencia (**). Eleva a la potencia indicada
print("Potencia:", a**b)

# Raiz (**) con exponente 0.5. Equivalente a math.sqrt()
print("Raíz cuadrada:", 81 ** (1 / 2))

import math

print(math.sqrt(81))

# ORDEN DE PRECEDENCIA DE LOS OPERADORES ARITMÉTICOS
# 1. paréntesis
# 2. potencias
# 3. multiplicaciones y divisiones, divión entera y módulo
# 4. sumas y restas

# OPERADORES LÓGICOS
# AND, OR, NOT
print("*** AND")
mayor_edad = True
ciudadano = True
vota = mayor_edad and ciudadano
print(vota)

print("*** OR")
trabaja = True
no_trabaja = False

cliente_1 = no_trabaja
cliente_2 = trabaja

debo_dar_alguno_credito = cliente_1 or cliente_2
print(f"{debo_dar_alguno_credito=}")

# OPERADORES DE COMPARACIÓN
# Igualdad ==
# Desigualdad !=
# Mayor que >
# Menor que <
# Mayor o igual que >=
# Menor o igual que <=

# ORDEN DE PRECEDENCIA GENERAL
# 1. Paréntesis
# 2. Operadores aritméticos.
# 3. Operadores de comparación.
# 4. Operadores lógicos.
