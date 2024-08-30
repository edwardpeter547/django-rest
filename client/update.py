import requests

endpoint = "http://localhost:8000/api/products/23/"

data = {"title": "Almond Milk Big Size"}

response = requests.put(endpoint, json=data)

print(response.json())
