import pandas as pd

irisdf = pd.read_csv ('/Users/arjunbubbar/Desktop/Jetlearn/Data Science/iris.csv')

print (irisdf.head ())

print('\nMean values:')

print('Petal Length Mean:', irisdf['petal_length'].mean())
print('Petal Width Mean:', irisdf['petal_width'].mean())
print('Sepal Length Mean:', irisdf['sepal_length'].mean())
print('Sepal Width Mean:', irisdf['sepal_width'].mean())

print('\nMinimum values:')

print('Petal Length Min:', irisdf['petal_length'].min())
print('Petal Width Min:', irisdf['petal_width'].min())
print('Sepal Length Min:', irisdf['sepal_length'].min())
print('Sepal Width Min:', irisdf['sepal_width'].min())

print('\nMaximum values:')

print('Petal Length Max:', irisdf['petal_length'].max())
print('Petal Width Max:', irisdf['petal_width'].max())
print('Sepal Length Max:', irisdf['sepal_length'].max())
print('Sepal Width Max:', irisdf['sepal_width'].max())

print('\nCount:',irisdf['species'].value_counts())


titanicdf = pd.read_csv ('/Users/arjunbubbar/Desktop/Jetlearn/Data Science/titanic.csv')

print ('\nMean Fares:')

print ('Male Class 1:', titanicdf [(titanicdf ['Sex'] == 'male') & (titanicdf ['Pclass'] == 1)]['Fare'].mean ())
print ('Female Class 1:', titanicdf [(titanicdf ['Sex'] == 'female') & (titanicdf ['Pclass'] == 1)]['Fare'].mean ())
print ('Male Class 2:', titanicdf [(titanicdf ['Sex'] == 'male') & (titanicdf ['Pclass'] == 2)]['Fare'].mean ())
print ('Female Class 2:', titanicdf [(titanicdf ['Sex'] == 'female') & (titanicdf ['Pclass'] == 2)]['Fare'].mean ())
print ('Male Class 3:', titanicdf [(titanicdf ['Sex'] == 'male') & (titanicdf ['Pclass'] == 3)]['Fare'].mean ())
print ('Female Class 3:', titanicdf [(titanicdf ['Sex'] == 'female') & (titanicdf ['Pclass'] == 3)]['Fare'].mean ())

print ('\nMales')

print ('Mean of who did not survive:', titanicdf [(titanicdf ['Sex'] == 'male') & (titanicdf ['Survived'] == 0)]['Age'].mean())
print ('Median of who did not survive:', titanicdf [(titanicdf ['Sex'] == 'male') & (titanicdf ['Survived'] == 0)]['Age'].median())

print ('\nFemales')

print ('Mean of who did not survive:', titanicdf [(titanicdf ['Sex'] == 'female') & (titanicdf ['Survived'] == 0)]['Age'].mean())
print ('Median of who did not survive:', titanicdf [(titanicdf ['Sex'] == 'female') & (titanicdf ['Survived'] == 0)]['Age'].median())


# WHOLE TASK EASIER WITH GROUPING AND AGGREGATION

survivedsex = titanicdf.groupby (['Survived', 'Sex'])

meanvalue = survivedsex ['Age'].mean ()

print (meanvalue)
print (meanvalue [[(0,'male'), (0, 'female')]])

# Need two square brackets, one for slicing, one for the list if fetching multiple columns


