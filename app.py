# import requests
from Lib.crawler import Crawler
# import os
from Lib.db import DB


BASE_URL = ["https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"]

if __name__ == "__main__":
    crawler = Crawler(BASE_URL)
    crawler.run()

