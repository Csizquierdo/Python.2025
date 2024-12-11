import requests

API_KEY = "76f4a980b73dedf934cbbf010ce5c1b8"
ciudad = "Mendoza"
URL = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
)


respuesta = requests.get(URL)
print(respuesta)
      
"""
if respuesta.status_code == 200:
    diccionario = respuesta.json()
    temperatura = diccionario["main"]["temp"]
    clima = diccionario["weather"][0]["description"]
    print(f"En la ciudad de {ciudad} hay una temperatura de {temperatura}ºC")
    print(f"Clima: {clima}")
else:
    print(respuesta.status_code)
"""