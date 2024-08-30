import requests

endpoint = "http://localhost:8000/api/products/25/"

response = requests.delete(endpoint)

print(response.status_code)
