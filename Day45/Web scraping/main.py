from bs4 import BeautifulSoup
#import lxml
with open("./welcome.html", encoding="utf8") as web:
    contents = web.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml")

# print(soup)
# print(soup.prettify())

# below statements will get hold of only first element
# print(soup.a)
# print(soup.p)

# All elements can be controlled as follows
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# To get text and href of anchor tag
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name.getText())

headings = soup.select(selector=".heading")
print(headings)
