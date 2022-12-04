""""Will do all the main work of the website, bones of the the project"""
from flask import Flask, redirect, url_for, render_template, request, flash
import scrape
import get_class_list
import get_semesters
import gpa

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = "super secret key"

@app.route('/', methods=["GET"])
def main():
    """"Renders the search box and the background"""
    languages = scrape.scrape()
    options = get_semesters.get_semesters()
    return render_template("index.html", languages=languages, options=options)

@app.route('/', methods=['GET','POST'])
def get_class_type():
    """"Redirect you to the specific page after you type in the subject type"""
    srch_term = request.form.get("type")
    sem_selector = request.form.get("sem-select")
    if sem_selector is None:
        sem_selector = "all"
    all_terms = scrape.scrape()
    if srch_term in all_terms:
        return redirect(url_for('search_page',srch_term=srch_term, sem=sem_selector))
    return redirect(url_for('get_class_type'))

@app.route('/searchPage/<srch_term>/<sem>')
def search_page(srch_term,sem):
    """"Displays the classes and the GPA after receiving input"""
    data_frame = get_class_list.get_class_list(srch_term, sem)
    languages = scrape.scrape()
    options = get_semesters.get_semesters()
    data_frame = data_frame[['Subject', 'Number','Course Title']].rename_axis(None)
    data_frame['Course Title'] = (data_frame['Course Title']
                                  .apply(lambda x: f'<a href="{sem}/{x}">{x}</a>'))
    return render_template("searchPage.html", data_table = data_frame.to_html(header="true", table_id="table",index=False, escape=False), srch_term = srch_term, languages=languages, options=options, sem=sem)


@app.route('/searchPage/<srch_term>/<sem>/<class_num>')
def look_up_class(srch_term, class_num, sem):
    """"Actually shows all of the GPAs and the info we have about a certain class such as CS 124"""
    languages = scrape.scrape()
    options = get_semesters.get_semesters() 
    datafr = gpa.createData(class_num, srch_term, sem)
    return render_template('displayData.html', data_table = datafr.to_html(header="true", table_id="table",index=False, escape=False), class1=class_num, languages = languages, options=options, sem=sem)

if __name__ == '__main__':
    app.run(debug=True)
