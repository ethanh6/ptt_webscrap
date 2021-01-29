import requests
from bs4 import BeautifulSoup

# 想要搜尋的看板
title = "studyabroad"

URL = "https://www.ptt.cc/bbs/" + title + "/index.html"
article_href = []
req = requests.get(URL)
bs = BeautifulSoup(req.text, "html.parser")

# list of tag with <a>
result = bs.select("div.title")

for i in result[:5]:
    print(i)

# article_href = [item.select("a").get("href") for item in result]

print(article_href)


