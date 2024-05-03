from bs4 import BeautifulSoup
import lxml
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, 'html.parser')

article_tags = soup.find_all(name='h3', class_='title')
movie_titles = [el.text for el in article_tags][::-1]

with open('movies.txt',"w", encoding='utf-8') as f:
    for title in movie_titles: f.write(f'{title}\n')