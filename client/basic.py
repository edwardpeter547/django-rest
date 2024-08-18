import requests

# Declare an endpoint
endpoint = "http://localhost:8000/api"

# make a http request to the endpoint
response = requests.get(endpoint)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# Javascript Object Notation almost equivalent to Python Dict
print(response.text)
print(response.status_code)
