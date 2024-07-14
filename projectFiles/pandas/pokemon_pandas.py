#import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 100

#os.getcwd()

poke = pd.read_csv('./Pokemon.csv')

print(poke.head())

print(type(poke))
print(type(poke['Name']))
print(type(poke['Name'].values))
print(type(poke['Name'].values[0]))

print(poke['Name'].head())

print(len(poke))

#sanity check
print(len(poke) == len(poke['Name']))


#Part 2

print(poke.info())

print(poke.describe())

print(poke.isnull().sum())

print(poke['Legendary'].sum())

print(poke[poke['Name'] == 'Pikachu'])

print(poke[poke.loc[:,'Name'].isin(['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle'])])


#making data subsets

image_poke = poke[poke.loc[:,'Name'].isin(['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle'])]

print(image_poke)

poke = poke.rename(columns={'#':'Number'})

print(poke.columns)

only_common = poke[poke['Legendary'] == False]
poke = only_common
print(only_common)

no_mega = poke[~poke['Name'].str.contains('Mega ')]
poke = no_mega
print(no_mega.head())

print(poke['Number'].groupby(poke['Number']).count().sort_values(ascending=False))

nodup_poke = poke.drop_duplicates('Number', keep='first', inplace=False)
print(nodup_poke.head())

nodup_poke.reset_index(inplace=True, drop=True)
print(nodup_poke.head())


#After data cleanup, finding information about the data

print(len(nodup_poke['Number'].unique()))

strongest_type_avg = nodup_poke[['Type 1','Total']].groupby(nodup_poke['Type 1']).mean().sort_values(by='Total',ascending=False)
print(strongest_type_avg)

strongest_type_max = nodup_poke[['Total', 'Name', 'Type 1']].sort_values(by='Total',ascending=False).groupby('Type 1', as_index=False).first()
print(strongest_type_max)

type_frequency = nodup_poke['Type 1'].groupby(nodup_poke['Type 1']).count().sort_values(ascending=False)
print(type_frequency)

top5_poke = nodup_poke[['Name', 'Total']].sort_values(by='Total', ascending=False)[0:5]
print(top5_poke)

generation_comparison = nodup_poke[['Generation', 'Total']].groupby(nodup_poke['Generation']).mean().sort_values(by='Total',ascending=False)
print(generation_comparison)

pikachu_type = nodup_poke['Type 1'][nodup_poke['Name'] == 'Pikachu'].values[0]
print(pikachu_type)

pikachu_rank = nodup_poke[nodup_poke['Type 1'] == pikachu_type].sort_values(by='Total', ascending=False)
pikachu_rank.reset_index(inplace=True)
print(pikachu_rank)


##Visualization

import matplotlib.cm as cm

type_colors = cm.spring(np.linspace(0.05, 0.95, len(type_frequency)))
type_frequency.plot.bar(color=type_colors)
plt.show()
#nodup_poke[nodup_poke['Type 1'].isin(['Bug', 'Water', 'Grass', 'Poison'])].boxplot(column='Total', by='Type 1')
#generation_comparison = generation_comparison.reset_index(level=0, drop=True).reset_index()
#print(generation_comparison)
generation_boxplot = nodup_poke[['Generation', 'Total']]
#generation_boxplot.boxplot(column='Total', by='Generation')
#generation_comparison.boxplot(column='Total', by='Generation')


generation_comparison['Generation'] = generation_comparison['Generation'].astype('str')
gen_colors = cm.summer(np.linspace(0.05, 0.95, len(generation_comparison)))
#generation_comparison.plot.bar(x='Generation', color=gen_colors, title='Comaprison of avg total stats between pokemon generations')

#strongest_type_max.sort_values(by='Total', ascending=False).plot.bar(x='Type 1', color=gen_colors, title='Most powerful pokemon of each type 1')

pikachu_rank['color'] = 'Grey'
pikachu_rank['size'] = 30
pikachu_rank['color'][pikachu_rank['Name']=='Pikachu']='Yellow'
pikachu_rank['size'][pikachu_rank['Name']=='Pikachu']=100
pika_plot = pikachu_rank.plot.scatter(x='Generation', y='Total', c=pikachu_rank['color'], s=pikachu_rank['size'], title='Pikachu vs other electric pokemon')

fig = pika_plot.get_figure()
fig.savefig('pika_plot.png')
#plt.show()



