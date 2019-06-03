from bs4 import BeautifulSoup
import urllib.request as urllib


# html_page = urllib.urlopen("https://www.blitz-cinestar.hr/cinestar-pula")
html_page = urllib.urlopen("https://www.blitz-cinestar.hr/cinestar-rijeka-4dx")
soup = BeautifulSoup(html_page, features="lxml")

my_divs = soup.find_all("div", {"class": "movie_box"})
movies = {}
for div in my_divs:
    title = div.find("a", {"class": "movieItemTitle"}).text
    movies[title] = {}
    schedule_times = div.find_all("a", {"class": "tips"})
    movie_types = div.find_all("div", {"class": "vrstafilmauni"})
    times = []
    types = []
    for time in schedule_times:
        times.append(time.text)
    for movie in movie_types:
        types.append(movie.text)

    movies[title]["schedule"] = times
    movies[title]["type"] = types

for movie in movies:
    if not len(movies[movie]['schedule']) == 0:
        print(movie + "\t" + str(movies[movie]['schedule']) + str(movies[movie]['type']))
