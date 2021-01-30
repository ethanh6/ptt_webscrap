from bs4.element import NavigableString
from bs4 import BeautifulSoup
import requests
from requests import exceptions
from requests.exceptions import HTTPError
import numpy as np
import pandas as pd 
import json
import sys
import os
from requests.models import Response

# choose the board of query
board_name = "studyabroad"

URL = "https://www.ptt.cc/bbs/" + board_name + "/index.html"

def main():
    try:
        response = requests.get(URL)

        # if response was successful, no exception would be raised
        response.raise_for_status()
        print("Response success")

    except HTTPError as http_err:
        print("HTTP error occurred:\n", http_err)

    except Exception as err:
        print("Other error occurred:\n", err)


    # get html 
    html_doc = response.text

    # bs4.BeautifulSoup object
    bs = BeautifulSoup(html_doc, "html.parser")

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
    
    write_to_json(result, board_name_=board_name)

def print_attr(data, attr):
    for d in data:
        for k, v in d.items():
            if k == attr:
                print(v)

def write_to_json(rst, board_name_):
    with open('data/' + board_name_ + ".json", 'w') as fout:
        json.dump(rst, fout)

def read_file():
    with open('data/' + board_name + ".json", "r") as fin:
        DATA = json.load(fin)
    print_attr(DATA, "title")

def remove_data():
    for filename in os.listdir('data'):
        if filename.endswith(".json"):
            os.remove('data/' + filename)
            print("Data" , filename, "removed")


if __name__ == "__main__":
    main()
    # remove_data()
