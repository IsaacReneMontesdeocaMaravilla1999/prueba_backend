from urllib.request import urlopen
import json

url = "https://prueba-backend-3258e-default-rtdb.firebaseio.com/estados.json"

datos = urlopen(url)

usuario = json.loads(datos.read())

print(usuario)

