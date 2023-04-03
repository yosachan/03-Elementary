import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as req

html="""
<html>
    <head>
        <meta charset="utf-8">
        <title>ＸＸＸＸＸＸＸＸ
        </title>
    </head>
    <body>
        <h1>こんにちは！</h1>
    </body>
</html>
"""

html
print("here")
parse_html = BeautifulSoup(html, "html.parser")
print(parse_html)
print("herehere")
print(parse_html.prettify())

print("ここから本番")

url = "https://www.xxxxxxxxxxx.com/"
response = req.urlopen(url)

parse_html = BeautifulSoup(response, "html.parser")

print(parse_html)
print(parse_html.title)
print(parse_html.title.string)
print(parse_html.find_all("a"))
title_lists = parse_html.find_all("a")
title_lists[1:10]
title_lists[10].string
title_lists[10].attrs["href"]

title_list=[]
url_list=[]

for i in title_lists:
    title_list.append(i.string)
    url_list.append(i.attrs["href"])

print(title_list)
print(url_list)

df_title_url = pd.DataFrame({"Title":title_list, "Url":url_list})

print(df_title_url)

df_notnull = df_title_url.dropna(how="any")
print(df_notnull)

df_notnull["Title"].str.contains("ＸＸ")

df_contain_python = df_notnull[df_notnull["Title"].str.contains("ＸＸ")]
print(df_contain_python)

df_contain_python.to_csv("output.csv")
