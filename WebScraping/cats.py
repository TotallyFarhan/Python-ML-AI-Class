import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

cats_wiki = 'https://en.wikipedia.org/wiki/List_of_cat_breeds'
page = requests.get(cats_wiki)

soup = BeautifulSoup(page.text, 'html.parser')

cat_table = soup.find('table', class_='wikitable')

breed = []
country = []
origin = []
body_type = []
coat_length = []
pattern = []
images = []

for row in cat_table.find('tbody').find_all('tr'):
    breed_info = row.find_all('td')
    breed_name = row.find('th')
    
    if len(breed_info) == 6:
        breed.append(breed_name.find(text=True))
        country.append(breed_info[0].find(text=True))
        origin.append(breed_info[1].find(text=True))
        body_type.append(breed_info[2].find(text=True))
        coat_length.append(breed_info[3].find(text=True))
        pattern.append(breed_info[4].find(text=True))
        
        if breed_info[5].find('img'):
            images.append(breed_info[5].find('img').get('src'))
        else:   
            images.append('No Image')
            
cat_breed_df = pd.DataFrame(
    {'Breed': breed,
     'Country': country,
     'Origin': origin,
     'Body Type': body_type,
     'Coat Length': coat_length,
     'Pattern': pattern,
     'Images': images
    })

pd.set_option('display.max_columns', None)

cat_breed_df = cat_breed_df.set_index('Breed')

cat_breed_df['Body Type'] = np.where(cat_breed_df['Body Type'].str.contains('\n'), cat_breed_df['Body Type'].str.replace('\n', ''), '')

print(cat_breed_df.head())
