from bs4 import BeautifulSoup, SoupStrainer
import sys

file_name = sys.argv[1]

only_links = SoupStrainer("a")

with open(file_name, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser", parse_only=only_links)

for tag in soup.find_all("a"):
    print(tag)