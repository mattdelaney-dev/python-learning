import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_html = response.text

soup = BeautifulSoup(movie_html, "html.parser")

movie_text = soup.find_all(name="h3", class_="title")
movite_titles = [movie.getText() for movie in movie_text]
movies = movite_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")