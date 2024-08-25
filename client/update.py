import requests

endpoint = "http://localhost:8000/api/products/update/1/"

data = {"title": "Sweet Orange", "price": 13.05}

response = requests.put(endpoint, json=data)

print(response.json())
