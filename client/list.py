import requests
from settings import config


endpoint = "http://localhost:8000/api/products/list/"

response = requests.get(endpoint)

print(response.json())
