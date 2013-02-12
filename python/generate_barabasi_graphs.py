'''
Created on Feb 4, 2013

The graphs generated here follow the barabsi model.

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
file = open('csv/barabasi_graphs.csv', 'w')
file.write("GraphName GenerateTime SaveTime FileSize\n")
#The +1 on the max size is just to be sure we include the max size in our range.
for i in range(increment,max_size+1,increment):
    #Defines the maximum degree per node
    G = zen.generating.barabasi_albert(i,0.01*i);
    G.compact()
    filename = 'barabasi' + str(i) + ".graph"
    
    #Profiling generation time
    difftime = profile.get_time_from_clock()
    gentime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " has taken " + gentime + " to generate."
    
    #Saving the generated graph
    memlist.write(G,'storage/barabasi/' + filename)
    filesize = profile.filesize('storage/barabasi/' + filename)
    filesize = filesize/1024
    
    #Profiling IO time
    difftime = profile.get_time_from_clock()
    savetime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
    print "Graph " + filename + " (" + str(filesize) + "kB), has taken " + savetime + " seconds to save on disk."
    file.write(filename + " " + gentime + " " + savetime + " " + str(filesize) + "\n")