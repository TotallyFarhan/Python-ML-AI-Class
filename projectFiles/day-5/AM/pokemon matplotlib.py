import pandas as pd
from matplotlib import pyplot as plt
 
poke = pd.read_csv("Pokemon.csv")
 
poke_stats = poke[['Name', 'Type 1', 'Total', 'Generation', 'Legendary']]
 
print(poke_stats[poke_stats['Name'] == 'Pikachu'])
 
poke_common = poke_stats[(poke_stats['Legendary'] == False) & (~poke['Name'].str.contains('Mega'))].drop_duplicates('Name', keep='first')
 
poke_gen1 = poke_common[poke_common['Generation'] == 1]
poke_electric = poke_gen1[poke_gen1['Type 1'] == 'Electric']
 
poke_electric_chart = poke_electric.sort_values(by='Total', ascending=False)
 
plt.bar(x=poke_electric_chart['Name'], height=poke_electric_chart['Total'])
plt.show()
