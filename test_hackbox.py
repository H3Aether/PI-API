# Code pour envoyer des données à l'API
# Sert uniquement de test

import requests

url = "http://127.0.0.1:5000/"
path = ""

print("\nL'Orchestrateur envoie une requête GET à l'API de la Hackbox. Elle retourne :")
req = requests.get(url+path)
print(f"CODE: {req.status_code}")
print(req.text)

data = {"action": "start"}

print(f"L'Orchestrateur envoie une requête POST à l'API de la Hackbox. Elle contient : {data}")
print("La Hackbox retourne :")
req = requests.post(url+path, data=data)
print(f"CODE: {req.status_code}")
print(req.text)