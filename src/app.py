from contextlib import redirect_stderr
from flask import Flask, redirect, url_for, render_template, request
import scrape
import pandas as pd
import getClassList

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

@app.route('/searchPage', methods= ["POST"])
def searchPage():
        srch_term = request.form.get("type")
        print(srch_term)
        df = getClassList.getClassList(srch_term)
        return df.to_html(header="true", table_id="table")


 
if __name__ == '__main__':
    app.run(debug=True)
    
