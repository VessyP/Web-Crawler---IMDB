from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Lib.constants import BASE_URL

def scrape_links(html):
    """Scrape the html, find all
    films with rating >= 8 and
    gather the links in a list."""

    links = list()
    ratings = list()
    soup = BeautifulSoup(html, 'html.parser')
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

    return links


