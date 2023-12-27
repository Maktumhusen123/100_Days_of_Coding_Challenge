from bs4 import BeautifulSoup
import requests

response = requests.get("https://empireonline.com/movies/features/best-movies-2")
content = response.text

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movies_list = [movie.getText() for movie in movies]
# print(movies_list)

# for n in range(len(movies_list)-1, -1, -1):
#    print(movies_list[n])

sorted_movies = movies_list[::-1]
with open("movies.txt", "w") as file:
    for movie in sorted_movies:
        file.write(f"{movie}\n")
