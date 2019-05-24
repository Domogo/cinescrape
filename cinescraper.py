from bs4 import BeautifulSoup
import urllib.request as urllib


# html_page = urllib.urlopen("https://www.blitz-cinestar.hr/cinestar-pula")
html_page = urllib.urlopen("https://www.blitz-cinestar.hr/cinestar-rijeka-4dx")
soup = BeautifulSoup(html_page, features="lxml")

my_divs = soup.find_all("div", {"class": "movie_box"})
titles = []
for div in my_divs:
    title = div.find("a", {"class": "movieItemTitle"}).text
    print(title)
    titles.append(title)
