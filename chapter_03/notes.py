import numpy as np
import pandas as pd


#
#   notes from chapter 3
#   on pandas
#
#   not ment to be runnable, just notes


data = pd.Series([0.25,0.5,0.75,1.0])

print(data)
print(data.values)
print(data.index)


population_dict ={'California':38332521,'Texas':26448193, 'New York':19651127, 'Florida': 19552860, 'Illinois':12882135}
population      = pd.Series(population_dict)
area_dict       = {'California':423967, 'Texas':695662, 'New York': 141297, 'Florida': 170312, 'Illinois':149995}
area            = pd.Series(area_dict)

states = pd.DataFrame({'population': population, 'area':area})
print("\n", states,"\n")


indA = pd.Index([1,3,5,7,9])
indB = pd.Index([2,3,5,7,11])

print( indA & indB ) #intersection of index sets
print( indA | indB ) #union of index sets
print( indA ^ indB ) #symetrical differences of sets




# can use indexs, slicing & masking with panda series

data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])

data['a':'c']
data[0,2]           # final index is included when slices with explicit index

data[data > 0.3]


#  data.loc[]    to specify using an explicit inex
#  data.iloc[]   to specify using implicit index


# can assign to dataframe like a python dictionary
states['density'] = states['population'] / states['area']

#  implicit / explicit indexing for dataframes as well
states.iloc[:3, :2]
states.loc[:'illinois', :"population"]


#
#               used for detecting null values
#
df.isnull()
df.notnull()
df.dropna()
df.fillna()

df.fillna(method='ffill') # forward-fill, fills null with previous data
df.fillna(method='bfill') # backward-fill, fills null with next piece of data
#spceify axis for dataframe
# if prev or next value is not available, it will remain nan

#can have multi-dimensional indexes for data,
# can use stack / unstack to change extra dimensional from index to values
df.stack()
df.unstack()


#   can use Panda IndexSlice object for slicing multi-d indexes / columns
#
idx = pd.IndexSlice 
data.loc[idx[:,1], idx[:,'HR']]

#sort entire index or just level
data.sort_index()
data.sort_level()

# can unstack specific levels of index / columns
data.unstack(level=1)


