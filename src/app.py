""""Will do all the main work of the website, bones of the the project"""
from flask import Flask, redirect, url_for, render_template, request
import scrape
import get_class_list

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=["GET"])
def main():
    """"Renders the search box and the background"""
    languages = scrape.scrape()
    return render_template("index.html", languages=languages)

@app.route('/', methods=['POST'])
def get_class_type():
    """"Redirect you to the specific page after you type in the subject type"""
    srch_term = request.form.get("type")
    return redirect(url_for('search_page',srch_term=srch_term))


@app.route('/searchPage/<srch_term>')
def search_page(srch_term):
    """"Displays the classes and the GPA after receiving input"""
    data_frame = get_class_list.get_class_list(srch_term)
    return (data_frame[['Subject', 'Number','Course Title']].rename_axis(None)
            .to_html(header="true", table_id="table",index=False))
if __name__ == '__main__':
    app.run(debug=True)
    