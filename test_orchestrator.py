# Code pour envoyer des données à l'API
# Sert uniquement de test

import requests

url = "http://127.0.0.1:5000/"
path = ""

data = {"id": 1, "success": True, "data": "blabla"}

print(f"\nLa Hackbox envoie une requête POST à l'API de l'Orchestrateur. Elle contient : {data}")
print("L'Orchestrateur retourne :")
req = requests.post(url+path, data=data)
print(f"CODE: {req.status_code}")
print(req.text)