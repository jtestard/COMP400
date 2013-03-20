'''
Created on Feb 4, 2013

This file was used to profile the memory usage of the zen library
under the following circumstances :
    -    Memory used by the python framework and zen library alone.
    -    Memory used by a graph once loaded into memory, we try with graphs of different size.
    
IMPORTANT : This file uses memory usage profiling methods specific to the Linux operating system.
@author: jtesta
'''

#This is a module I wrote which contains simple methods for profiling in python. I write 
#my results in .csv files to generate graphs for this profiling.
import profile
import gc #For garbage collection
import random
import timeout
import platform

#Importing Zen
import zen
import zen.io.memlist as memlist
vm_zen_python = round(profile.memory()/1024)
ram_zen_python = round(profile.resident()/1024)
#print 'Virtual Memory used by python and the zen framework ', vm_zen_python, 'kb'
#print 'RAM used by python and the zen framework ', ram_zen_python, 'kb'

max_size = 20000
increment = 1000
TOTAL_RAM = 150*1024*1024

def read_partition_info(partType,graphType,size):
    filename = type+string(size)+".graph"
    global partitions
    partitions = {}
    file = open('storage/partitions/'+partType+'/'+graphType+'/'+filename)
    s

def k_neighbours(k,graph):
    "nothing yet"

def profile_graph(type):
    global max_size,increment
    print 'Looking at partition usage for k-bounded queries in' + type + " graphs!"
    file = open('csv/' + type + '_graphs_partitions.csv', 'w')
    file.write("StartNode K #PartitionsSearched\n")
    for i in range(increment,max_size+1,increment):
        #We want to profile the time taken to load each graph into memory for each category. 
        #We use manual garbage collection to make sure we are only keeping the minimum number of 
        #objects within memory
        gc.collect()
        
        #Load the graph from memory
        filename = type + str(i) + ".graph"
        profile.start_clock()
        G = memlist.read("storage/" + type + "/" + filename)
                
        #Execute a few shortest paths and take the maximum value as a reference.
        for j in range(sample):
            index = random.randint(0,i)
            #source = G.node_object(index)
            #zen.algorithms.shortest_path.single_source_shortest_path(G, index)
            #zen.algorithms.shortest_path.dijkstra_path(G,index)
            list[j] = profile.get_time_from_clock()
        difftime = max(list)
        shortestpathtime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
        
        #Execute a few clustering computations and take the maximum value as a reference.
        #zen.algorithms.clustering.ncc(G)
        difftime = profile.get_time_from_clock()
        ncctime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
        
        #zen.algorithms.clustering.lcc(G)
        difftime = profile.get_time_from_clock()
        lcctime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
        
        #zen.algorithms.clustering.gcc(G)
        difftime = profile.get_time_from_clock()
        gcctime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
        
        #zen.algorithms.spanning.minimum_spanning_tree(G)
        difftime = profile.get_time_from_clock()    
        msttime = str(difftime.seconds) + "." + str(difftime.microseconds/1000)
        
        print "Time for queries : SP=" + shortestpathtime + "seconds, NCC=" + ncctime + "seconds, LCC=" + lcctime + "seconds, GCC=" + gcctime + "seconds, MST=" + msttime
        file.write(str(i) + " " + str(filesize) + " " + loadtime + " " + str(vm_graph) + " " + str(ram_graph) + " " + shortestpathtime + " " + ncctime + " " + lcctime + " " + gcctime + " " + msttime + "\n")
        
#profile_graph("random")
#profile_graph("sparse")
#profile_graph("dense")
profile_graph("metric")