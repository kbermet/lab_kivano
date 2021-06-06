import urllib.request
import bs4 as bs
import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup



class Writer:
    def __init__(self, products):
        self.depDF = pd.DataFrame(
            {'title': products.titles,
             'link': products.links,
             'category': products.categories,
             }
        )

    def write_to_csv(self):
        csvFileContents = self.depDF.to_csv(index=False)
        with open("kivano_test.csv", "w", encoding='utf-8') as f:
            f.write(csvFileContents)


class Products:
    def __init__(self, ads):
        self.ads = ads
        self.titles = []
        self.links = []
        self.categories = []
        for ad in ads:
            self.titles.append(ad.title)
            self.links.append(ad.link)
            self.categories.append(ad.category)

class Bike:
    def __init__(self, title, link, category):
        self.title = title
        self.link = link
        self.category = category

def get_html(url):
    response = requests.get(url)
    return response.text

def find_deps(html):
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_='list-view').find_all('div', class_='item')
    url = 'https://www.kivano.kg'
    for ad in ads:
        try:
            title = ad.find('div', class_='listbox_title').text
            print(title)
        except:
            title = 'No title'
        try:
            link = ad.find('div', class_='listbox_title').find('a').get('href')
            print(link)
        except:
            link = 'No link'
        try:
            category = ad.find('span', class_='page-title').text
            print(category)
        except:
            category = 'No category'

if __name__=='__main__':
    url = 'https://www.kivano.kg'
    par = Products(find_deps(url))
    w = Writer(par)
    w.write_to_csv()

find_deps(html)