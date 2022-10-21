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
    return

@app.route('/', methods=['POST'])
def get_class_type():
    srch_term = request.form.get("type")
    return redirect(url_for('search_page',input=srch_term))


@app.route('/searchPage/<input>')
def search_page(input):
    df = getClassList.getClassList(input)
    return (df[['Subject', 'Number','Course Title']].rename_axis(None)
            .to_html(header="true", table_id="table",index=False))
 
if __name__ == '__main__':
    app.run(debug=True)
    
