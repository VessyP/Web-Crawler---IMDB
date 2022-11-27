import requests
import os
from Lib.constants import DATA_PATH

BASE_URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"


class Crawler():
    def __init__(self, seed):
        self.seed = seed

    # def make_filename(self,url):
    #   """ Extracts domain from a url.
    #     Prepend data_path and append '.html'
    #
    #     :param url: string
    #
    #     return `domain`.html string
    #   """
    #   pass

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

    def run(self):
        """ run the crawler for each url in seed
          Use multithreading for each GET request

        """
        for url in self.seed:
            print(f"URL is {url}")
            html = self.get_html(url)
            self.write_to_file("imdb.html", html)


if __name__ == '__main__':
    seed = [
        "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    ]
    crawler = Crawler(seed)
    crawler.run()



