from flask import Flask
from flask_cors import *

app = Flask(__name__)

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run()