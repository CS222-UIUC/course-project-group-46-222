from contextlib import redirect_stderr
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')

def hello_word():
        return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)