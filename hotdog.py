'''
Question 2.12 in Probability and Statistics for Computer Scientists, D.A. Forsyth (Sep 2014)

You can find a dataset giving the sodium content and calorie content of three types of hot dog at http://lib.stat.cmu.edu/DASL/Datafiles/Hotdogs.html. The types are Beef, Poultry, and Meat (a rather disturbingly vague label). Use class-conditional histograms to compare these three types of hot dog with re- spect to sodium content and calories.

CURRENTLY BROKEN!!!!

'''

import numpy as np
import matplotlib.pyplot as plt 

# Loads hot-dogs.csv into matrix, seperator = ', and \n'
matrix = np.genfromtxt('hot-dogs.csv', delimiter=',')

print matrix

Food = []
Calories = []
Sodium = []

# Loads the various Food, Cal, Sod from matrix into categories
for row in matrix:
    print row
    Food.append(str(row[0]))
    Calories.append(int(row[1]))
    Sodium.append(int(row[2]))

ind = np.arange(len(Food)) # the x locations for various groups
width = 0.2

fig, ax = plt.subplots()

rects1 = ax.bar(ind, Calories, width, color='g')
rects2 = ax.bar(ind + width, Sodium, width, color='y')

# Add some text for labels, title and axes ticks
ax.set_ylabel('Calories & Milligrams of Sodium')
ax.set_xlabel('Hotdog Type')
ax.set_title('Hotdog Type vs Calories & Sodium in mg')
ax.set_xticks(ind+width)
ax.set_xticklabels(Food)

ax.legend((rects1[0], rects2[0]), ('Calories', 'Sodium'),bbox_to_anchor = (1.1, 1.1), shadow=True, fancybox=True, ncol=2)

# attach some text labels
def label(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2.0, 1.02 * height, '%d' % int(height),
                ha='center', va='bottom')

label(rects1)
label(rects2)

plt.show()
