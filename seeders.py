import requests
import json


base_url='http://localhost:5000'


requests.post(base_url + "/authors", data = json.dumps({"firstName": "Juancito", "lastName": "Tomatito", "nationality": "Argentina"}), headers={'Content-Type': 'application/json'})
requests.post(base_url + "/authors", data = json.dumps({"firstName": "Pedrito", "lastName": "Manzanito", "nationality": "Chile"}), headers={'Content-Type': 'application/json'})
requests.post(base_url + "/authors", data = json.dumps({"firstName": "Paulito", "lastName": "Duraxnito", "nationality": "Bolivia"}), headers={'Content-Type': 'application/json'})