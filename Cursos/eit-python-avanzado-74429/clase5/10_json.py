import json

personas: list[dict] = []

try:
    with open("10_json.json", "r") as file:
        personas = json.load(file)
except FileNotFoundError:
    print("El archivo no existe")
except json.decoder.JSONDecodeError:
    print("El archivo no es un json o está dañado")


nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
formulario = {"nombre": nombre, "edad": edad}
personas.append(formulario)
print(personas)

try:
    with open("10_json.json", "w") as file:
        json.dump(personas, file, indent=4)
except Exception as e:
    print("Hubo un error:", type(e), e)
