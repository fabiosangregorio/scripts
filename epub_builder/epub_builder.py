import requests
import csv
import os
import sys
from bs4 import BeautifulSoup
from xhtml2pdf import pisa


def get_links(file_path):
    links = []
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(path) as f:
        reader = csv.reader(f)
        links = [col for row in reader for col in row]
    return links


def get_articles_from_website(links):
    articles = []
    for link in links[1:2]:
        print("Requesting ", link)
        response = requests.get(link)
        if response.status_code != 200:
            raise
        soup = BeautifulSoup(response.text, "html5lib")
        article = soup.find("article", id=id_selector)
        article = f"<html><body>{article}</body></html>"
        articles.append(article)
    return articles


# python epub_builder.py links.csv "article_1-0"
if __name__ == "__main__":
    # parse args
    file_path = sys.argv[1]
    id_selector = sys.argv[2]

    links = get_links(file_path)
    articles = get_articles_from_website(links)
    with open("out.pdf", "w+b") as f:
        pisa_status = pisa.CreatePDF(articles[0], dest=f)