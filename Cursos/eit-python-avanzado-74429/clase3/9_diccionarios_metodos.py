# Métodos de diccionarios para iterar

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": False,
    "cursos": ["Python", "JavaScript"],
}

# keys()
# Devuelve un objeto dict_keys que contiene las claves del diccionario.
claves = diccionario.keys()
print(claves)  # dict_keys(['nombre', 'edad', 'es_estudiante', 'cursos'])


# values()
# Devuelve un objeto dict_values que contiene los valores del diccionario.
valores = diccionario.values()
print(valores)  # dict_values(['Juan', 30, False, ['Python', 'JavaScript']])


# items()
# Devuelve un objeto dict_items que contiene las claves y valores del diccionario como tuplas.
elementos = diccionario.items()
print(elementos)
