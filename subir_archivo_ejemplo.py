import requests

# URL del recurso
url = '<TU_LINK_AQUÍ>'

# Archivo a subir
files = {
    'file': open('<RUTA_DE_TU_ARCHIVO>', 'rb')  # Reemplaza por la ruta de tu archivo
}

# Hacer la petición POST para subir el archivo
response = requests.post(url, files=files)

# Imprimir resultados
print(f"Código de estado: {response.status_code}")
print("Respuesta del servidor:")
print(response.text)  # Cambiar a response.json() si esperas JSON
