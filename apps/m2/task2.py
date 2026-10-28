from bs4 import BeautifulSoup, SoupStrainer
import sys

file_name = sys.argv[1]

all_tags = SoupStrainer(True)

with open(file_name, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser", parse_only=all_tags)

for tag in soup.find_all(True):
    print(tag)