from pyexpat.errors import messages
from flask import Flask
from flask import request
import collections
from pymongo import MongoClient
from make_audio import audio_gen

mongo_uri = 'mongodb://localhost:27017'
client = MongoClient(mongo_uri)

db = client['appdb']
col = db['users']


app = Flask(__name__)

@app.route('/<id>')
def users_action(id):
    results = col.find({'id': int(id)})
    for n in results:
        message = n['message']
        print("Message id: " + id)
        print("Mensaje a procesar: " + message)
    audio_gen(message)
    return("Audio generado")

@app.route('/')
def home():
    print("Home Page in")
    return("Home page")

app.run(debug=True)