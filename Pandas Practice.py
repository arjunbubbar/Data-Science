import pandas as pd

irisdf = pd.read_csv ('/Users/arjunbubbar/Desktop/Jetlearn/Data Science/Datasets/iris.csv')

print (irisdf.agg ({'petal_length':['min','max'],'petal_width':['min','max']}))

species = irisdf.groupby ('species')

print (species [['sepal_length','sepal_width']].mean ())

irisdf ['species'] = irisdf ['species'].str.upper ()

# Assign back to the dataframe to make changes 

print (irisdf ['species'])

print (species.median ())


