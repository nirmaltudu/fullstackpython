import os

from flusk import Flusk

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
