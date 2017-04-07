#import urllib
#import urllib2
import requests
import json
#import goslate
from bs4 import BeautifulSoup
import os
import sys


data = {}

temp  = []

def scrape_title_and_url(soup, url_word):
    try:
        data[url_word] = []
        for items in soup.findAll("tr"):
            title  = items.findAll("td")[0]
            for content in items.findAll("td"):


                temp.append(content.contents)
               # data[url_word].append({title : content.contents})
                #break
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

    print temp[]
if __name__ == "__main__":
    main()















