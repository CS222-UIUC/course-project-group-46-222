import pandas as pd

def get_semesters():
    data_frame =  pd.read_csv('data/uiuc-gpa-dataset.csv')
    year_term = data_frame[['Term', 'YearTerm']].values.tolist()
    *y,=map(list,{*map(tuple,year_term)})
    for row in y:
        row[1] = row[1][0:row[1].index('-')]
    y.sort(key=lambda x:x[1],reverse=True)
    to_return = []
    for row in y:
        string = ""
        for item in row:
            string += item
            string += " "
        to_return.append(string)
    return to_return
