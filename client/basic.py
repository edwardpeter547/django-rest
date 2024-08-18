import requests

# Declare an endpoint
endpoint = "http://localhost:8000/api/"

# make a http request to the endpoint
response = requests.get(
    endpoint,
    params={"abc": 123},
    json={"name": "Peter Edward"},
)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# Javascript Object Notation almost equivalent to Python Dict
print(response.json())
# print(response.status_code)
