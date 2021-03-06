import numpy as np
import argparse
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

NUM_COLORS = 10

with open("lab1_1_summary_stats.txt") as input_file:
    trials = input_file.read().splitlines()

i = 0;

time = [100]
m = [100]

for x in range (0, 100):
    iter = trials[x].split(" ")
    nodes = int(iter[0]);
    index = (nodes/10) - 1
    time.append((float(iter[3])))
    m.append(float(iter[1]))



cm = plt.get_cmap('gist_rainbow')    
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
ax.set_xlim(0,5000)
ax.set_ylim(0,20)
plt.scatter(m, time, color=(cm(1.*9/NUM_COLORS)))
ax.plot(np.unique(m), np.poly1d(np.polyfit(m, time, 1))(np.unique(m)))


m.pop(0)
time.pop(0)

for x in range(0,100):
    print(str(m[x])+","+str(time[x]))

plt.suptitle('Runtime average')
plt.xlabel('m edges')
plt.ylabel('Runtime in Milliseconds')
plt.legend(loc=2)
plt.show();

