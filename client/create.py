import requests
from settings import config

headers = {
    "Authorization": "Bearer 61b87afda11022277cc32793b034e3286e2b1996"
}

endpoint = "http://localhost:8000/api/products/"
data = {"title": "Yam Chips", "price": 33.99}

response = requests.post(endpoint, json=data, headers=headers)

print(response.json())
