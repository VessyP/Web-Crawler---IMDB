import requests
import os
from Lib.constants import DATA_PATH
import re
from bs4 import BeautifulSoup
from scraper import links

BASE_URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"


class Crawler():
    def __init__(self, seed):
        self.seed = seed

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
git in
            return r.text


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
        # print(genre_list)

        film_info = {'title': title,
                     'director': director,
                     'genre': genre_list}

        print(film_info)



    def run(self):
        """ run the crawler for each url in seed
          Use multithreading for each GET request

        """
        for url in self.seed:
            # print(f"URL is {url}")
            html = self.get_html(url)
            self.write_to_file("imdb.html", html)


if __name__ == '__main__':
    seed = [
        "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    ]
    crawler = Crawler(seed)
    crawler.run()

    for link in links:
        print(link)
        crawler.get_page_data(link)

