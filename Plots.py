import matplotlib.pyplot as plt

import numpy as np


# Creating a plot 

# x = np.arange (1,11)

# y = 2 * x + 3


# # Line plot, just plot can change to any other data visualisation - give figure size in inches (w,h), colour, lines, o/^, labels displayed by legend, show at the end, stick to values with ticks


# plt.figure (figsize = (8,6))

# plt.plot (x,y,'r--o', linewidth = 5, label = 'y=2x+3')

# plt.legend ()

# plt.title ('Line Plot')

# plt.xlabel ('x values')

# plt.ylabel ('y values')

# plt.xticks (ticks = x, labels = x), masking, can be done on both axes

# plt.xticks (ticks = x, labels = ['a','b','c','d','e','f','g','h','i','j'])

# plt.show ()


# Multiple line plots on the same figure (smoother curve decrease the step)


# x = np.arange (1,11,0.01)

# plt.figure (figsize = (8,6))

# plt.plot (x, x**2, 'r-', label = 'y = x^2')

# plt.plot (x, x**3, 'g-', label = 'y = x^3')

# plt.legend ()

# plt.show ()


# Bar chart (how many bars in the third part)


# x = np.arange (1,10,2)

# y = np.random.randint (30,51,5)

# plt.bar (x,y)

# # Multiple bar plots

# a = np.arange (2,11,2)

# b = np.random.randint (30,101,5)

# plt.bar (a,b)

# plt.show ()

# Bar plots with categorical values

# x = ['black','brown','grey','blonde']

# y = np.random.randint (5,25,4)

# plt.bar (x,y)

# plt.show ()


# Histograms, will just give frequences for intervals from random array (rwidth is for separating, take up less space)

# x = np.random.randint (20,60,50)

# print (x)

# bins = np.arange (20,61,10)

# plt.hist (x,bins, rwidth = 0.8)

# plt.show ()


# Scatter plot, just data points (s - size of the points)

# x = np.arange (100,110)

# y = np.random.randint (1,25,10)

# plt.scatter (x,y, color = 'r', s = 50, marker = '^')

# plt.show ()


# Pie chart, calculates percentage of total for each category, autopct format percentage

# subjects = ['maths', 'coding', 'finance', 'history', 'politics']

# score = [8,10,8,2,4]

# plt.pie (score, labels = subjects, autopct='%1.1f%%')

# plt.show ()


# Stack plot

# reading = [1,2,1,3,2]

# football = [0,2,0,3,0]

# piano = [0.5,1,1,2,5]

# dog = [1,2,10,5,2.5]

# activities = ['reading','football','piano','dog']

# days = ['monday','tuesday','wednesday','thursday','friday']

# plt.stackplot (days,reading, football, piano, dog, labels = activities, colors = ['r','c','g','y'])

# plt.legend ()

# plt.show ()


# Sub plots, subplot divided into 2 by 2 for example and then what part of the grid

# x = np.arange (1,11)

# y1 = 2 * x + 7

# y2 = x**2 - 3

# plt.subplot (2,2,1)

# plt.plot (x,y1)

# plt.subplot (2,2,4)

# plt.scatter (x,y2)

# plt.show ()


