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
    times = []
    for time in schedule_times:
        times.append(time.text)
    movies[title]["schedule"] = times

for movie in movies:
    print(movie + "\t" + str(movies[movie]['schedule']))
