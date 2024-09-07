import requests

headers = {
    "Authorization": "Bearer 61b87afda11022277cc32793b034e3286e2b1996"
}

endpoint = "http://localhost:8000/api/products/1/"

response = requests.get(endpoint, headers=headers)

print(response.json())
