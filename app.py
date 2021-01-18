# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import os

app = Flask(__name__)
WHO = os.environ.get('WHO')

@app.route('/')
def hello_world():
    if WHO:
        return WHO
    else:
        return 'Hello World!!'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
