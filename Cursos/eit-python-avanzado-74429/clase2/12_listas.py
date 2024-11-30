# Listas

# Definición: Colección mutable de objetos indexados.

lista = [1, 2, 3, "hola", True, ("a", "")]
print(lista)

# Representación
print(f"Python reconoce una list mediante el nombre {type(lista)}")

# Creación de una lista vacía
lista_vacia = []
lista_vacia_2 = list()
print(lista_vacia, lista_vacia_2)

# Longitud
lista = [1, 2, 3, "hola", True, ("a", "")]
print(f"La lista tiene {len(lista)} elementos")

# Acceso a elementos de la tupla mediante índices
print(lista[0])
hola = lista[3]
print(hola, type(hola))

# Crear elementos
lista += [1000]
print(lista)

# Modificar
lista[0] = "Hola Pyhton"
print(lista)

# Eliminar
del lista[0]
# del lista[0:3]
print(lista)

# Operador in
print(3 in lista, "a" in lista)

# Desempaquetar
numeros_primos = [2, 3, 5]
# primero = numeros_primos[0]
# segundo = numeros_primos[1]
# tercero = numeros_primos[2]
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)

# Desempaquetar más elementos
numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
primero, segundo, tercero, *otros = numeros_primos
print(primero, segundo, tercero, otros)
primero, *medio, ultimo = numeros_primos
print(primero, medio, ultimo)

# Concatenación
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = lista_1 + lista_2
print(lista_1, lista_3)
