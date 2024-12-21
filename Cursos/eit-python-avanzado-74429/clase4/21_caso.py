def mayus_dict(diccionario: dict[str, str]) -> dict[str, str]:
    return {k.upper(): v.upper() for k, v in diccionario.items()}


original = {"hola": "hola", "2": "chau"}
nuevo = mayus_dict(original)
print(original)
print(nuevo)
