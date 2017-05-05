import json
import numpy as np
import re
with open('lab1_1a_greedy_results.json') as data_file:    
    data = json.load(data_file)

results = [[0 for x in range(100)] for y in range(100)] 
    
for x in range (0, 100):
    iter = data[str(x)]
    for y in range (0, 100):
        graphstring = iter.keys()[y]
        graphstringclean = re.sub("[^0-9+_]","",graphstring)
        graphstringclean = graphstringclean.split("_")
        n = graphstringclean[1]
        m = graphstringclean[2]
        colors = int(iter[graphstring]['colors'])
        time = float(iter[graphstring]['time'])
        results[x][y] = str(n)+ " "+str(m) +" "+ str(colors)+ " "+ str(time)


for x in range (0,100):
    c= []
    t = []
    for y in range(0,100):
        iter = results[y][x].split(" ")
        n = iter[0]
        m = iter[1]
        c.append(int(iter[2]))
        t.append(float(iter[3]))
    c_mean = np.mean(c)
    t_mean = np.mean(t)
    c_var = np.var(c, ddof=1)
    t_var = np.var(t, ddof=1)
    print(str(n) + " " +str(m)+ " " +str(c_mean) +" " + str(t_mean) +" "+ str(c_var) + " " +str(t_var))
            
        
    
