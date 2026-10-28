from bs4 import BeautifulSoup, SoupStrainer
import sys

file_name = sys.argv[1]

tags_with_id = SoupStrainer(attrs={"id": True})

with open(file_name, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser", parse_only=tags_with_id)

for tag in soup.find_all(id=True):
    print(tag)