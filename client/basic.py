import requests

# Declare an endpoint
endpoint = "http://localhost:8000/api/"

# make a http request to the endpoint
response = requests.post(
    endpoint,
    json={"content": "Paw-Paw"},
)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# Javascript Object Notation almost equivalent to Python Dict
print(response.json())
# print(response.status_code)
