import sys

from bs4 import BeautifulSoup, SoupReplacer


def add_test_class(tag):
    if tag.name == "p":
        tag["class"] = "test"

if len(sys.argv) < 2:
    print("Usage: python task7.py <html_file>")
    sys.exit(1)
    
file_name = sys.argv[1]
replacer = SoupReplacer(xformer=add_test_class)

with open(file_name, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser", replacer=replacer)

with open("modified_paragraphs.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
