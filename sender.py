# Code pour envoyer des données à l'API
# Sert uniquement de test

import requests

url = "http://127.0.0.1:5000/"
path = ""

data = {"action": "start"}

req = requests.post(url+path, data=data)
print(req.status_code)
print(req.text)