# pd for pandas

import pandas as pd

nums = [1,3,4,34,321,925,321,45,4,26,1,29,4,87]

print (nums)
print (type (nums))

ser = pd.Series (nums)

print (ser)
print (type (ser))

# Series prints the index and the values

# Prints the index

print (ser [3])

# Statistical functions

print (ser.sum ())
print (ser.min ())
print (ser.max ())
print (ser.mean ())
print (ser.count ())
print (ser.median ())
print (ser.mode ())

# Count of unique values, categorises them

print (ser.value_counts ())

# Sorting in either increasing or decreasing order

print (ser.sort_values ())

# For descending order - set ascending to false

print (ser.sort_values (ascending=False)) 

