from flask import Flask
import os, json
app = Flask(__name__)
from app import routes
@app.route('/')
@app.route('/app/all_genres')
def all_genres():
    with open(os.path.join(os.path.dirname(__file__), "resources", "all_genres.json")) as file:
        return json.dump(file)
