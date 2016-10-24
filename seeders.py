#!/usr/bin/python
import requests
import json


base_url='http://localhost:5000'


#response = requests.post(base_url + "/authors", 
#            data = json.dumps({"firstName": "Juancito", 
#                               "lastName": "Tomatito", 
#                               "nationality": "Argentina"}), 
#            headers={'Content-Type': 'application/json'})
#id_author_A_created = response.json()['id']
#response = requests.post(base_url + "/authors", 
#            data = json.dumps({"firstName": "Pedrito", 
#                               "lastName": "Manzanito", 
#                               "nationality": 
#                               "Chile"}), 
#            headers={'Content-Type': 'application/json'})
#id_author_B_created = response.json()['id']
#response = requests.post(base_url + "/authors", 
#            data = json.dumps({"firstName": "Paulito", 
#                               "lastName": "Duraxnito", 
#                               "nationality": "Bolivia"}), 
#            headers={'Content-Type': 'application/json'})
#response = requests.post(base_url + "/books", 
#            data = json.dumps({"title" : "la mama de los anillos",
#                               "publisher" : "zauron",
#                               "editionYear" : 1000,
#                               "editionCountry" : "mordor",
#                               "price" : 10.10,
#                               "isbn" : "1234567890", 
#                               "reputationValue" : 9,
#                               "loanType": "LOCAL",
#                               "gender":"terror"}), 
#            headers={'Content-Type': 'application/json'})
#id_book_A_created = response.json()['id']
#response = requests.post(base_url + "/books", 
#            data = json.dumps({"title" : "la hermana de los anillos",
#                               "publisher" : "gandalf",
#                               "editionYear" : 9999,
#                               "editionCountry" : "gondor",
#                               "price" : 90.10,
#                               "isbn" : "9999999999", 
#                               "reputationValue" : 10,
#                               "loanType": "REMOTE", 
#                               "gender":"terror"}), 
#            headers={'Content-Type': 'application/json'})
#id_book_B_created = response.json()['id']
#response = requests.post(base_url + "/books/" + id_book_A_created + "/authors/" + id_author_A_created, 
#            data = json.dumps({}),
#            headers={'Content-Type': 'application/json'})
#response = requests.post(base_url + "/books/" + id_book_A_created + "/authors/" + id_author_B_created, 
#            data = json.dumps({}),
#            headers={'Content-Type': 'application/json'})
#response = requests.post(base_url + "/members", 
#            data = json.dumps({'firstName' : 'pabloide',
#                               'lastName' : 'profelmi',
#                               'dni' :  '35666666',
#                               'nationality' : 
#                               'Argentina','cuil' : 
#                               '20356666662','phone' : 
#                               '0540111557781234',
#                               'email' : 'asdasd@gmail.com',
#                               'zipCode' : '1602',
#                               'city' : 'vicente lopez',
#                               'state' : 'buenos aires',
#                               'enabled' : 'True',
#                               'reputation' : '7'}), 
#            headers={'Content-Type': 'application/json'})
#id_member_A_created = response.json()['id']
#response = requests.post(base_url + "/members", 
#            data = json.dumps({'firstName' : 'javioide',
#                               'lastName' : 'profelmi',
#                               'dni' :  '357777777',
#                               'nationality' : 'Argentina',
#                               'cuil' : '203577777772',
#                               'phone' : '0540111557666666',
#                               'email' : 'wwwwwwwwwwww@gmail.com',
#                               'zipCode' : '1632',
#                               'city' : 'vicente lopez',
#                               'state' : 'buenos aires',
#                               'enabled' : 'True',
#                               'reputation' : '8'}), 
#            headers={'Content-Type': 'application/json'})
#id_member_B_created = response.json()['id']

#response = requests.post(base_url + "/samples", 
#            data = json.dumps({"bookId": "1",
#                               "barCode":"1234567890", 
#                               "acquisitionDate": "2016-10-06", 
#                               "discardDate": "2016-10-13"}), 
#            headers={'Content-Type': 'application/json'})
#id_sample_A_created = response.json()['id']
#response = requests.post(base_url + "/samples", 
#            data = json.dumps({"bookId": "1" ,
#                               "barCode":"000000000", 
#                               "acquisitionDate": "2016-10-23"}), 
#            headers={'Content-Type': 'application/json'})
#id_sample_B_created = response.json()['id']
#response = requests.post(base_url + "/samples", 
#            data = json.dumps({"bookId": "1",
#                               "barCode":"1111111111", 
#                               "acquisitionDate": "2016-10-23"}), 
#            headers={'Content-Type': 'application/json'})
#id_sample_C_created = response.json()['id']



#response = requests.post(base_url + "/loans",
#            data = json.dumps({'agreedReturnDate' : '2016-10-24',
#                               'withdrawDate' : '2016-10-24',
#                               'loanType': 'REMOTE',
#                               'sampleId': "2", 
#                               'memberId': "1"}),
#            headers={'Content-Type': 'application/json'})
#print(response.text)
response = requests.post(base_url + "/loans",
            data = json.dumps({'agreedReturnDate' :  "2016-10-19",
                               'withdrawDate' : "2016-10-24",
                               "loanType": "REMOTE",
                               'sampleId': "3", 
                               'memberId': "1"}),
            headers={'Content-Type': 'application/json'})
print(response.text)
#response = requests.post(base_url + "/loans",
#            data = json.dumps({'agreedReturnDate' : '2016-10-24',
#                               'returnDate': None, 
#                               'withdrawDate' : '2016-10-22',
#                               'comment' : 'soy de atlanta y q?',
#                               'loanType': 'LOCAL',
#                               'sampleId': id_sample_B_created, 
#                               'memberId': id_member_A_created}),
#            headers={'Content-Type': 'application/json'})
#response = requests.post(base_url + "/loans",
#            data = json.dumps({'agreedReturnDate' :  "2016-10-24",
#                               'returnDate': "2016-10-22",
#                               'withdrawDate' : "2016-10-04",
#                               'comment' : "gol gol gol",
#                               "loanType": "LOCAL",
#                               'sampleId': id_sample_B_created, 
#                               'memberId': id_member_B_created}),
#            headers={'Content-Type': 'application/json'})
