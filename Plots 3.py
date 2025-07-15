# Create a subplot with 2 rows and 3 columns with the following plots:
# In row 1 column 2 add a scatter plot between years of experience and salary
# In row 2 column 1 add a histogram for years of experience in 5-year interval
# In row 2 column 3 add a histogram for salary in an interval of 10000
# In row 1 colum 3 add a bar plot with the mean salary of employees with experience of 1-5, 5-10 and 10-15 years.


import matplotlib.pyplot as plt

import pandas as pd 

import numpy as np

salarydf = pd.read_csv ('/Users/arjunbubbar/Desktop/Jetlearn/Data Science/Datasets/Salary.csv')


plt.subplot (2,3,2)

plt.scatter (salarydf ['YearsExperience'], salarydf ['Salary'])

plt.subplot (2,3,4)

maximum = salarydf ['YearsExperience'].max ()

bins = np.arange (0, maximum, 5)

plt.hist (salarydf ['YearsExperience'], bins)

plt.subplot (2,3,6)

maximum2 = salarydf ['Salary'].max ()

bins2 = np.arange (0, maximum2, 10000)

plt.hist (salarydf ['Salary'], bins2)

plt.subplot (2,3,3)

x = salarydf.loc [(salarydf ['YearsExperience'] >= 1) & (salarydf ['YearsExperience'] <= 5), 'Salary'].mean ()

y = salarydf.loc [(salarydf ['YearsExperience'] >= 5) & (salarydf ['YearsExperience'] <= 10), 'Salary'].mean ()

z = salarydf.loc [(salarydf ['YearsExperience'] >= 10) & (salarydf ['YearsExperience'] <= 15), 'Salary'].mean ()

plt.bar (['1-5','5-10','10-15'], [x,y,z])

plt.show ()



