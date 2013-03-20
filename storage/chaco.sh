#First need to install chaco at http://www.cs.sandia.gov/~bahendr/chaco.html.
#then need to add the following to .bashrc file:
#		-		PATH=$HOME/Chaco-2.2/exec:$PATH

#Then need to change the default config file by adding and copy it to the sh directory.
#		-		OUTPUT_ASSIGN = TRUE
#		-		ECHO = -2
#		-		PROMPT = FALSE

#I added the chaco executable to my path in order to call the command 'chaco'".
#You can either do like me or replace the calls to 'chaco' by the path to the executable.

#Cleaning previous runs
echo "Cleaning previous runs..."
rm runs/KL/sparse/*.graph

#Computing partitions for sparse files.
#This file computes partitions for 
echo "The partitioning algorithm has the following parameters :"
echo "	-	Partitioning method : kernighan lin."
echo "	-	#Partitions : 16."

#Computing partitions for sparse files.
for i in {1000..20000..1000}; do
	echo "Processing partition for sparse$i.graph..."
	first = $'vertex/sparse/sparse'
	second = $'.graph\npartitions/KL/sparse/sparse'
	third = $'.graph\n5\n1\n4\n1\nn'
	echo $first:$i:$second:$i:$third
	#echo $'vertex/sparse/sparse'$"$i.graph\npartitions/KL/sparse/sparse$i.graph\n5\n1\n4\n1\nn'
	#echo $'vertex/sparse/sparse'"$i"'.graph\npartitions/KL/sparse/sparse$i.graph\n5\n1\n4\n1\nn' | chaco >> runs/KL/sparse/sparse$i.run
done