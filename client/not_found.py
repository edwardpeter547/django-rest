import requests

endpoint = "http://localhost:8000/api/products/1000/"

response = requests.get(endpoint)

print(response.json())
