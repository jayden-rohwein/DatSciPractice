import numpy as np
print(numpy.__version__)


#
#       Basic syntax for numpy library
#

# create an array filled with linear sequence starting at 9, ending at 20, stepping by 2
np.arange(0,20,2)

# create an array of five values evenly spaced between 0 and 1
np.linespace(0,1,5)

# create a 3x3 array of uniformly distributed random values between 0 and 1
np.random.random(3,3)


# create a 3x3 aray of normally distributed random values
np.random.normal(0,1,(3,3))

# create a 3x3 array of random integers in the interval [0,10)
np.random.randint(0,10,(3,3))

# create an uninitialized array of three integers
# values will be whatever happens to already exist at the memory location
np.empty(3)



x1 = np.random.randint((10, size=6))
x2 = np.random.randint(10, size=(3,4)) 
x3 = np.random.randint(10, size=(3,4,5))

print("x3 ndim:  ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size:  ", x3.size)
print("x3 dtpe:  ", x3.dtype)

x = np.arange(10)

x[:5] # first five elements

x[5:] # last five elements

x[4:7] # middle subarray

x[::2] # every other element

x[1::2] # every other element starting at index 1 

x[::-1] # all the elements reversed


# ----- mulit dimmentional Arrays -----

x2[:2,:3] # two rows, three columns

x2[:3, ::2] # all 3 rows, every other columns

x2[::-1, ::-1] # reverse both dimmentions

x2[:,0] # first column
x2[0,:] # first row

x2[:2,:2].copy()  # creates a copy of the slice, not a pointer to original one


# takes 1d array and 'reshapes' it to a 3x3 2d array
grid = np.arange(1,10).reshape((3,3))

#concatenate 2 arrays
np.concatenate(row,row)

# can concatenate 2d arrays by either axis, zero index default 0
np.concatenate([grid,grid], axis=1)

# adds a row to a 2d array
np.vstack( row, grid)

# adds a column to a 2d array
np.hstack(grid, column)

# splits array x on idicies the indicies 3,5
np.split(x, [3,5])

# splits a 2d array into upper and lower
upper, lower = np.vsplit( grid, [2])

# splits a 2d array into left and right
left, right = np.hsplit(grid, [2])

#np dsplit will split 3d arrays on the z axis
closer, farther = np.dsplit( cube, [2])



#   Trig operations

np.sin(theta)
np.cos(theta)
np.tan(theta)
np.arcsin(x)
np.arccos(x)
np.arctan(x)

np.exp(x)      #e  ^ x
np.exp2(x)     #2  ^ x
np.power(3,x)  #3  ^ x
np.log(x)
np.log2(x)
np.log10(x)


# reduce will apply the add funcion untill there is only one result left
np.add.reduce(x)  

#accumulate will return all the intermediate steps of redcue
np.add.accumulate(x)

x = [1,2,3,4,5]
np.multiply.outer(x,x)
#result will be a times table

#
#  broudcasting - operate between arrays of different sizes and shapes
#







