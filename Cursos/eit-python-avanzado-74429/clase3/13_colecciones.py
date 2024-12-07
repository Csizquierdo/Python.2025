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

nacionalidad_italiana_de_cintia: str = usuarios[0]["nacionalidades"][1]
print(nacionalidad_italiana_de_cintia)
