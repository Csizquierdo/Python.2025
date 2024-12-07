# Métodos de diccionarios

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": False,
    "cursos": ["Python", "JavaScript"],
}

# get(key, default=None)
# Devuelve el valor asociado a la clave especificada.
# Si la clave no existe, devuelve un valor predeterminado opcional.

print("*** GET")
nombre = diccionario.get("nombre")
print(nombre)
apellido = diccionario.get("apellido", "No se encontró el apellido")
print(apellido)

# update(dict)
# Actualiza el diccionario con los pares clave-valor de otro diccionario.
print("*** UPDATE")
datos_complementarios = {"apellido": "Pérez"}
diccionario.update(datos_complementarios)
print(diccionario)

# pop(key, default=None)
# Elimina y devuelve el valor asociado a la clave especificada.
# Si la clave no existe, devuelve un valor predeterminado opcional.
print("*** POP")
lo_que_borré = diccionario.pop("edad")
print(lo_que_borré)
print(diccionario)

# popitem()
# Elimina y devuelve un par clave-valor arbitrario del diccionario.
# Si el diccionario está vacío, lanza una excepción KeyError.
print("*** POPITEM")
par_clave_valor = diccionario.popitem()
print(par_clave_valor)
print(diccionario)
