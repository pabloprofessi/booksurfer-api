#!/usr/bin/python
import requests
import json


base_url='http://localhost:5000'


book_list = [
{"title" : "alfajor",
"publisher" : "planeta",
"editionYear" : 2010,
"editionCountry" : "argentina",
"price" : 100,
"isbn" : "2128629716",
"gender" : "fisica",
"reputationValue" : 6,
"loanType" : "REMOTE"},
{"title" : "harry potter",
"publisher" : "planeta",
"editionYear" : 2010,
"editionCountry" : "argentina",
"price" : 200,
"isbn" : "3029855590",
"gender" : "fisica",
"reputationValue" :  8,
"loanType" : "LOCAL"},
{"title" : "pacman trumpeter",
"publisher" : "emece",
"editionYear" : 2010,
"editionCountry" : "argentina",
"price" : 10.50,
"isbn" : "2332932199",
"gender" : "terror",
"reputationValue" : 4,
"loanType" : "REMOTE"},
{"title" : "gringos amigos",
"publisher" : "golondrina",
"editionYear" : 2010,
"editionCountry" : "argentina",
"price" : 10.50,
"isbn" : "1621017673",
"gender" : "terror",
"reputationValue" : 6,
"loanType" : "LOCAL"},
{"title" : "gefatura de bebe gloglo",
"publisher" : "salamndra",
"editionYear" : 2010,
"editionCountry" : "argentina",
"price" : 10.50,
"isbn" : "2649520825",
"gender" : "legislatura",
"reputationValue" : 3,
"loanType" : "REMOTE"},
]

book_id_list = []
for book in book_list:
        response = requests.post(base_url + "/books", 
                   data = json.dumps(book),                        
                   headers={'Content-Type': 'application/json'})
        book_id_list.append(response.json()['id'])
	


author_list = [
{"firstName" : "pablo", 
"lastName" : "professi",
"nationality" : "argentino"},
{"firstName" : "javier", 
"lastName" : "anselmi",
"nationality" : "argentino"},
{"firstName" : "kuasimodo", 
"lastName" : "borbonete",
"nationality" : "frances"},
{"firstName" : "quintaro", 
"lastName" : "grindustre",
"nationality" : "holanda"},
{"firstName" : "gonzo", 
"lastName" : "bonneli",
"nationality" : "hungria"},
{"firstName" : "ratimi", 
"lastName" : "tripipio",
"nationality" : "kasajstan"},
]

author_id_list = []
for author in author_list:
        response = requests.post(base_url + "/authors", 
                   data = json.dumps(author),                        
                   headers={'Content-Type': 'application/json'})
        author_id_list.append(response.json()['id'])

requests.post(base_url + "/books/" + book_id_list[0] + "/authors/" + author_id_list[0], data = json.dumps({}),headers={'Content-Type': 'application/json'})
requests.post(base_url + "/books/" + book_id_list[0] + "/authors/" + author_id_list[1], data = json.dumps({}),headers={'Content-Type': 'application/json'})
requests.post(base_url + "/books/" + book_id_list[1] + "/authors/" + author_id_list[2], data = json.dumps({}),headers={'Content-Type': 'application/json'})
requests.post(base_url + "/books/" + book_id_list[1] + "/authors/" + author_id_list[3], data = json.dumps({}),headers={'Content-Type': 'application/json'})
requests.post(base_url + "/books/" + book_id_list[2] + "/authors/" + author_id_list[4], data = json.dumps({}),headers={'Content-Type': 'application/json'})
requests.post(base_url + "/books/" + book_id_list[2] + "/authors/" + author_id_list[2], data = json.dumps({}),headers={'Content-Type': 'application/json'})
requests.post(base_url + "/books/" + book_id_list[2] + "/authors/" + author_id_list[0], data = json.dumps({}),headers={'Content-Type': 'application/json'})




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
#response = requests.post(base_url + "/loans",
#            data = json.dumps({'agreedReturnDate' :  "2016-10-19",
#                               'withdrawDate' : "2016-10-24",
#                               "loanType": "REMOTE",
#                               'sampleId': "3", 
#                               'memberId': "1"}),
#            headers={'Content-Type': 'application/json'})
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
