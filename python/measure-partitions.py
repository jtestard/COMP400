'''
Created on Feb 4, 2013

This file is meant to analyze how many partitions some queries are using when performing k-neighbour searches.
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
import zen.io.edgelist as edgelist

max_size = 20000
increment = 1000

#Reads the partition information and returns it in a format that the system can use for it's analysis.
def read_partition_info(method,graphType,size):
    filename = str(graphType)+str(size)+".graph"
    partitions = []
    file = open('storage/partitions/'+method+'/'+graphType+'/'+filename, "r")
    for line in file:
        partitions.append(int(line))
    return partitions

#returns the number of partitions in a k-neighbor search using a depth first search algorithm.
def k_neighbours(k,source,graph,partitionsAll,partitionsQuery,nodesVisited):
    #Base case
    if k<=0:
        return
    else:
        node = graph.node_object(source)
        if not node==None:
            for neighbour in graph.neighbors_iter(node):
                neighIndex = int(neighbour)
                if not neighIndex in nodesVisited:
                    nodesVisited.append(neighIndex)
                    neighbour_partition = partitionsAll[neighIndex]
                    if not neighbour_partition in partitionsQuery:
                        partitionsQuery.append(neighbour_partition)
                    k_neighbours(k-1,neighIndex,graph,partitionsAll,partitionsQuery,nodesVisited)
        else:
            print "WARN : Node "+str(source)+" has no object reference in graph G!"
        return
    
def profile_graph(type,method,size):
    global max_size,increment
    print 'Looking at partition usage for k-bounded queries in' + type + " graphs!"
    if not size=='normal' :
        method += '/'+size
    file = open('csv/'+method+'/' + type + '_graphs_partitions.csv', 'w')
    file.write("StartNode k=1 k=2 k=3 k=4\n")
    for i in [1000,1000,20000]:#range(increment,max_size+1,increment):
        #We want to profile the time taken to load each graph into memory for each category. 
        #We use manual garbage collection to make sure we are only keeping the minimum number of 
        #objects within memory
        gc.collect()
        
        #Load the graph and partitions from disk
        partitions = read_partition_info(method,type,i)
        filename = type + str(i) + ".graph"
        G = edgelist.read("storage/edgelist/" + type + "/" + filename)
        nodes = G.nodes()
        #Collect some data about your queries
        for j in range(1,10):
            sourceIndex = random.randint(0,len(nodes))
            source = int(nodes[sourceIndex])
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(1,source,G,partitions,partitionsQuery,nodesVisited)
            print "1-Query from node "+str(source)+" has accessed "+str(len(partitionsQuery))+"..."
            file.write(str(source)+" "+str(len(partitionsQuery)))
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(2,source,G,partitions,partitionsQuery,nodesVisited)
            print "2-Query from node "+str(source)+" has accessed "+str(len(partitionsQuery))+"..."
            file.write(" "+str(len(partitionsQuery)))
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(3,source,G,partitions,partitionsQuery,nodesVisited)
            print "3-Query from node "+str(source)+" has accessed "+str(len(partitionsQuery))+"..."
            file.write(" "+str(len(partitionsQuery)))
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(4,source,G,partitions,partitionsQuery,nodesVisited)
            print "4-Query from node "+str(source)+" has accessed "+str(len(partitionsQuery))+"..."
            file.write(" "+str(len(partitionsQuery))+"\n")
        file.write("\n")
        
#profile_graph("random")
#profile_graph("sparse","random","normal")
#profile_graph("sparse","KL","normal")
profile_graph("sparse","KL","big")
profile_graph("sparse","random","big")
profile_graph("sparse","KL","small")
profile_graph("sparse","random","small")
#profile_graph("dense")
#profile_graph("metric")