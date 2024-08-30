import requests
from settings import config

endpoint = "http://localhost:8000/api/products/"
data = {"title": "Almond Milk", "price": 33.99}

response = requests.post(endpoint, json=data)

print(response.json())
