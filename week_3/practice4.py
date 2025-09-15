import pandas as pd
import requests
from io import StringIO

company_code = input()

site = requests.get('https://finance.naver.com/item/main.naver?code=' + company_code)
html_content = site.text
tables = pd.read_html(StringIO(html_content))

EPS = float(tables[4].values[9][4])
PER = float(tables[4].values[10][4])

FairValue = int(EPS * PER)
print('fair value: {:,.0f}'.format(FairValue))