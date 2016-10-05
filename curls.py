import requests
from pprint import pprint 
import json

base_url='http://localhost:5000'

#curls de test
#---------------
#
#rutas:
#/ping
#/books
#/books/<id>/samples
#/authors
#/members
#/loans

response = requests.get(base_url + "/ping" )
pprint(response.text)

def test_entity(entity, data_post, data_put):
    pprint("############## " + entity + " ##################")
    
    response = requests.post(base_url + "/" + entity, data = json.dumps(data_post), headers={'Content-Type': 'application/json'})
    print("POST output:")
    pprint(response.json())
    id_created = response.json()['id']
    
    response = requests.put(base_url + "/" + entity + "/" + id_created , data = json.dumps(data_put), headers={'Content-Type': 'application/json'})
    response = requests.put(base_url + "/" + entity + "/" + id_created , data = json.dumps(data_post), headers={'Content-Type': 'application/json'})
    print("PUT output:")
    pprint(response.json())
    
    print("GET all output:")
    response = requests.get(base_url + "/" + entity , headers={'Content-Type': 'application/json'})
    pprint(response.json())
    
    print("GET one output:")
    response = requests.get(base_url + "/" + entity  + "/" + id_created , headers={'Content-Type': 'application/json'})
    pprint(response.json())
    
    #print("DELETE output:")
    #response = requests.delete(base_url + "/" + entity  + "/" + id_created , headers={'Content-Type': 'application/json'})
    #pprint(response.json())


#AUTHOR
data_post = {"firstName": "Juancito", "lastName": "Tomatito", "nationality": "Argentina"}
data_put = {"firstName": "Juancito", "lastName": "Tomatito", "nationality": "Boliviana"}
entity = "authors"

test_entity(entity, data_post, data_put)

#data_post = {
#  "title": "senor de los anillos",
#  "publisher": "planeta",
#  "image_url": "https://media.creativemornings.com/uploads/user/avatar/49419/Bechtel_Profile_Square.jpg",
#  "publish_year": "1999",
#  "editorial": "garbarino",
#  "authors": [
#    {
#      "first_name": "Juan",
#      "last_name": "Tomate",
#      "nationality": "Argentina"
#    },
#    {
#      "first_name": "Pedro",
#      "last_name": "Tomate",
#      "image_url": "https://media.creativemornings.com/uploads/user/avatar/49419/Bechtel_Profile_Square.jpg",
#      "nationality": "Argentina"
#    }
#  ]
#}












