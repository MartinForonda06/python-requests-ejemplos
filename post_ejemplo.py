import requests

# URL del recurso
url = '<TU_LINK_AQUÍ>'

# Datos a enviar (puedes cambiar este diccionario)
data = {
    'clave1': 'valor1',
    'clave2': 'valor2'
}

# Hacer la petición POST
response = requests.post(url, json=data)  # Cambiar 'json=data' por 'data=data' si es necesario enviar como formulario

# Imprimir resultados
print(f"Código de estado: {response.status_code}")
print("Respuesta del servidor:")
print(response.json())  # Si el contenido es JSON
