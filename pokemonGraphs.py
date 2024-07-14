import pandas as pd
from matplotlib import pyplot as plt

poke = pd.read_csv("Pokemon.csv")

##poke_stats = poke[['Name', 'Type 1', 'Total', 'Generation', 'Legendary']]
##
##print(poke_stats[poke_stats['Name'] == 'Pikachu'])
##
##poke_common = poke_stats[(poke_stats['Legendary'] == False) & (~poke['Name'].str.contains('Mega'))].drop_duplicates('Name', keep='first')
##
##poke_gen1 = poke_common[poke_common['Generation'] == 1]
##poke_electric = poke_gen1[poke_gen1['Type 1'] == 'Electric']
##
##print("\nAverage Pokemon's Total Power: " + str(poke_common.Total.mean()))
##print("\nAverage Generation 1 Electric Pokemon's Total Power: " + str(poke_electric.Total.mean()))
##
##poke_electric_chart = poke_electric.sort_values(by="Total", ascending=False)
##
##plt.bar(x=poke_electric_chart['Name'], height=poke_electric_chart['Total'])
##plt.show()

ash_list = ['Raichu', 'Mewtwo', 'Pidgeot', 'Venusaur', 'Charizard', 'Blastoise']
gary_list = ['Pidgeot', 'Alakazam', 'Rhydon', 'Exeggutor', 'Arcanine', 'Blastoise']

poke_ash = poke[poke['Name'].isin(ash_list)]
poke_gary = poke[poke['Name'].isin(gary_list)]

ash_graph = plt.figure(1)
plt.bar(x=poke_ash['Name'], height=poke_ash['Total'])
plt.title("Ash's Pokemon Team")

gary_graph = plt.figure(2)
plt.bar(x=poke_gary['Name'], height=poke_gary['Total'])
plt.title("Gary's Pokemon Team")
plt.show()
