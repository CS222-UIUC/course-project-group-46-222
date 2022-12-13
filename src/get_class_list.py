"This function will return all the classes that fit the search term"
import pandas as pd

def get_class_list(srch_term, sem):
    """Will return a data frame with srch_Term"""
    data_frame =  pd.read_csv('data/uiuc-gpa-dataset.csv')
    if sem == "all":
        return (data_frame.loc[data_frame['Subject'] == srch_term]
                        .drop_duplicates(subset=['Course Title']))
    sem_arr = sem.split(' ')
    term = sem_arr[0]
    year = sem_arr[1]
    return (data_frame.loc[(data_frame['Subject'] == srch_term) & (data_frame['Year'] == int(year)) & (data_frame['Term'] == term)]
                        .drop_duplicates(subset=['Course Title']))

