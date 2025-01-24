import requests

# URL del recurso
url = '<TU_LINK_AQUÍ>'

# Headers personalizados
headers = {
    'Authorization': 'Bearer <TU_TOKEN_AQUÍ>',
    'Content-Type': 'application/json'
}

# Hacer la petición GET (o cambia por POST/PUT según lo que necesites)
response = requests.get(url, headers=headers)

# Imprimir resultados
print(f"Código de estado: {response.status_code}")
if response.ok:
    print("Respuesta JSON:")
    print(response.json())  # Si el contenido es JSON
else:
    print(f"Error: {response.text}")
