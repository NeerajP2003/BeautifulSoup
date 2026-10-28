from bs4 import BeautifulSoup
import sys

file_name = sys.argv[1]

with open(file_name, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

for tag in soup.find_all("p"):
    tag["class"] = "test"

with open("modified_paragraphs.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
