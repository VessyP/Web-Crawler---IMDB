import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from Lib.constants import DATA_PATH
from Lib.constants import BASE_URL
from Lib.scraper import scrape_links
from Lib.db import DB


class Crawler():
    def __init__(self, path):
        self.main_page_url = urljoin(BASE_URL, path)
        self.db = DB()
        self.status = 0

    def write_to_file(self, filename, content):
        """ Write string to given filename"""

        with open(DATA_PATH + filename, "w", encoding="utf-8") as f:
            f.write(content)

    def get_html(self, url):
        """ Make GET request and save content to file
          First try with SSL verification (default),
          if error => print a message."""

        print(f'get_html: {url}')
        headers = {"user-agent": "Chrome/107.0.5304.123"}
        r = requests.get(url, headers=headers)
        # print(f'r.encoding: {r.encoding}')
        if r.ok:
            # r.encoding = 'UTF-8'

            return r.text
        else:
            print('!!!!!!!!!!!!!!! : Problem getting page')
            print(r)
            exit()

    def create_empty_table(self):
        """ Deleting any existing imdb table
        and creating an empty one. """
        self.db.drop_imdb_table()
        self.db.create_imdb_table()

    def get_page_data(self, html):
        """ Getting title, director and genre
        for each film with rating >=8 and
        storing them into dictionary."""

        film_info = {}
        soup = BeautifulSoup(html, 'html.parser')
        title_class = soup.find('div', class_='sc-80d4314-1 fbQftq')
        title = title_class.find('h1').getText(strip=True)

        content_container = soup.find('div', class_='ipc-metadata-list-item__content-container')
        director = content_container.find('li').getText(strip=True)

        storyline_genres = soup.find('div', class_="ipc-chip-list__scroller")
        genre_list = list()
        genre_a = storyline_genres.find_all('a')
        for a in genre_a:
            genre = a.getText(strip=True)
            genre_list.append(genre)
            genre_all = '; '.join(genre_list)

        film_info = {'title': title,
                     'director': director,
                     'genre': genre_all}

        print(film_info)
        return film_info

    def process_pages(self, links):
        """For each film with rating >=8:
        getting the html of the page, running a function
        to store the required info in a dictionary and
        saving it to a database. """

        for link in links:
            html = self.get_html(link)
            film_info = self.get_page_data(html)
            self.db.insert_row(film_info)

    def run(self):
        """ Run the crawler."""

        self.create_empty_table()
        html = self.get_html(self.main_page_url)

        # get list of links to be scrapped for data
        links = scrape_links(html)

        # get data for each film and save it to a DB
        self.process_pages(links)

        # Indicate that the crawler is ready
        self.update_status()

    def update_status(self):
        """Updating the status of the crawler
        after it finishes its job."""

        self.status = 1
        print('Crawler finish its job!')
