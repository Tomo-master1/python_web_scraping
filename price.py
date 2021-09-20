import requests
from bs4 import BeautifulSoup

keyword = input('比較したい商品を入力してください:\n')

def get_rakuten():
    #?s=2は価格が安い順, f=2は送料無料
    url = 'https://search.rakuten.co.jp/search/mall/' + keyword +'?f=2&s=2'
    responce = requests.get(url)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.searchresultitem')
    
    item_number = 0
    price_list = []
    
    for item in items:
        title = item.select_one('.title').text.replace('\n','')
        price = item.select_one('.important').text.replace(',', '').replace('円', '')
        price_list.append(price)
        print(item_number)
        print(title)
        print(price + '\n')
        item_number += 1
    selected_item_number = int(input('楽天：商品番号を入力してください\n'))
    selected_price = int(price_list[selected_item_number])
    return selected_price
        
def get_yahoo():
    url = 'https://shopping.yahoo.co.jp/search?p=' + keyword + '&ship=on&X=2'
    responce = requests.get(url)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('._2W0PXaK-syIW')
    
    item_number = 0
    price_list = []
    
    for item in items:
        title = item.select_one('._2EW-04-9Eayr').text
        price = item.select_one('._3-CgJZLU91dR').text.replace(',', '')
        price_list.append(price)
        print(item_number)
        print(title)
        print(price + '\n')
        item_number += 1
    selected_item_number = int(input('yahoo：商品番号を入力してください\n'))
    selected_price = int(price_list[selected_item_number])
    return selected_price
        
    
    
rakuten_price = get_rakuten()
yahoo_price = get_yahoo()

print('楽天：{0}円\nyahoo：{1}円'.format(rakuten_price, yahoo_price))

if rakuten_price < yahoo_price:
    print('楽天の方が安い')
elif yahoo_price < rakuten_price:
    print('yahooの方が安い')
else:
    print('同じ値段')