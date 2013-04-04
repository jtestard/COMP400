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

#max_size = 20000
max_size = 41000
increment = 10000
start = 1000
sample_size = 100
#Reads the partition information and returns it in a format that the system can use for it's analysis.
def read_partition_info(method,graphType,size):
    filename = str(graphType)+str(size)+".graph"
    partitions = []
    file = open('storage/partitions/'+method+'/'+graphType+'/'+filename, "r")
    for line in file:
        partitions.append(int(line))
    file.close()
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
    print 'Looking at partition usage for k-bounded queries in ' + type + " graphs!"
    if not size=='normal' :
        method += '/'+size
    file = open('csv/'+method+'/' + type + '_graphs_partitions.csv', 'w')
    file.write(method+","+type+" k=1 k=2 k=3 k=4\n")
    
    if type != 'facebook':
        for i in range(start,max_size+1,increment):
            #We want to profile the time taken to load each graph into memory for each category. 
            #We use manual garbage collection to make sure we are only keeping the minimum number of 
            #objects within memory
            gc.collect()
            
            #Load the graph and partitions from disk
            partitions = read_partition_info(method,type,i)
            filename = type + str(i) + ".graph"
            G = edgelist.read("storage/edgelist/" + type + "/" + filename)
            nodes = G.nodes()
            print "Querying for " + size + " graph : " + filename + " using the " + method + " method...\n"
            partitionsAcc = [[0]*sample_size for _ in range(4)]
            #Collect some data about your queries
            for j in range(0,sample_size-1):
                sourceIndex = random.randint(0,len(nodes)-1)
                source = int(nodes[sourceIndex])
                partitionsQuery = []
                nodesVisited=[]
                k_neighbours(1,source,G,partitions,partitionsQuery,nodesVisited)
                partitionsAcc[0][j] = len(partitionsQuery)
                partitionsQuery = []
                nodesVisited=[]
                k_neighbours(2,source,G,partitions,partitionsQuery,nodesVisited)
                partitionsAcc[1][j] = len(partitionsQuery)
                partitionsQuery = []
                nodesVisited=[]
                k_neighbours(3,source,G,partitions,partitionsQuery,nodesVisited)
                partitionsAcc[2][j] = len(partitionsQuery)
                partitionsQuery = []
                nodesVisited=[]
                k_neighbours(4,source,G,partitions,partitionsQuery,nodesVisited)
                partitionsAcc[3][j] = len(partitionsQuery)
            
            file.write(filename+" ")
            for j in range(0,3):
                file.write(str(float(sum(partitionsAcc[j]))/float(len(partitionsAcc[j])) ) + " ")
            file.write(str(float(sum(partitionsAcc[3]))/float(len(partitionsAcc[3]))) + "\n")       
    else :
        gc.collect()
        partitions = read_partition_info(method,type,"")
        filename = type + ".graph"
        G = edgelist.read("storage/edgelist/" + type + "/" + filename)
        nodes = G.nodes()
        print "Querying for " + size + " graph : " + filename + " using the " + method + " method...\n"
        partitionsAcc = [[0]*sample_size for _ in range(4)]
        #Collect some data about your queries
        for j in range(0,sample_size-1):
            sourceIndex = random.randint(0,len(nodes)-1)
            source = int(nodes[sourceIndex])
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(1,source,G,partitions,partitionsQuery,nodesVisited)
            partitionsAcc[0][j] = len(partitionsQuery)
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(2,source,G,partitions,partitionsQuery,nodesVisited)
            partitionsAcc[1][j] = len(partitionsQuery)
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(3,source,G,partitions,partitionsQuery,nodesVisited)
            partitionsAcc[2][j] = len(partitionsQuery)
            partitionsQuery = []
            nodesVisited=[]
            k_neighbours(4,source,G,partitions,partitionsQuery,nodesVisited)
            partitionsAcc[3][j] = len(partitionsQuery)
        
        file.write(filename+" ")
        for j in range(0,3):
            file.write(str(float(sum(partitionsAcc[j]))/float(len(partitionsAcc[j])) ) + " ")
        file.write(str(float(sum(partitionsAcc[3]))/float(len(partitionsAcc[3]))) + "\n")
    file.close()
        
#profile_graph("random")
#profile_graph("sparse","random","normal")
#profile_graph("sparse","KL","normal")
#profile_graph("sparse","KL","big")
#profile_graph("sparse","random","big")
#profile_graph("sparse","KL","small")
#profile_graph("sparse","random","small")
#profile_graph("barabasi","KL","normal")
#profile_graph("barabasi","random","normal")
#profile_graph("barabasi","KL","big")
#profile_graph("barabasi","random","big")
#profile_graph("barabasi","KL","small")
#profile_graph("barabasi","random","small")
#profile_graph("barabasi","KLEdgeCosts","normal")
#profile_graph("barabasi","KLEdgeCosts","small")
#profile_graph("barabasi","KLEdgeCosts","big")
#profile_graph("dense")
#profile_graph("metric")
profile_graph("facebook","KL","normal")
profile_graph("facebook","random","normal")
profile_graph("facebook","KL","big")
profile_graph("facebook","random","big")
profile_graph("facebook","KL","small")
profile_graph("facebook","random","small")