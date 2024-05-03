from bs4 import BeautifulSoup
from dotenv import load_dotenv
import lxml
import requests
import os

load_dotenv()

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, 'html.parser')

article_tags = soup.find_all(name='h3', class_='title')
movie_titles = [el.text for el in article_tags][::-1]

with open(os.environ.get("FILEPATH"),mode="w", encoding='utf-8') as f:
    print("[FILE WRITE] -> movies.txt")
    for title in movie_titles: f.write(f'{title}\n')
    print("[FILE CLOSE] -> movies.txt")