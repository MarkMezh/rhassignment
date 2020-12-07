import flask
from flask import Flask, request
app = Flask(__name__)
from urllib.parse import urlparse


@app.route('/')
def hello():
    return "this is my first project"


def get_url():
    o = urlparse(request.base_url)
    host = o.hostname
    return host


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

