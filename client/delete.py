import requests

endpoint = "http://localhost:8000/api/products/delete/20/"

response = requests.delete(endpoint)

print(response.status_code)
