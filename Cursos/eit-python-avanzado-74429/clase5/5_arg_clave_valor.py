# Argumentos clave - valor


def mostrar(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


mostrar(nombre="Juan", edad=25, ciudad="Buenos Aires")
