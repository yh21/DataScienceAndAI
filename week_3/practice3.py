import pandas as pd
import requests
from io import StringIO

# 웹에서 HTML 가져오기
site = requests.get('https://therk987.github.io/teachablemachine/sample_site.html')
html_content = site.text  # 문자열로 HTML 가져오기

# 읽어오기
tables = pd.read_html(StringIO(html_content))
print(tables)
print(tables[0].values)