from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/hola')
def hello_world():
    return "Hola Mundo!!!"
@app.route('/jhomar')
def hola_jhomar():
    return "Hola Jhomar!!!"
@app.route("/rickySerie")
def ricky():
    url1='https://rickandmortyapi.com/api/character'
    data = requests.get(url1)
    data_ans=data.json()
    personajes= data_ans["results"]
    for i in personajes:
        print(i['name'])
        print("-")
    return render_template("dashboard.html", personajes=personajes)
    
    

        
if __name__ == '__main__':
    app.run()

