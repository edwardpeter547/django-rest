import requests

# Declare an endpoint
endpoint = "https://httpbin.org/anything"

# make a http request to the endpoint
response = requests.get(
    endpoint,
    json={"age": 33},
    # data={"name": "Peter Edward", "school": "Sharda University"},
    headers={"content-type": "application/x-www-form-urlencoded"},
)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# Javascript Object Notation almost equivalent to Python Dict
print(response.json())
print(response.status_code)
