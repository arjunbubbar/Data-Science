import matplotlib.pyplot as plt

import pandas as pd

titanicdf = pd.read_csv ('/Users/arjunbubbar/Desktop/Jetlearn/Data Science/Datasets/titanic.csv')

pclass = titanicdf.groupby ('Pclass')['Pclass'].count()

print (pclass)

plt.bar (pclass.index, pclass.values)

plt.xlabel ('Passenger Class')
plt.ylabel ('Number of Passengers')
plt.title ('Passenger Count by Class')

plt.xticks (pclass.index)

plt.show ()

age = titanicdf ['Age']

plt.hist (age, bins = range (0,90,10), rwidth = 0.8)

plt.xlabel ('Age')
plt.ylabel ('Number of Passengers')
plt.title ('Age Distribution')

plt.show ()



irisdf = pd.read_csv ('/Users/arjunbubbar/Desktop/Jetlearn/Data Science/Datasets/iris.csv')

species = irisdf.groupby ('species')['species'].count()

print (species)

plt.pie (species.values, labels = species.index, autopct='%1.1f%%')

plt.title ('Species Distribution')

plt.show ()


plt.scatter(irisdf['petal_length'], irisdf['petal_width'])

plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.show()



















