from config.scrape import LIMIT
from config.url import BB_URL
from bs4 import BeautifulSoup
import requests

class BB_Scraper:
    def __init__(self) -> None:
        response = requests.get(BB_URL)
        response.raise_for_status()
        bb_webpage = response.text

        soup = BeautifulSoup(bb_webpage, 'html.parser')

        #article_tags = soup.find(name='li', class_='o-chart-results-list__item')

        song_tags = soup.select("li ul .c-title")
        songs = [el.getText().replace('\n','').replace('\t','') for el in song_tags]

        artist_tags = soup.select("li ul .c-label")
        #artists = [el.getText().replace('\n','').replace('\t','') for el in artist_tags]

        #print(songs)
        print(artist_tags)

        #print(songs)

        ##class="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light  lrv-u-padding-l-1@mobile-max"


BB_Scraper()