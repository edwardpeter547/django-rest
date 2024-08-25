import requests
from settings import config


endpoint = "http://localhost:8000/api/products/create/"
data = {"title": "Avocado", "price": 33.99}

response = requests.post(endpoint, json=data)

print(response.json())
