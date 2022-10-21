import pandas as pd 

def getClassList(srch_term):
    df =  pd.read_csv('data/uiuc-gpa-dataset.csv')
    return (df.loc[df['Subject'] == srch_term].drop_duplicates(subset=['Course Title']))

print(getClassList('CS'))