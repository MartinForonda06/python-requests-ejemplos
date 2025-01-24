import requests

# URL del recurso
url = '<TU_LINK_AQUÍ>'

try:
    # Hacer la petición GET con un tiempo límite (timeout)
    response = requests.get(url, timeout=5)
    
    # Verificar si la respuesta fue exitosa
    response.raise_for_status()  # Lanza un error si el código de estado es 4xx/5xx
    print("Petición exitosa:")
    print(response.json())  # Cambiar a response.text si no esperas JSON

except requests.exceptions.Timeout:
    print("Error: La solicitud tomó demasiado tiempo y se agotó.")
except requests.exceptions.ConnectionError:
    print("Error: No se pudo establecer conexión con el servidor.")
except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error desconocido: {e}")
