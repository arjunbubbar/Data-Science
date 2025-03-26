import matplotlib.pyplot as plt

import numpy as np

# Creating a plot 

x = np.arange (1,11)

y = 2 * x + 3

# Line plot, just plot can change to any other data visualisation - give figure size in inches (w,h), colour, lines, o/^, labels displayed by legend, show at the end, stick to values with ticks

plt.figure (figsize = (8,6))

plt.plot (x,y,'r--o', linewidth = 5, label = 'y=2x+3')

plt.legend ()

plt.title ('Line Plot')

plt.xlabel ('x values')

plt.ylabel ('y values')

# plt.xticks (ticks = x, labels = x), masking, can be done on both axes

plt.xticks (ticks = x, labels = ['a','b','c','d','e','f','g','h','i','j'])

plt.show ()