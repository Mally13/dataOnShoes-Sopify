from cgitb import handler
from gettext import install
import requests
import json
import pandas as pd


url = 'https://helmboots.com/products.json?limit=250&page1'

r = requests.get(url)

data = r.json()

product_list = []

for item in data['products']:
    title = item['title']
    handle = item['handle']
    created = item['created_at']
    product_type = item['product_type']
    
    for image in item['images']:
        try:
            imagesrc = image['src']
        except:
            imagesrc = 'None'
            
    products = {
        'title':title,
        'handle':handle,
        'created':created,
        'product_type':product_type,
        'image':imagesrc,
    }
    
    product_list.append(products)
    
df = pd.DataFrame(product_list)
df.to_csv('test_run.csv', index=0)

            