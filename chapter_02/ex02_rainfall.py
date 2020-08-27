import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn; seaborn.set() 

data = pd.read_csv('chapter_02/Seattle2014.csv')
rainfall = np.array(data["PRCP"])
inches = rainfall / 254 # 1/10mm -> inches
print(inches)

plt.hist(inches,40)
plt.savefig("chapter_02/rain_fall.png")

# construct a must of all days with rain
rainy = ( inches > 0 )

#construct a mask of all sumer days - june 21st is the 172 day & 90 days later is 262
summer = (np.arange(365)  < 262) & ( np.arange(365) > 172 )



print("Median precip on rainy days in 2014 ( inches):   ",
    np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches):   ",
    np.median(inches[summer]))
print("Maximum precip on sumer days in 2014 (inches):   ",
    np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
    np.median(inches[rainy & ~summer]))