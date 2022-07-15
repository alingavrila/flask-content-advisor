'''An advisor on what content type to try'''
from flask import Flask
from random import randint
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'The docker is running well :)'


if __name__ == '__main__':
    # Make the server publicly available by default
    app.run(debug=True, host='0.0.0.0')
