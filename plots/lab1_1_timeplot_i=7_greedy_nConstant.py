import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

NUM_COLORS = 10

def roundup(x):
    return int(math.ceil(x /10.0)) *10

with open("lab1_1_random_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()

i = 0;

time = [100]
m = [100]

for x in range (0, 1200):
    iter = trials[x].split(" ")
    if(int(iter[6]) == 7):
        time.append(float(iter[3]))
        m.append(int(iter[1]))

cm = plt.get_cmap('gist_rainbow')
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
ax.set_xlim(10,5000)
ax.set_ylim(0,max(time))

m.pop(0)
time.pop(0)
m.pop(99)
time.pop(99)

for x in range (0, 10):
    plt.scatter(m, time, color=(cm(1.*5/NUM_COLORS)))
    ax.plot(np.unique(m), np.poly1d(np.polyfit(m, time, 1))(np.unique(m)))

for x in range (0, 98):
    print(str(m[x])+","+str(time[x]))

plt.suptitle('Runtime average')
plt.xlabel('Edges')
plt.ylabel('Runtime in Milliseconds')
plt.legend(loc=2)
plt.show()