from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
content = response.text

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

articles = soup.find_all(name="span" , class_="titleline")
# print(article_tag)

article_text = []
article_links = []
# print(article_text)
for article in articles:
    article_text.append(article.getText())
    article_links.append(article.find(name="a").get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]
highest_voted_index = article_upvotes.index(max(article_upvotes))

print(article_text[highest_voted_index])
print(article_links[highest_voted_index])
print(article_upvotes[highest_voted_index])





