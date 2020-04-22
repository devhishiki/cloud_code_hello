"""
A sample Hello World server.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "Hello World!!!"
    return message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
