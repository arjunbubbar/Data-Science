import pandas as pd

# Creating a dataframe, appears in a table, rows are index, columns the categories, the series get converted into 2D

details = {'name':['john','amy','jack'], 'age': [23,21,28], 'gender': ['male','female','male']}

people = pd.DataFrame (details)

print (people)
print (type (people))

# Get column names

print (people.columns)

# Gives the index, start, stop and step

print (people.index)

# Read csv

titanicdf = pd.read_csv ('/Users/arjunbubbar/Desktop/Jetlearn/Data Science/titanic.csv')

print (titanicdf)

# Can get data from an external source, therefore use pandas

# Gives complete information

titanicdf.info ()

# Print first five rows, specify number in bracket if any other number

print (titanicdf.head ())
print (titanicdf.head (12))

# Print last five rows, specify number in bracket if any other number

print (titanicdf.tail (20))

# Finds row and columns, in tuple, so immutable

print (titanicdf.shape)

# Extracting values of one column, series is the result

print (titanicdf ['Fare'])

print (titanicdf ['Fare'].mean ())

print (titanicdf ['Pclass'].value_counts ())
