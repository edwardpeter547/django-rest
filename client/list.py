from email import header
from getpass import getpass

import requests
from settings import config

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter Username:\n")
password = getpass("Enter Password:\n")

token_response = requests.post(
    auth_endpoint, json={"username": username, "password": password}
)

if token_response.status_code == 200:
    token = token_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    endpoint = "http://localhost:8000/api/products/"
    response = requests.get(endpoint, headers=headers)
    print(response.json())
