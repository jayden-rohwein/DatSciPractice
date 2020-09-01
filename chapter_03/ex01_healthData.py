import numpy as np
import pandas as pd 


index = pd.MultiIndex.from_product([[2013,2014],[1,2]], names=['year','visit'])
columns = pd.MultiIndex.from_product([['Bob','Guido','Sue'],['HR','Temp']], names=['subject','type'])

# mocked data
data = np.round(np.random.randn(4,6),1)
data[:,::2] *= 10
data += 37


health_data = pd.DataFrame(data, index=index, columns=columns)
data_mean = health_data.mean(level='year').mean(axis=1, level='type')

print('\n','Health Data:', '\n')
print(health_data, '\n\n')
print('Average Heart Rate and Temperature per Year:', '\n')
print(data_mean, '\n\n')

