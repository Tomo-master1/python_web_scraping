import requests
from bs4 import BeautifulSoup

def get_rakuten():
    url = 'https://search.rakuten.co.jp/search/mall/pythonチュートリアル/'
    responce = requests.get(url)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.searchresultitem')
    
    
    for item in items:
        title = item.select_one('.title')
        print(title.text)
    
get_rakuten()