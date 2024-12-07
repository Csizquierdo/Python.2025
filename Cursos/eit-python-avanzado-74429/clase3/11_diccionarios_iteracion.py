print("***str")
text = "hola"
for letra in text:
    print(letra)

print("***list | tuple | set")
numeros_romanos = ["I", "V", "X", "L", "C", "D", "M"]
for numero in numeros_romanos:
    print(numero)

print("***dict keys()")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": False,
    "cursos": ["Python", "JavaScript"],
}
for clave in persona.keys():
    print(clave)

print("***dict values()")
for valor in persona.values():
    print(valor)

print("***dict items()")
for clave, valor in persona.items():
    print(f"La clave es '{clave}'. Su valor es '{valor}'")
