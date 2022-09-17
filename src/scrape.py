import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape():
    URL = "http://catalog.illinois.edu/courses-of-instruction/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    majors = []

    for link in soup.find_all('li'):
        if ' - ' in link.text:
            majors.append(link.text)

    shrthandToMajor = {}

    list1 = []
    for major in majors:
        split = major.split(' - ')
        shrthandToMajor[split[0]] = split[1]
        list1.append(split[0])

    df = pd.DataFrame(list(shrthandToMajor.items()))
    df.columns =['Short', 'Long']
    df = df.set_index('Short')

    df.to_csv('data/majors.csv', sep='\t')
    return list1