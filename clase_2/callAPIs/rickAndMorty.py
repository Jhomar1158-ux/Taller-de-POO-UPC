import requests

url1='https://rickandmortyapi.com/api/character'
data = requests.get(url1)
data_ans=data.json()
personajes= data_ans["results"]
for i in personajes:
    print(i['name'])
    print("-")
    