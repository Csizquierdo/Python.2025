with open("test2.txt", "w") as archivo:
    archivo.write("Python\n")
    archivo.write("Django\n")

with open("test2.txt") as archivo:
    contenido = archivo.read()
    print(contenido)
