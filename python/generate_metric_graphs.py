'''
Created on Feb 4, 2013

The metric graph is designed such that the closer two nodes are (here we mean by distance the difference in node index
between two nodes), the higher the chance of an edge between them.

@author: jtesta
'''

if __name__ == '__main__':
    pass

import zen
import profile
import random
import zen.io.memlist as memlist

max_size = 20000
increment = 1000

profile.start_clock()
file = open('csv/metric_graphs.csv', 'w')
file.write("Nodes GenerateTime SaveTime FileSize\n")
#The +1 on the max size is just to be sure we include the max size in our range.
for i in range(increment,max_size+1,increment):
    #Defines the maximum degree per node
    max_degree = i*0.1;
    G = zen.Graph()
    for j in range(i):
        G.add_node(j)
    
    #Define edges for each node
    for j in range(i):
        k = 0
        while k < max_degree:
            x = random.randint(1,max_degree)
            x = round(random.uniform(0,1)*random.uniform(0,1)*x)
            other_node = (j+x) % i
            if not G.has_edge(j,other_node):
                G.add_edge(j,other_node)
            k+=1
    G.compact()
    filename = 'metric' + str(i) + ".graph"
    
    #Profiling generation time
    difftime = profile.get_time_from_clock()
    gentime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " has taken " + gentime + " to generate."
    
    #Saving the generated graph
    memlist.write(G,'storage/metric/' + filename)
    filesize = profile.filesize('storage/metric/' + filename)
    filesize = filesize/1024
    
    #Profiling IO time
    difftime = profile.get_time_from_clock()
    savetime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " (" + str(filesize) + "kB), has taken " + savetime + " seconds to save on disk."
    file.write(str(i) + " " + gentime + " " + savetime + " " + str(filesize) + "\n")

