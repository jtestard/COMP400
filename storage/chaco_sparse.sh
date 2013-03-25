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
rm runs/KL/sparse/*.run
rm runs/KL/big/sparse/*.run
rm runs/KL/small/sparse/*.run
rm runs/random/sparse/*.run
rm runs/random/big/sparse/*.run
rm runs/random/small/sparse/*.run

#Computing KL partitions for sparse files.
for i in {1000..20000..1000}; do
	echo "Processing KL partition for sparse$i.graph..."
	echo -e "vertex/sparse/sparse$i.graph\npartitions/KL/sparse/sparse$i.graph\n1\n100\n4\n1\nn" | chaco >> runs/KL/sparse/sparse$i.run
done

#Computing random partitions for sparse files.
for i in {1000..20000..1000}; do
	echo "Processing random partition for sparse$i.graph..."
	echo -e "vertex/sparse/sparse$i.graph\npartitions/random/sparse/sparse$i.graph\n5\n1\n4\n1\nn" | chaco >> runs/random/sparse/sparse$i.run
done

#This file computes partitions for 
echo "The partitioning algorithm has the following parameters :"
echo "	-	Partitioning method : kernighan lin."
echo "	-	#Partitions : 64."


#Computing KL partitions for sparse files.
for i in {1000..20000..1000}; do
	echo "Processing KL partition (small) for sparse$i.graph..."
	echo -e "vertex/sparse/sparse$i.graph\npartitions/KL/smallparts/sparse/sparse$i.graph\n1\n100\n6\n1\nn" | chaco >> runs/KL/smallparts/sparse/sparse$i.run
done

#Computing random partitions for sparse files.
for i in {1000..20000..1000}; do
	echo "Processing random partition (small) for sparse$i.graph..."
	echo -e "vertex/sparse/sparse$i.graph\npartitions/random/smallparts/sparse/sparse$i.graph\n5\n1\n6\n1\nn" | chaco >> runs/random/smallparts/sparse/sparse$i.run
done

#This file computes partitions for 
echo "The partitioning algorithm has the following parameters :"
echo "	-	Partitioning method : kernighan lin."
echo "	-	#Partitions : 64."


#Computing KL partitions for sparse files.
for i in {1000..20000..1000}; do
	echo "Processing KL partition (big) for sparse$i.graph..."
	echo -e "vertex/sparse/sparse$i.graph\npartitions/KL/bigparts/sparse/sparse$i.graph\n1\n100\n2\n1\nn" | chaco >> runs/KL/bigparts/sparse/sparse$i.run
done

#Computing random partitions for sparse files.
for i in {1000..20000..1000}; do
	echo "Processing random partition (big) for sparse$i.graph..."
	echo -e "vertex/sparse/sparse$i.graph\npartitions/random/bigparts/sparse/sparse$i.graph\n5\n1\n2\n1\nn" | chaco >> runs/random/bigparts/sparse/sparse$i.run
done