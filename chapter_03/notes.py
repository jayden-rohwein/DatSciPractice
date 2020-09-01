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


#    ---------   pd concatenation

pd.concat[ser1, ser2]
pd.concat[df3,df4]

# con specify to concat by axis or rows
pd.concat[df3,df4, axis='col']  # or axis=1

# can hadle duplicate indicies in a variety of ways
pd.concat([df1,df2]), verify_integrity=True) # throws error if their are duplicate results
pd.concat([df1, df2], ignore_index=True) # creates a new index for duplicate results
pd.concat([df1, df2],keys=['x','y'] # creates a second level of indexes 

# with joins
pd.concat([df1, df2], join='inner')    # relation db style inner join
pd.concat([df1, df2], join_axes[df5.columns]) # specify which columsn to join on

# append returns a new list & is less efficient then pd.concat
df1.append(df2)






pd.merge(df1, df2)  # will reconize a shared column and join on that column, indexs are lost
# can be one to one, one to many, and many to many 
# one to many - creates an additional column, a column may have repeated results
# many to many - creates an additional entry(s) along with column,

pd.merge( df1, df2 on='employee') # con specify the merge key
pd.merge( df1, df2, left_on='employee' right_on='name')

# drop name because that has same info as emplyee, don't need it in our dataframe
pd.merge( df1, df2, left_on='employee' right_on='name').drop('name, axis=1')

#can merge by index also
pd.merge(df1, df2, left_index=True, right_index=True)
pd.join(df1, df2)   # merge that defauts to joining on indices



#merge by default is an "inner join", this can be explicitly set
pd.join(df1, df2, how="inner")


