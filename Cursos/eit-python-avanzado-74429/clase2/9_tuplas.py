# Tuplas
# Defición: Coleccion inmutable de elementos indexados.
tupla = (1, 2, 3, "hola", True, ("a", ""))
print(tupla)

# Representación
print(f"Python reconoce una tupla mediante el nombre {type(tupla)}")

# Creación de una tupla vacía
tupla_vacia_1 = ()
tupla_vacia_2 = tuple()
print(tupla_vacia_1, tupla_vacia_2)

# Creación de una tupla con un solo elemento
tupla_un_elemento = (1,)
print(tupla_un_elemento, type(tupla_un_elemento))

# Longitud
tupla = (1, 2, 3, "hola", True, ("a", ""))
print(f"La tupla tiene {len(tupla)} elementos")

# Acceso a elementos de la tupla mediante índices
hola = tupla[3]
print(hola)

# Crear, modificar, eliminar: no se puede porque es inmutable
# tupla[3] = "HOLA"
# print(tupla)

# Operador in
print(2 in tupla)
print("a" in tupla)
print(tupla[-1], "a" in tupla[-1])
# Desempaquetar
numeros_primos = (2, 3, 5)

# primero = numeros_primos[0]
# segundo = numeros_primos[1]
# tercero = numeros_primos[2]
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)


# Desempaquetar más elementos
numeros_primos = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
primero, segundo, tercero, *otros = numeros_primos
print(primero, segundo, tercero, otros)
primero, *medio, ultimo = numeros_primos
print(primero, medio, ultimo)

# Concatenación
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
tupla_3 = tupla_1 + tupla_2
print(tupla_1, tupla_3)