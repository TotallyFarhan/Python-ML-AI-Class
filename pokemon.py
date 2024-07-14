import pandas as pd

pokemon = pd.read_csv('Pokemon.csv')

pokemon_team = pokemon[pokemon['Legendary'] == False].sort_values(by="Total", ascending = False).drop_duplicates('Type 1', keep='first').head(6)
print(pokemon_team)
