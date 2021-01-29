from bs4.element import NavigableString
import requests
from bs4 import BeautifulSoup

# 想要搜尋的看板
title = "studyabroad"

URL = "https://www.ptt.cc/bbs/" + title + "/index.html"
req = requests.get(URL)

# BeautifulSoup object
bs = BeautifulSoup(req.text, "html.parser")

# select all 'div' tag with attribute class='title'
# return a bs4.element.ResultSet object
div = bs.find_all(name='div', class_="title")

result = []

for i in div:
    # get only tag element, skip NavigableString object
    if isinstance(i, NavigableString): continue

    print(i)

    article_title = i.contents
    article_href  = i.href


    # result.append({"title": article_title, "url": article_href})

for i in result:
    print(i)

# alternative approach, using CSS selector, return a list
# div = bs.select("div.title")

