import requests
from bs4 import BeautifulSoup

html = requests.get("https://news.naver.com/main/ranking/popularDay.naver")
soup = BeautifulSoup(html.content, 'html.parser')
news = soup.find_all('a', {"class":"list_title nclicks('RBP.rnknws')"})

# for i in news:
#     print(i.text)

hotnews = list()
for i in news:
    hotnews.append(i.text + '\n')

with open('hotnews.txt', 'w') as f:
    f.writelines(hotnews)
    f.close()