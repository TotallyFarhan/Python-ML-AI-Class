import pandas as pd
 
poke = pd.read_csv('Pokemon.csv')

poke = poke[poke['Legendary'] == False]
poke = poke.drop_duplicates('#', keep='first')
poke = poke[['Total', 'Name']]
poke = poke.sort_values(by='Total',ascending=False)
poke = poke.head(6)

print(poke)
