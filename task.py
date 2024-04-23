import requests
from bs4 import BeautifulSoup

def get_zakuski_list(zakuski_id=None):
    url = 'https://dominopizza.ru/'

    response = requests.get(url=url, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    div_zakuski = soup.find('div', {'id': 'zakuski'})

    div_class_cols = div_zakuski.find_all('div', {'class': 'col'})
    
    zakuski_list = []
    
    for div_class_col in div_class_cols:
        
        
        zakuski_picture = div_class_col.a.div.find(
            'div', {'class': 'product-picture'})

        
        zakuski_detail = div_class_col.a.div.find(
            'div', {'class': 'product-card-content'})
        
        zakuski_id = zakuski_detail.find(
            'div', {'class': 'product-name'}
            ).get('id')
        
        zakuski_name = zakuski_detail.find(
            'div', {'class': 'product-name'}
            ).get_text()
        
        
        zakuski_description = zakuski_detail.find(
            'p', {'class': 'product-description'}
            ).get_text()
        
        zakuski_price = zakuski_detail.find(
            'div', {'class': 'price'}
            ).get_text()
        
        zakuski_list.append({
            'id': zakuski_id,
            'name': zakuski_name,
            'description': zakuski_description,
            'details': zakuski_detail,
            'price': zakuski_price,
            'picture': zakuski_picture.picture.img.get('src')
        })
        
        
        
        print(zakuski_name)
        print(zakuski_description)
        print(zakuski_price)
        print(zakuski_picture.picture.img['src'])
        print('-----------------')
        
    return zakuski_list



zakuski = get_zakuski_list()