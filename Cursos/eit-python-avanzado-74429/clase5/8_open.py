# archivo = open("test.txt", "w")
# archivo.write(input("Escribe algo: ") + "\n")
# archivo.write("Python\n")
# archivo.write("Django\n")
# archivo.close()

# archivo = open("test.txt", "a")
# archivo.write("FastAPI\n")
# archivo.close()

archivo = open("test.txt")
contenido = archivo.read()
print(contenido)
archivo.close()
