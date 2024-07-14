import pandas as pd
from matplotlib import pyplot as plt

poke = pd.read_csv("Pokemon.csv")

poke_stats = poke[['Name', 'Type 1', 'Total', 'Generation', 'Legendary']]

print(poke_stats[poke_stats['Name'] == 'Pikachu'])
print(poke_stats.Total.mean())

poke_common = poke_stats[(poke_stats['Legendary'] == False) & (~poke['Name'].str.contains('Mega'))].drop_duplicates('Name', keep='first', inplace=False)
print(poke_common.Total.mean())

poke_gen1 = poke_common[poke_common['Generation'] == 1]
poke_electric = poke_gen1[poke_gen1['Type 1'] == 'Electric']

print(poke_electric.Total.mean())

#poke_electric = poke_common[poke_common['Type 1'] == 'Electric']
#poke_electric.boxplot(column='Total', by='Generation')
#plt.show()

#poke_electric_chart = poke_electric[['Name', 'Total']]
poke_electric_chart = poke_electric.sort_values(by='Total', ascending=False, inplace=False)
print(poke_electric_chart)
#poke_electric_chart.plot.bar(poke_electric_chart['Total'], poke_electric_chart['Name'], align='center')
#plt.xticks(poke_electric_chart['Total'], poke_electric_chart['Name'])

#x = poke_electric_chart['Name']
#totals = poke_electric_chart['Total']

#x_pos = [i for i, _ in enumerate(x)]

#plt.bar(x=poke_electric_chart['Name'], height=poke_electric_chart['Total'], data=poke_electric_chart)
#plt.bar(x=poke_electric_chart['Name'], height=poke_electric_chart['Total'])

#plt.show()

ash_list = ['Pikachu', 'Butterfree', 'Pidgeot', 'Bulbasaur', 'Charizard', 'Squirtle']
gary_list = ['Pidgeot', 'Alakazam', 'Rhydon', 'Exeggutor', 'Arcanine', 'Blastoise']

poke_ash = poke[poke.loc[:,'Name'].isin(ash_list)].sort_values(by='Total', ascending=False)

poke_gary = poke[poke.loc[:,'Name'].isin(gary_list)].sort_values(by='Total', ascending=False)

print(poke_ash)
print(poke_gary)

##ash_graph = plt.figure(1)
##plt.bar(x=poke_ash['Name'], height=poke_ash['Total'])
##plt.title("Ash's Pokemon Team")
##
##gary_graph = plt.figure(2)
##plt.bar(x=poke_gary['Name'], height=poke_gary['Total'])
##plt.title("Gary's Pokemon Team")
##
##hp_stats = poke_ash['HP']
##attack_stats = poke_ash['Attack']
##defense_stats = poke_ash['Defense']
##speed_stats = poke_ash['Speed']
##special_attack_stats = poke_ash['Sp. Atk']
##special_defense_stats = poke_ash['Sp. Def']
##total_stats = poke_ash['Total']
##
##ash_breakdown = plt.figure(3)
##plt.bar(poke_ash['Name'], hp_stats, color='#00ff00')
##plt.bar(poke_ash['Name'], attack_stats, bottom=hp_stats, color='#ff0000')
##plt.bar(poke_ash['Name'], defense_stats, bottom=(hp_stats+attack_stats), color='#0000ff')
##plt.bar(poke_ash['Name'], speed_stats, bottom=(hp_stats+attack_stats+defense_stats), color='#ffff00')
##plt.bar(poke_ash['Name'], special_attack_stats, bottom=(hp_stats+attack_stats+defense_stats+speed_stats), color='#990099')
##plt.bar(poke_ash['Name'], special_defense_stats, bottom=(hp_stats+attack_stats+defense_stats+speed_stats+special_attack_stats), color='#440044')
##plt.title("Ash's Pokemon Team Stats Breakdown")
#plt.show()

#This is an optional section. You gotta pip install WordCloud to get it working.

##from wordcloud import WordCloud
##pokemon_movie = open('pokemon_transcript.txt', 'r+').read().split(' ')
###Location: http://www.script-o-rama.com/movie_scripts/p/pokemon-the-movie-script-transcript.html
###Tutorial: https://python-graph-gallery.com/260-basic-wordcloud/
##wordcloud = WordCloud(width=480, height=480, margin=0).generate(pokemon_movie)
##plt.imshow(wordcloud, interpolation='bilinear')
##plt.axis("off")
##plt.margins(x=0, y=0)
##plt.show()

#boxplot to show which types are generally the strongest
#poke_common.boxplot(column='Total', by='Type 1')
#plt.show()


poke.plot.scatter(x='Attack', y='Defense', title='Pokemon Attack and Defense')
plt.show()

