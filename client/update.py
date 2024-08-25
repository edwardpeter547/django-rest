import requests

endpoint = "http://localhost:8000/api/products/update/5/"

data = {"title": "Guava Fruit", "price": 124.05}

response = requests.put(endpoint, json=data)

print(response.json())
