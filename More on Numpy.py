# Creating a random array

import numpy as np

rand = np.random.randint (1,50,10)

print (rand)

# Slicing an array - taking a part of it 

print (rand [2:5])

# If starting or ending not given then will start from 0 or finish with last

print (rand [:8])
print (rand [6:])

# Third number is the step

print (rand [1: :2])

# Reverses array

print (rand [ : :-1])

# Slicing with selected index

print (rand [[0,2,3,6,9]])

# Conditional slicing - retrieves evens, more than etc.

print (rand [rand % 2 == 0])
print (rand [rand > 25])

# For more dimensions

rand2 = np.random.randint (1,50,(6,6))

print (rand2)

print (rand2 [2:,3:])
print (rand2 [2:,1:])
print (rand2 [1: :2,2: :2])

print (rand2 [rand2 > 25])

# Sort an array - in an increasing order 

print (rand)
print (np.sort (rand))

# Evaluating expressions

r = np.random.randint (5,15,10)
h = np.random.randint (15,20,10)
v = 3.14 * r*r*h
print (r)
print (h)
print (v)