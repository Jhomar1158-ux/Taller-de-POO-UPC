from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hola Mundo!!!"

@app.route("/ricky")
def ricky():
    url1='https://rickandmortyapi.com/api/character'
    data = requests.get(url1)
    data_ans=data.json()
    personajes= data_ans["results"]
    for i in personajes:
        print(i['name'])
        print("-")
    return render_template("index.html",personajes=personajes)
        
if __name__ == '__main__':
    app.run()

