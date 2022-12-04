import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.imdb.com/"
html = requests.get(urljoin(BASE_URL, "chart/moviemeter/?ref_=nv_mv_mpm"))

links = list()
ratings = list()

def scrape_links(html):


    soup = BeautifulSoup(html.content, 'html.parser')
    table = soup.find("table", class_="chart full-width").tbody
    rows = table.find_all('tr')

    for tr in rows:
        rating_td = tr.find('td', class_='ratingColumn imdbRating')
        rating = rating_td.get_text().replace('\n', " ")
        rating.strip()
        if rating == " ":
            ratings.append("N/A")
        else:
            ratings.append(float(rating))
            if float(rating) >= 8:
                link_td = tr.find('td', class_='titleColumn')
                a = link_td.a
                links.append(urljoin(BASE_URL, a['href']))

    # print(ratings)       # Test
    # print(links)
    #
    # print(len(ratings))  # Test
    # print(len(links))


scrape_links(html)
