#!/usr/bin/python3
"""Start the Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display 'C' followed by the value of < the text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
