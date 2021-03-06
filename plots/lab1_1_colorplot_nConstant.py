import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

NUM_COLORS = 10

with open("lab1_1_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()

i = 0;

colors = [[] for y in range(100)]
m = [[] for y in range(100)]

for x in range (0, 100):
    iter = trials[x].split(" ")
    nodes = int(iter[0]);
    index = (nodes/10) - 1
    colors[index].append(float(iter[2]))
    m[index].append(float(iter[1])/((nodes*(nodes-1))/2) *100)



cm = plt.get_cmap('gist_rainbow')    
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
ax.set_xlim(10,100)
ax.set_ylim(0,100)
    
for x in range (0, 10):
    #plt.scatter(m[x], time[x])
    ax.plot(np.unique(m[x]), np.poly1d(np.polyfit(m[x], colors[x], 1))(np.unique(m[x])), label = "n="+str((x+1)*10)+ " r={}")
    stats = np.polyfit(m[x],colors[x],1,full=True)
    print("n="+str((x+1)*10)+" r="+str(stats))
    


plt.suptitle('Average Number of Colors')
plt.xlabel('m % of maximum edges')
plt.ylabel('Colors')
plt.legend(loc=2)
plt.show();

