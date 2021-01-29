from bs4.element import NavigableString
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd 
import json

# 想要搜尋的看板
board_name = "studyabroad"

URL = "https://www.ptt.cc/bbs/" + board_name + "/index.html"

# get the website
req = requests.get(URL)

# get html 
html_doc = req.text

# bs4.BeautifulSoup object
bs = BeautifulSoup(html_doc, "html.parser")


# print(type(bs))
# print(bs.title)
# print(bs.title.name)
# print(bs.title.string)
# print(bs.title.parent.name)
# print(bs.a)
# print(type(bs.a))

# print(bs.a.string)
# print(type(bs.a.string))

# select all 'div' tag with attribute class='title'
# return a bs4.element.ResultSet object
div = bs.find_all('div', class_="r-ent")

result = []
for item in div:
    attr = {}

    # locate title and url
    title = item.find("div", class_="title")

    try:
        attr["title"] = title.find('a').string
    except:
        attr["title"] = None

    try:
        attr["url"] = title.find('a')['href']
    except:
        attr["url"] = None

    # locate date
    try:
        attr["date"] = item.find("div", class_="date").string
    except:
        attr["date"] = None
    

    # locate upvotes
    attr["upvotes"] = item.find("div", class_='nrec').string

    result.append(attr)

def print_attr(data, attr):
    for d in data:
        for k, v in d.items():
            if k == attr:
                print(v)

def write_to_json():
    with open('data/' + board_name + ".json", 'w') as fout:
        json.dump(result, fout)

write_to_json()


def read_file():
    with open('data/' + board_name + ".json", "r") as fin:
        DATA = json.load(fin)
    print_attr(DATA, "title")

read_file()
