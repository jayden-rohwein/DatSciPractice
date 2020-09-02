import pandas as pd
import numpy as np 



#
#       Finding the states with the Largest and Smallest Density
#

pop     = pd.read_csv('chapter_03/state-population.csv')
areas   = pd.read_csv('chapter_03/state-areas.csv')
abbrevs = pd.read_csv('chapter_03/state-abbrevs.csv')

# print(pop.head()); print(areas.head()); print(abbrevs.head())

merged = pd.merge( pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', axis=1)

# see if their is any null data to address
# print(merged.isnull().any())
# print(merged[merged['population'].isnull()].head())
# print(merged.loc[merged['state'].isnull(), 'state/region'].unique())
# 
# some data about population was missing from original source
# data was missing from our abbreviations table

merged.loc[merged['state/region'] == 'PR', 'state']  = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
#print(merged.isnull().any())
#
# no more null data was in the states column

final = pd.merge(merged, areas, on='state', how='left')
#print(final.isnull().any())
#
# null data in area column
# print( final['state'][final['area (sq. mi)'].isnull()].unique() )
# null data is for United states as whole, not relevant so we can drop it
final.dropna(inplace=True)

data2010 = final.query("year == 2010 & ages == 'total'")
data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)

print('\n')
print( density.head(), '\n')
print( density.tail(), '\n')