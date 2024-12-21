"""
Crear una función que reciba un diccionario y transformar sus valores en mayúsculas
Se debe crear un diccionario con 2 elementos cuyos valores sean cadenas
Pasarlo como argumento a la función
Debo guardar en una variable la devolución de la función
Imprimir el diccionario original y luego el diccionario transformado en mayúsculas
"""


def convertir_a_mayusculas(diccionario: dict[str, str]) -> dict:
    diccionario_final = {}
    for k, v in diccionario.items():
        diccionario_final[k.upper()] = v.upper()
    return diccionario_final


diccionario_original = {"nombre": "juan", "apellido": "perez"}
diccionario_transformado = convertir_a_mayusculas(diccionario_original)

print(diccionario_original)
print(diccionario_transformado)
