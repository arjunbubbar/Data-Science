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

# Get values of multiple columns

print (titanicdf [["Name","Age","Fare"]])

# Statistical summary of all numerical columns, spread etc.

print (titanicdf.describe ())

# Filtering the rows, conditions

print (titanicdf [titanicdf ['Age'] > 18])

print (titanicdf [titanicdf ['Pclass'] == 1])

# Multiple conditions, use & (and), | (or)
 
print (titanicdf [(titanicdf ['Sex'] == 'female') & (titanicdf ['Pclass'] == 1)])

print (titanicdf [(titanicdf ['Age'] < 18) | (titanicdf ['Survived'] == 1)])

# Index based slicing - get part of rows and columns [sr:er, sc:ec], does not show last index, can also list indices

print (titanicdf.iloc [234:240, 3:6])

print (titanicdf.iloc [[2,4,5,6,764,342],[5,2,3]])

# Conditional slicing [Condition for rows, [column names in list] ]

print (titanicdf.loc [titanicdf ['Age'] > 18, ['Sex', 'Age', 'Pclass']])

# Changing values

titanicdf.loc [0:2, 'Name'] = ['John', 'Jack', 'Elizabeth']

print (titanicdf.head ())

# Add a column 

titanicdf ['Discounted Fare'] = titanicdf ['Fare'] / 2

print (titanicdf.head ())

# Rename column (inplace alters original dataset, makes changes permanent)

titanicdf.rename (columns = {'Pclass':'Passenger Class', 'Fare': 'Ticket Price'}, inplace = True) 

print (titanicdf.columns)

# Save dataframe changes at csv
# titanicdf.to_csv ('titanic2.csv')

# Sorting in increasing or decreasing order (by = some category)

print (titanicdf.sort_values (by = 'Passenger Class'))

print (titanicdf.sort_values (by = 'Passenger Class', ascending = False))

# Replacing a value (either specify on which column or on whole dataframe)

titanicdf ['Sex'].replace ({'male':'m','female':'f'}, inplace = True)

print (titanicdf ['Sex'])
