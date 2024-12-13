"""
A partir del código anterior (13_colecciones) solicitar al usuario un nombre a buscar
Si lo encuentra, mostrar sus nacionalidades
"""


usuarios = [
    {
        "nombre": "Cintia",
        "nacionalidades": ["argentina", "italiana"],
    },
    {
        "nombre": "Juan",
        "nacionalidades": ["española"],
    },
    {
        "nombre": "Liam",
        "nacionalidades": [],
    },
]

usuario_nombre: str = input("ingrese un usuario: ").lower().strip().capitalize()

for user in usuarios:
<<<<<<< HEAD
    indice: int = usuarios.index(user)
    for valor in user.values():
        if usuario_nombre == valor:    
            nacionalidad: str = usuarios[indice]["nacionalidades"]
            print(f"La nacionalidad es: '{nacionalidad}'")
=======
    for nombres, nacionalidad in usuarios.items():
>>>>>>> 360d57bcea66e3c0f88f4da549f04f9e3f9a4b43

