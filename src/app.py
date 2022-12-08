""""Will do all the main work of the website, bones of the the project"""
from flask import Flask, redirect, url_for, render_template, request, flash
import scrape
import get_class_list
import get_semesters
import gpa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


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
    #number = data_frame.loc[data_frame['Course Title'] == 'Intro to Popular TV & Movies', 'Number'].squeeze()
    # print(number)
    print(data_frame)
    data_frame['Course Title'] = (data_frame['Course Title']
                                  .apply(lambda x: f'<a href="{sem}/{x}/{number_C(data_frame, x)}">{x}</a>'))
                    
    return render_template("searchPage.html", data_table = data_frame.to_html(header="true", table_id="table",index=False, escape=False), srch_term = srch_term, languages=languages, options=options, sem=sem)

# Returns the number of the column given the data_frame and the Course Title as input    
def number_C(data_frame, x):
    return data_frame.loc[data_frame['Course Title'] == x, 'Number'].squeeze()


@app.route('/searchPage/<srch_term>/<sem>/<course_title>/<number>')
def look_up_class(srch_term, course_title, sem, number):
    """"Actually shows all of the GPAs and the info we have about a certain class such as CS 124"""
    gpa.clearMem()

    languages = scrape.scrape()
    options = get_semesters.get_semesters() 
    print(sem)
    print(srch_term)
    print(course_title)
    print(number)
    number = int(number)
    datafr = gpa.createData(number, srch_term, sem)
    
    graphs = gpa.createImages(number, srch_term, sem)
    print(graphs[0])
    length = len(graphs)
    return render_template('displayData.html', data_table = datafr.to_html(header="true", table_id="table",index=False, escape=False), class1=course_title, languages = languages, options=options, sem=sem, length = length, graphs=graphs)
    
if __name__ == '__main__':
    app.run(debug=True)

