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
file = open('csv/random_graphs.csv', 'w')
file.write("Nodes GenerateTime SaveTime FileSize\n")
#The +1 on the max size is just to be sure we include the max size in our range.
for i in range(increment,max_size+1,increment):
    edge_probability_1 = random.uniform(0,1.0)
    edge_probability_2 = random.uniform(0,1.0)
    edge_probability_3 = random.uniform(0,1.0)
    edge_probability_4 = random.uniform(0,1.0)
    edge_probability_5 = random.uniform(0,1.0)
    #I only want my graph to be dense with a small probability (average density = 0.03125*#nodes)
    G = zen.generating.rgm.erdos_renyi(i,edge_probability_1*edge_probability_2*edge_probability_3*edge_probability_4*edge_probability_5)
    G.compact()
    filename = 'random' + str(i) + ".graph"
    
    #Profiling generation time
    difftime = profile.get_time_from_clock()
    gentime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " has taken " + gentime + " to generate."
    
    #Saving the generated graph
    memlist.write(G,'storage/random/' + filename)
    filesize = profile.filesize('storage/random/' + filename)
    filesize = filesize/1024
    
    #Profiling IO time
    difftime = profile.get_time_from_clock()
    savetime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " (" + str(filesize) + "kB), has taken " + savetime + " seconds to save on disk."
    file.write(str(i) + " " + gentime + " " + savetime + " " + str(filesize) + "\n")