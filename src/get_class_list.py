"This function will return all the classes that fit the search term"
import pandas as pd

def get_class_list(srch_term):
    """Will return a data frame with srch_Term"""
    data_frame =  pd.read_csv('data/uiuc-gpa-dataset.csv')
    return (data_frame.loc[data_frame['Subject'] == srch_term]
            .drop_duplicates(subset=['Course Title']))
