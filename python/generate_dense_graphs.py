'''
Created on Feb 4, 2013

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
file = open('csv/dense_graphs.csv', 'w')
file.write("Nodes GenerateTime SaveTime FileSize\n")
#The +1 on the max size is just to be sure we include the max size in our range.
for i in range(increment,max_size+1,increment):
    edge_probability = random.uniform(0,1.0)
    scaling = 0.05
    base_value = 0.05
    #Graphs of this category are potentially very big (average node degree = 0.0725*#nodes), which means the 20,000 node graph may have up to 4,000,000 edges.
    #which would be a graph of size 600MB.
    G = zen.generating.rgm.erdos_renyi(i,edge_probability*scaling+base_value)
    G.compact()
    filename = 'dense' + str(i) + ".graph"
    
    #Profiling generation time
    difftime = profile.get_time_from_clock()
    gentime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " has taken " + gentime + " to generate."
    
    #Saving the generated graph
    memlist.write(G,'storage/dense/' + filename)
    filesize = profile.filesize('storage/dense/' + filename)
    filesize = filesize/1024
    
    #Profiling IO time
    difftime = profile.get_time_from_clock()
    savetime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " (" + str(filesize) + "kB), has taken " + savetime + " seconds to save on disk."
    file.write(str(i) + " " + gentime + " " + savetime + " " + str(filesize) + "\n")

