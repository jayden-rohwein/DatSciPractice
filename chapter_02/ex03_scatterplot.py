import numpy as np 
rand = np.random.RandomState(42)
import matplotlib.pyplot as plt
import seaborn; seaborn.set()



mean = [0,0]
cov = [[1,2], [2,5]]
X = rand.multivariate_normal(mean,cov,100)


#plt.scatter(X[:,0], X[:,1])
#plt.savefig("chapter_02/scatterplot.png")

indices = np.random.choice(X.shape[0], 20, replace=False)
selection = X[indices]

plt.scatter(X[:,0], X[:,1], alpha=0.3)
plt.scatter(selection[:,0], selection[:,1],
    facecolor='none', s=200)
plt.savefig("chapter_02/scatterplot02.png")

