import requests

# URL del recurso
url = '<TU_LINK_AQUÍ>'

# Hacer la petición GET
response = requests.get(url)

# Imprimir resultados
print(f"Código de estado: {response.status_code}")
if response.ok:  # Si la petición fue exitosa (status_code 200-299)
    print("Respuesta JSON:")
    print(response.json())  # Si el contenido es JSON
else:
    print(f"Error en la solicitud: {response.text}")
