""""Will do all the main work of the website, bones of the the project"""
from flask import Flask, redirect, url_for, render_template, request, flash
import scrape
import get_class_list

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = "super secret key"

@app.route('/', methods=["GET"])
def main():
    """"Renders the search box and the background"""
    languages = scrape.scrape()
    return render_template("index.html", languages=languages)

@app.route('/', methods=['POST'])
def get_class_type():
    """"Redirect you to the specific page after you type in the subject type"""
    srch_term = request.form.get("type")
    all_terms = scrape.scrape()
    if srch_term in all_terms:
        return redirect(url_for('search_page',srch_term=srch_term))
    return redirect(url_for('get_class_type'))

@app.route('/searchPage/<srch_term>/')
def search_page(srch_term):
    """"Displays the classes and the GPA after receiving input"""
    data_frame = get_class_list.get_class_list(srch_term)
    data_frame = data_frame[['Subject', 'Number','Course Title']].rename_axis(None)
    data_frame['Course Title'] = (data_frame['Course Title']
                                  .apply(lambda x: f'<a href="{x}">{x}</a>'))
    return data_frame.to_html(header="true", table_id="table",index=False, escape=False)

@app.route('/searchPage/<srch_term>/<class_num>')
def look_up_class(srch_term, class_num):
    """"Actually shows all of the GPAs and the info we have about a certain class such as CS 124"""
    return render_template('searchPage.html', class1=class_num)

if __name__ == '__main__':
    app.run(debug=True)
