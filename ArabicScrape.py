#import urllib
#import urllib2
import requests
import json
#import goslate
from bs4 import BeautifulSoup
import os
import sys
import pprint
import re

data = dict()

temp  = []

def scrape_title_and_url(soup, url_word):
    try:
        data[url_word] = []
        for items in soup.findAll("tr"):
            title  = str(items.findAll("td")[0].text)
            if str(title) != 'English':
                for content in items.findAll("td"):
                    if content != items.findAll("td")[0]:
                        content = re.sub("<[^>]*>", "", content.encode_contents())
                        if content != "" or '' or None or "''":
                            data.setdefault(str(title), [])
                            if len(data[title]) < 2:
                                data[title].append(str(content))
                    elif str(title) or title == " " or "" or '' or None:
                        continue
                    elif str(content) or content == " " or "" or '' or None:
                        continue
    except:
    	pass


def main():

    urls = []

    home = requests.get("http://arabic.desert-sky.net/vocab.html")
    list = BeautifulSoup(home.content, "html.parser")
    for links in list.findAll("tr"):
        for address in links.findAll("a"):
            urls.append("http://arabic.desert-sky.net/" + address['href'])


    for url in urls:
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        url_split = url.split("/")[-1:]
        url_word = url_split[0].split(".")[0]
        scrape_title_and_url(soup, url_word)
        break

    #pp = pprint.PrettyPrinter(indent=4)
    #print pp.pprint(data.values().get("cat"))
    #print pp.pprint(data)
    with open('result.json', 'w') as fp:
        json.dump(data, fp, sort_keys=True)

if __name__ == "__main__":
    main()















