# urllib (내장)함수로 html source 가져오기
import urllib.request
html_source = urllib.request.urlopen("https://www.naver.com/")
# print(html_source.read())

# 외장 모듈 requests 사용해서 html source 가져오기
import requests
html = requests.get("https://www.naver.com/")
# print(html.text)

import requests
from bs4 import BeautifulSoup
html = requests.get("https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=109")
html.text
soup = BeautifulSoup(html.text, 'html.parser')
data = soup.find('div', {'class':'text-box'})
print(data)