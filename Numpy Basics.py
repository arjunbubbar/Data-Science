# Numeric Python - library helps you do mathematical operations
# Useful for data science and ML
# array - collection of values, no commas, can convert to array
# array easier to do mathematical operations

import numpy as np

nums = [23,45,60,91,212]

print (nums)
print (type (nums))

numsarray = np.array (nums)
print (numsarray)
print (type (numsarray))

for i in nums:
    print (i / 2)

print (numsarray / 2)

# cannot do nums/2 so its easier 

# array of zeros 
# integers no decimals, can change float default to different type

zero = np.zeros (5, int)
print (zero)

table = np.zeros ((3,4), int)
print (table)

# array of ones 

table1 = np.ones ((4,5), int)
print (table1)

# array should have numbers falling in a range
# arange - create an array with numbers in a range

table2 = np.arange (2,20)
print (table2)

# can specify a step

table3 = np.arange (1, 50, 5)
print (table3)

# find dimension

print (table.ndim)
print (table1.ndim)
print (table2.ndim)

# finds number of rows and columns

print (table.shape)
print (table2.shape)

# finds total items

print (table.size)
print (table1.size)
print (table2.size)

# can find different arrangements - permutations, same items in different orders

print (np.random.permutation (table3))
print (np.random.permutation (table3))
print (np.random.permutation (table3))

# array of random numbers, give range and then how many numbers, can give rows and columns

print (np.random.randint (0,100,10))
print (np.random.randint (0,100,(3,3)))

# change shape of array

table4 = np.random.randint (0,100,(3,4))
print (table4)
print (table4.reshape ((2,6)))
