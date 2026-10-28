from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer
import sys

file_name = sys.argv[1]

replacer = SoupReplacer("b", "blockquote")

with open(file_name, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser", replacer=replacer)

with open("modified_tags.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
