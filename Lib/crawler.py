import requests
import os
from Lib.constants import DATA_PATH
import re
from bs4 import BeautifulSoup
from Lib.scraper import links
from Lib.db import DB

BASE_URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"


class Crawler():
    def __init__(self, seed):
        self.seed = seed
        self.db = DB()
        self.status = 0

    # def make_filename(self,url):
    #     pass
    #   """ Extracts domain from a url.
    #     Prepend data_path and append '.html'
    #
    #     :param url: string
    #
    #     return `domain`.html string     ?????????????????????????????
    #   """
    #     file_name = url.split('/')[5] + ".html"
    #
    # make_filename(BASE_URL)

    def write_to_file(self, filename, content):
        """ Write string to given filename
            :param filename: string
            :param content: sring
        """
        with open(DATA_PATH + filename, "w", encoding="utf-8") as f:
            f.write(content)

    def get_html(self, url):
        """ Make GET request and save content to file
          First try with SSL verification (default),
          if error => disable SSL verification

          :param url: string
        """
        r = requests.get(url)
        # print(f'r.encoding: {r.encoding}')
        if r.ok:
            # r.encoding = 'UTF-8'

            return r.text

    def create_empty_table(self):
        self.db.drop_imdb_table()
        self.db.create_imdb_table()

    def get_page_data(self, html):
        film_info = {}

        # for link in links:
        #     html = link
        headers = {"user-agent": "Chrome/107.0.5304.123"}
        html = requests.get(link, headers=headers)
        soup = BeautifulSoup(html.content, 'html.parser').body

        title_class = soup.find('div', class_='sc-80d4314-1 fbQftq')
        title = title_class.find('h1').getText(strip=True)
        # print(title)

        content_container = soup.find('div', class_='ipc-metadata-list-item__content-container')
        director = content_container.find('li').getText(strip=True)
        # print(director)

        storyline_genres = soup.find('div', class_="ipc-chip-list__scroller")
        genre_list = list()
        genre_a = storyline_genres.find_all('a')
        for a in genre_a:
            genre = a.getText(strip=True)
            genre_list.append(genre)
            genre_all = '; '.join(genre_list)
        # print(genre_list)

        film_info = {'title': title,
                     'director': director,
                     'genre': genre_all}

        print(film_info)
        self.db.insert_row(film_info)

    def run(self):
        """ run the crawler for each url in seed
          Use multithreading for each GET request

        """
        for url in self.seed:
            # print(f"URL is {url}")
            html = self.get_html(url)
            self.write_to_file("imdb.html", html)

        self.create_empty_table()





    def update_status(self):
        """Updating the status of the crawler
        after it finishes its job."""

        self.status = 1
        print('Crawler finish its job!')


# if __name__ == '__main__':
seed = [
    "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
]
crawler = Crawler(seed)
crawler.run()
crawler.create_empty_table()
#
for link in links:
    # print(link)

    crawler.get_page_data(link)
