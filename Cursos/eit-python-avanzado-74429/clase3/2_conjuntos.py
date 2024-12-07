# Conjuntos

# Definición: Colección mutable y no indexada (desordenada) de objetos únicos.
# No pueden tener como valor objetos mutables (ej: conjuntos, diccionarios)
# Sí puede contener tuplas porque son inmutables

# Declaración
# conjunto = {1, 2, "hola", 3.14, True, (1, 2, 3), [100, 200]}
conjunto = {1, 2, "hola", 3.14, True, (1, 2, 3), "a", "a"}
print(conjunto)


# Representación
print(f"Python reconoce una list mediante el nombre {type(conjunto)}")

# Creación de un conjunto vacío
# conjunto_vacio = {}  # Esto es un diccionario vacío, no un conjunto vacío
conjunto_vacio_2 = set()
# print(conjunto_vacio, conjunto_vacio_2)
print(conjunto_vacio_2)

# Longitud
conjunto = {1, 2, "hola", 3.14, True, (1, 2, 3), "a", "a"}
print(f"El conjunto tiene {len(conjunto)} elementos")

# Acceso a elementos mediante índices

# Crear elementos

# Modificar

# Eliminar

# Operador in
print(3 in conjunto, "a" in conjunto)

# Desempaquetar
numeros_primos = {2, 3, 5}
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)


# Desempaquetar más elementos
numeros_primos = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
primero, segundo, tercero, *otros = numeros_primos
print(primero, segundo, tercero, otros)
primero, *medio, ultimo = numeros_primos
print(primero, medio, ultimo)

frutas = {"manzana", "naranja"}
mas_frutas = {"pera", "uva"}
todas_las_frutas = {*frutas, *mas_frutas}
print(todas_las_frutas)
