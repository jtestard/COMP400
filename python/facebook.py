'''
Created on April 4, 2013

@author: jtesta
'''

if __name__ == '__main__':
    pass

file = open('storage/edgelist/facebook/facebook.graph', 'r')
edgesA = []
edgesB = []
for line in file :
    pair = line.split(" ")
    if int(pair[1]) in edgesA and :
            edgesA.append(int(pair[0]))
            edgesB.append(int(pair[1]))

        
file.close()
edges = sorted(edges,key=str.lower)
file = open('storage/edgelist/facebook/facebook_cpy.graph', 'w')
for line in edges :
    file.write(line)
file.close()