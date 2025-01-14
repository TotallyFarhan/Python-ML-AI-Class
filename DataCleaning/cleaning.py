import pandas as pd
import numpy as np

pd.options.display.max_columns = None

#Dataset 1

df = pd.read_csv("Datasets/BL-Flickr-Images-Book.csv")

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

df.drop(columns=to_drop, inplace=True)

df.set_index('Identifier', inplace=True)

regex = r'^(\d{4})'

extr = df['Date of Publication'].str.extract(regex, expand=False)

df['Date of Publication'] = pd.to_numeric(extr)

pub = df['Place of Publication']

london = pub.str.contains("London")

oxford = pub.str.contains("Oxford")

df['Place of Publication'] = np.where(london, 'London', 
                                      np.where(oxford, 'Oxford',
                                               pub.str.replace('-', ' ')))
# Dataset 2

university_towns = []

with open('Datasets/university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            state = line
        else:
            university_towns.append((state, line))

    
towns_df = pd.DataFrame(university_towns, columns=['State', 'RegionName'])

def get_citystate(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

towns_df = towns_df.applymap(get_citystate)


# Dataset 3

olympics_df = pd.read_csv("Datasets/olympics.csv", header = 1)

new_names =  {'Unnamed: 0': 'Country',
             '? Summer': 'Summer Olympics',
             '01 !': 'Gold',
             '02 !': 'Silver',
             '03 !': 'Bronze',
             '? Winter': 'Winter Olympics',
             '01 !.1': 'Gold.1',
             '02 !.1': 'Silver.1',
             '03 !.1': 'Bronze.1',
             '? Games': '# Games',
             '01 !.2': 'Gold.2',
             '02 !.2': 'Silver.2',
             '03 !.2': 'Bronze.2'}


olympics_df.rename(columns = new_names, inplace= True)

print(olympics_df.head())
    
    
    
    
    