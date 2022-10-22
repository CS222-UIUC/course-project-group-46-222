""""Scrapes the website and gives us a list of all the subject types"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape():
    """"Main scraper returns a list of all of the majors and their abbreviations"""
    link_ = "http://catalog.illinois.edu/courses-of-instruction/"
    page = requests.get(
        link_,
        timeout=5)

    soup = BeautifulSoup(page.content, "html.parser")
    majors = []

    for link in soup.find_all('li'):
        if ' - ' in link.text:
            majors.append(link.text)

    short_major = {}

    list1 = []
    for major in majors:
        split = major.split(' - ')
        short_major[split[0]] = split[1]
        list1.append(split[0])

    data_frame = pd.DataFrame(list(short_major.items()))
    data_frame.columns =['Short', 'Long']
    data_frame = data_frame.set_index('Short')

    data_frame.to_csv('data/majors.csv', sep='\t')
    return list1
