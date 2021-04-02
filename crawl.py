import bs4 
import xml.etree.ElementTree as Xet
import pandas as pd
import requests
import json 
import xmltodict
import httplib2
import time

#def get_sitemap(url):
#    response = requests.get(url)
#    with open("sitemap.xml", "wb") as f:
#        f.write(response.content)

def get_sitemap(url):
    response = requests.get(url)
    sitemap = response.content
    data_dict = xmltodict.parse(sitemap)
    json_data = json.dumps(data_dict)
    with open('sitemap.json', 'w') as json_file:
            json_file.write(json_data)
            json_file.close()


def convert_sitemap_to_json():
    pass
#    with open('sitemap.xml', encoding="utf8") as xml_file:
#        data_dict = xmltodict.parse(xml_file.read())
#        xml_file.close()
#        json_data = json.dumps(data_dict)
#
#        with open('sitemap.json', 'w') as json_file:
#            json_file.write(json_data)
#            json_file.close()

def get_urls_list():
    addresses = []
    with open('sitemap.json') as f:
        data = json.load(f)

        for val in data["urlset"]['url']:
            addresses.append(val["loc"])
    df = pd.DataFrame(addresses, columns=["urls"])
    df.index.name = "index"
    df.to_csv("url_list.csv")

def get_links(url):
    print(url)
    time.sleep(0.3)
    http = httplib2.Http()
    links = []
    try: 
        status, page = http.request(url)
        for link in bs4.BeautifulSoup(page, parse_only=bs4.SoupStrainer('a'), features="html.parser"):
            if link.has_attr('href'):
                links.append(link['href'])
    except:
        links.append("Page Error")
    return links

def crawl_for_links():
    df = pd.read_csv('url_list.csv')
    df["links"] = df['urls'].apply(get_links)
    df.to_csv("crawled_site.csv")