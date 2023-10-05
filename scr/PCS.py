import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys, os

# read the file in data and declare the type of the variable 
# since is not a standard file format this is the loader
# then convert all into a dataframe 
categories = []
reference = []
tested = []
t_difference = []

path = os.chdir("/Users/zhanz0h/Desktop/MLR-PCS/plot_test/tests")
pcs_file = glob.glob('*.pcs')[0]

        
for line in open(pcs_file).readlines():
    words = line.split()
    if len(words) == 4:
        # print (words)
        categories.append(words[0])
        reference.append(float(words[1]))
        tested.append(float(words[2]))
        t_difference.append(float(words[3]))
#title = line

plot_chart = np.add(reference, t_difference)     
data = {'categories': categories, 'reference': reference, 'tested': tested, 't_difference': t_difference, pcs_file: plot_chart}
df = pd.DataFrame(data)




# to close the radar, duplicate the first column
categories = np.concatenate((categories, [categories[0]]))

reference = np.concatenate((reference, [reference[0]]))
tested = np.concatenate((tested, [tested[0]]))
t_difference = np.concatenate((t_difference, [t_difference[0]]))
plot_chart = np.concatenate((plot_chart, [plot_chart[0]]))

# We have 12 categories the radar chart should have 12 radial axis
# To find out the angle of each quadrant we divide 360/12 = 30 degree
# Angle need to be 
label_placement = np.linspace(start = 0, stop = 2 * np.pi, num = len(categories))
#print(len(categories))
#print(reference[2])

plt.figure(figsize=(8,8), facecolor = 'white')
ax = plt.subplot(polar = True)

ax.plot(label_placement, reference, 'o--', color = 'green')
ax.plot(label_placement, plot_chart, 'o-', color = 'red')

# Fix axis to go in the right order and start at 12 o'clock.
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw axis lines for each angle and label.
lines, labels = ax.set_thetagrids(np.degrees(label_placement), labels = categories)


# Go through labels and adjust alignment based on where
# it is in the circle.
for label, angle in zip(ax.get_xticklabels(), label_placement):
    if 0 < angle < np.pi:
        label.set_horizontalalignment('left')
    else:
        label.set_horizontalalignment('right')



    
for i in range(len(categories)):
    ax.text(label_placement[i], reference[i] + 0.08, f'{reference[i]:.2f}', ha='center', va='center', color='green')
    ax.text(label_placement[i], plot_chart[i] - 0.08, f'{plot_chart[i]:.2f}', ha='center', va='center', color='red')
        


# Draw ylabels
ax.set_rlabel_position(0)
#plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.yticks([0,0.2,0.4,0.6,0.8,1.0,1.2], ["0","0.2","0.4","0.6","0.8","1.0", "1.2"], color="grey", size=10)
# plt.ylim(0,40)
plt.ylim(0,1.3)





ax.legend(labels = ['reference', pcs_file], loc = (0.95, 0.95))
#plt.title(title)
