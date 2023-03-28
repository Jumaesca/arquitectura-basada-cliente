import requests

# Hacer una solicitud GET al servidor
response = requests.get("http://localhost:5000/")
print(response.content)

# Hacer una solicitud POST al servidor
data = {"nombre": "Juan"}
response = requests.post("http://localhost:5000/saludar", json=data)
print(response.content)
