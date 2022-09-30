from contextlib import redirect_stderr
from flask import Flask, redirect, url_for, render_template, request
import scrape
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=["GET"])
def main():
        if request.method == "GET":
                languages = scrape.scrape()
                return render_template("index.html", languages=languages)  

@app.route('/', methods=['POST'])
def get_class_type():
        text = request.form['type']
        text = text.upper()
        return text
 
if __name__ == '__main__':
    app.run(debug=True)
    