from contextlib import redirect_stderr
from flask import Flask, redirect, url_for, render_template, request
import scrape
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def main():
        if request.method == "GET":
                languages = scrape.scrape()
                return render_template("index.html", languages=languages)  


if __name__ == '__main__':
    app.run(debug=True)