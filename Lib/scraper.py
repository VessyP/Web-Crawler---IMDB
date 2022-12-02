import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
html = requests.get(BASE_URL)


def scrape_links(html):
    links = list()
    ratings = list()

    soup = BeautifulSoup(html.content, 'html.parser')
    table = soup.find("table", class_="chart full-width")
    # for row in table.findAll("tr"):
        # cells = row.findAll("td")
    scraped_ratings = soup.find_all('td', class_='ratingColumn imdbRating')
    for rating in scraped_ratings:
        rating = rating.get_text().replace('\n', " ")
        rating = rating.strip()
        if not rating:
            ratings.append("N/A")
        else:
            ratings.append(float(rating))
            if float(rating) >= 8:
                a_tag = soup.find('a', href=True)
                links.append(a_tag['href'])

    print(ratings)
    print(links)

    print(len(ratings))     #Test
    print(len(links))


scrape_links(html)






# --------------------------------- VARIANT 2 -----------------------------------


# soup = BeautifulSoup(html.content, 'html.parser')
# scraped_ratings = soup.find_all('td', class_='ratingColumn imdbRating')
#
# ratings = []
# movies = []
# links = []
#
# for rating in scraped_ratings:
#     rating = rating.get_text().replace('\n', " ")
#     rating = rating.strip()
#     if not rating:
#         ratings.append("N/A")
#     else:
#         ratings.append(float(rating))
# # print(ratings)
#
# scraped_movies = soup.find_all('td', class_='titleColumn')
# for movie in scraped_movies:
#     movie = movie.get_text().replace('\n', "")
#     movie = movie.strip(" ")
#     # rx = re.compile(r"^([\w\s:]+).*$", movie)
#     # movie = rx.group(1)
#
#     movies.append(movie)
# # print(movies)
#
# poster_column = soup.find_all('td', class_="posterColumn")
# for column in poster_column:
#     a_tag = soup.find('a', href=True)
#     links.append(a_tag['href'])
# # print(links)
#
# # for r in ratings:
# #     if r != "" and (r[0] == '8' or r[0] == '9' or (r[0] == '1' and r[1] == 0)):
#
#
# movie_dict = {}
# n = 0
# while n in range(len(ratings)):
#     movie_dict[ratings[n]] = [movies[n], links[n]]
#     n += 1
# print(movie_dict)
#
# print(len(ratings))
# print(len(dict.keys(movie_dict)))
