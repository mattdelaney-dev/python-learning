import os
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, "website.html")

with open(file_path) as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchor = soup.find_all(name="a")

for tag in all_anchor:
    # tag.getText()
    tag.get("href")

heading = soup.find(name="h1", id="name")
# print(heading)

company_url = soup.select_one(selector="p a")
print(company_url)