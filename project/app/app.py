from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is a Flask application!'

