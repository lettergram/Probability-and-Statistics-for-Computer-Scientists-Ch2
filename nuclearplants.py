import numpy as np
import matplotlib.pyplot as plt 

matrix = np.genfromtxt('np.csv', delimiter=',')

date  = []
cost  = []
MWatt = []
costperMWatt = []

for row in matrix:
    costperMWatt.append(float(row[0]) / float(row[1]))
    cost.append(float(row[0]))
    MWatt.append(float(row[1]))
    date.append(int(row[2]))
    
ind = np.arange(len(date))  # the x locations for the groups
width = 0.2

fig, ax = plt.subplots()

rects1 = ax.bar(ind, cost, width, color='g')
rects2 = ax.bar(ind + width, MWatt, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('MWatts and Cost ($100,000) per Power Plant')
ax.set_xlabel('Date 1967 - 1971')
ax.set_title('MWatts and Cost per Nuclear Power Plant')
ax.set_xticks(ind+width)
ax.set_xticklabels(date)

ax.legend((rects1[0], rects2[0]), ('Cost', 'Power'),bbox_to_anchor = (1.1, 1.1), shadow=True, fancybox=True, ncol=2)

def label(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2.0, 1.02 * height, '%d' % int(height),
                ha='center', va='bottom')

label(rects1)
label(rects2)

print 'Power Mean: ' + str(np.mean(MWatt))
print 'Power Standard Deviation: ' + str(np.std(MWatt))
print 'Cost Mean: ' + str(np.mean(cost))
print 'Cost Standard Deviation: ' + str(np.std(cost))
print 'Cost per MWatt Mean: ' + str(np.mean(costperMWatt))
print 'Cost per MWatt Standard Deviation: ' + str(np.std(costperMWatt))

plt.show()

fig, bx = plt.subplots()

rects3 = bx.bar(ind, costperMWatt, width, color='r')

bx.set_ylabel('Cost ($100,000) per MWatt')
bx.set_xlabel('Date 1967 - 1971')
bx.set_title('Cost per MWatt From a Nuclear Power Plant')
bx.set_xticks(ind+width)
bx.set_xticklabels(date)

i = 0
for rect in rects3:
    height = rect.get_height()
    bx.text(rect.get_x() + rect.get_width() / 2.0, 1.02 * height, '%3.2f' % height,
            ha='center', va='bottom')
plt.show()
