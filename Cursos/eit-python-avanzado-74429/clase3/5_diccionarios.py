# Diccionarios

# Definición: Colección mutable y no indexada (desordenada) de pares clave-valor.

# Declaración
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": False,
    "cursos": ["Python", "JavaScript"],
}

# Representación
print(f"Python reconoce este tipo de datos mediante el nombre {type(diccionario)}")


# Creación de un tipo vacío
diccionario_vacio = {}
diccionario_vacio_2 = dict()
print(diccionario_vacio, diccionario_vacio_2)


# Longitud
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": False,
    "cursos": ["Python", "JavaScript"],
}
print(f"Longitd {len(diccionario)}")

# Acceso a elementos mediante índices
print("**** ACCESO A LOS ELEMENTOS")
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["es_estudiante"])
print(diccionario["cursos"])

# Crear elementos
diccionario["altura"] = 1.75
print(diccionario)

# Modificar elementos
diccionario["edad"] += 1
print(diccionario)

# Eliminar elementos
del diccionario["altura"]
print(diccionario)

# Operador in
diccionario_de_cartas_españolas = {
    1: "As",
    2: "Dos",
    3: "Tres",
    4: "Cuatro",
    5: "Cinco",
    6: "Seis",
    7: "Siete",
    10: "Sota",
    11: "Caballo",
    12: "Rey",
}

print(f"¿Está la carta 10? {'Sí' if 10 in diccionario_de_cartas_españolas else 'No'}")
print(f"¿Está la carta 20? {'Sí' if 20 in diccionario_de_cartas_españolas else 'No'}")


# Desempaquetar
datos_civiles = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
datos_estudios = {"idiomas": ["Español", "Inglés"], "cursos": ["Python", "JavaScript"]}
datos_completos = {**datos_civiles, **datos_estudios}
print(datos_completos)
