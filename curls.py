import requests
from pprint import pprint 
import json

base_url='http://localhost:5000'

#curls de test
#---------------
#
#rutas:
#/ping
#/authors
#/samples
#/books
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
    pprint(response.json())
    response = requests.put(base_url + "/" + entity + "/" + id_created , data = json.dumps(data_post), headers={'Content-Type': 'application/json'})
    print("PUT output:")
    pprint(response.json())
    
    print("GET all output:")
    response = requests.get(base_url + "/" + entity , headers={'Content-Type': 'application/json'})
    pprint(response.json())
    
    print("GET one output:")
    response = requests.get(base_url + "/" + entity  + "/" + id_created , headers={'Content-Type': 'application/json'})
    pprint(response.json())
    
    print("DELETE output:")
    response = requests.delete(base_url + "/" + entity  + "/" + id_created , headers={'Content-Type': 'application/json'})
    pprint(response.json())


#AUTHOR
author_data_post = {"firstName": "Juancito", "lastName": "Tomatito", "nationality": "Argentina"}
author_data_put = author_data_post
author_data_put["nationality"] = "Boliviana"
author_entity = "authors"

test_entity(author_entity, author_data_post, author_data_put)

#BOOK
sample_data_post = {"barCode":"1234567890", "acquisitionDate": "2016-10-06"}
sample_data_put = {"barCode":"1234567890", "acquisitionDate": "2016-10-06", "discardDate": "2016-10-08"}
book_entity = "books"
book_data_post = {
    "title" : "la mama de los anillos",
    "publisher" : "zauron",
    "editionYear" : "1000",
    "editionCountry" : "mordor",
    "price" : "10.10",
    "isbn" : "1234567890", 
    "reputationValue" : "9",
    "loanType": "LOCAL",
    "samples" : [sample_data_post, sample_data_put],
    "authors" : [author_data_post, author_data_put] 
    }

book_data_put = {
    "title" : "la hermana de los anillos",
    "publisher" : "gandalf",
    "editionYear" : "9999",
    "editionCountry" : "gondor",
    "price" : "90.10",
    "isbn" : "9999999999", 
    "reputationValue" : "10",
    "loanType": "REMOTE",
    "authors" : [author_data_post, author_data_put] 
    }

test_entity(book_entity, book_data_post, book_data_put)

#SAMPLE

sample_entity = "samples"
response = requests.post("http://localhost:5000/books", data = json.dumps({"title" : "la mama de los anillos","publisher" : "zauron","editionYear" : "1000","editionCountry" : "mordor","price" : "10.10","isbn" : "1234567890", "reputationValue" : "9", "loanType": "LOCAL", "samples" : [],"authors" : [] }), headers={'Content-Type': 'application/json'})
id_created = response.json()['id']
sample_data_post["bookId"] = id_created
sample_data_put["bookId"] = id_created
test_entity(sample_entity, sample_data_post, sample_data_put)
response = requests.delete("http://localhost:5000/books/" + str(id_created) , headers={'Content-Type': 'application/json'})


#MEMBERS

member_data_post = {
    'firstName' : 'pabloide',
    'lastName' : 'profelmi',
    'dni' :  '35666666',
    'nationality' : 'Argentina',
    'cuil' : '20356666662',
    'phone' : '0540111557781234',
    'email' : 'asdasd@gmail.com',
    'zipCode' : '1602',
    'city' : 'vicente lopez',
    'state' : 'buenos aires',
    'enabled' : 'True',
    'reputation' : '7'}
member_data_put = {
    'firstName' : 'javioide',
    'lastName' : 'profelmi',
    'dni' :  '357777777',
    'nationality' : 'Argentina',
    'cuil' : '203577777772',
    'phone' : '0540111557666666',
    'email' : 'wwwwwwwwwwww@gmail.com',
    'zipCode' : '1632',
    'city' : 'vicente lopez',
    'state' : 'buenos aires',
    'enabled' : 'True',
    'reputation' : '8'}

member_entity = "members"

test_entity(member_entity, member_data_post, member_data_put)

#LOANS

loan_data_post = {
        'agreedReturnDate' :  "2016-10-24",
        'returnDate' : None,
        'withdrawDate' : "2016-10-22",
        'comment' : "aguante tangalanga",
        "loanType": "LOCAL",
        }
loan_data_put = {
        'agreedReturnDate' :  "2016-10-24",
        'returnDate' : "2016-10-22",
        'withdrawDate' : "2016-10-04",
        'comment' : "aguante tangalanga el regreso",
        "loanType": "REMOTE",
        }
loan_entity = "loans"


response = requests.post("http://localhost:5000/books", data = json.dumps({"title" : "la mama de los anillos","publisher" : "zauron","editionYear" : "1000","editionCountry" : "mordor","price" : "10.10","isbn" : "1234567890", "reputationValue" : "9", "loanType": "LOCAL","samples" : [],"authors" : [] }), headers={'Content-Type': 'application/json'})
sample_data_post["bookId"] = response.json()['id']

response = requests.post("http://localhost:5000/samples", data = json.dumps(sample_data_post), headers={'Content-Type': 'application/json'})
sample_id_created = response.json()['id']

response = requests.post("http://localhost:5000/members", data = json.dumps(member_data_post), headers={'Content-Type': 'application/json'})
member_id_created = response.json()['id']

loan_data_post['sampleId'] = sample_id_created
loan_data_post['memberId'] = member_id_created
loan_data_put['sampleId'] = sample_id_created
loan_data_put['memberId'] = member_id_created


test_entity(loan_entity, loan_data_post, loan_data_put)

response = requests.delete("http://localhost:5000/books/" + sample_data_post["bookId"], headers={'Content-Type': 'application/json'})
response = requests.delete("http://localhost:5000/members/" + member_id_created, headers={'Content-Type': 'application/json'})

##################################
#SPECIAL CASES
################
#/samples/<sample_id>/loans

pprint("######################### /samples/<sample_id>/loans ##########################")
response = requests.post("http://localhost:5000/books", data = json.dumps({"title" : "la mama de los anillos","publisher" : "zauron","editionYear" : "1000","editionCountry" : "mordor","price" : "10.10","isbn" : "1234567890", "reputationValue" : "9", "loanType":"LOCAL", "samples" : [],"authors" : [] }), headers={'Content-Type': 'application/json'})
sample_data_post["bookId"] = response.json()['id']

response = requests.post("http://localhost:5000/samples", data = json.dumps(sample_data_post), headers={'Content-Type': 'application/json'})
sample_id_created = response.json()['id']

response = requests.post("http://localhost:5000/members", data = json.dumps(member_data_post), headers={'Content-Type': 'application/json'})
member_id_created = response.json()['id']

loan_data_post['sampleId'] = sample_id_created
loan_data_post['memberId'] = member_id_created

response = requests.post("http://localhost:5000/loans", data = json.dumps(loan_data_post), headers={'Content-Type': 'application/json'})

new_loan_id = response.json()['id']

response = requests.get("http://localhost:5000/samples/" + sample_id_created + "/loans", headers={'Content-Type': 'application/json'})

pprint(response.json())
response = requests.delete("http://localhost:5000/loans/" + new_loan_id , headers={'Content-Type': 'application/json'})
response = requests.delete("http://localhost:5000/samples/" + sample_id_created , headers={'Content-Type': 'application/json'})
response = requests.delete("http://localhost:5000/books/" + sample_data_post["bookId"], headers={'Content-Type': 'application/json'})
response = requests.delete("http://localhost:5000/members/" + member_id_created, headers={'Content-Type': 'application/json'})

