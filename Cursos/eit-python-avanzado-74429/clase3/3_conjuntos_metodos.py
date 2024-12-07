# Métodos conjuntos

conjunto_a = {0, 1, 2, 3, 4}

# add()
# Agrega 1 elemento al conjunto, si existe no lo agrega
conjunto_a.add(5)
print(conjunto_a)

# pop()
# Elimina un elemento aleatorio del conjunto y lo devuelve
elemento_eliminado = conjunto_a.pop()
print(elemento_eliminado)
print(conjunto_a)

# remove()
# Elimina un elemento especificado del conjunto, si no existe lanza una
# excepción KeyError
conjunto_a.remove(5)
# conjunto_a.remove(5)
print(conjunto_a)


# discard()
# Elimina un elemento especificado del conjunto, si no existe no hace nada
conjunto_a.discard(5)
print(conjunto_a)

# clear()
# Elimina todos los elementos del conjunto
conjunto_a.clear()
print(conjunto_a)
